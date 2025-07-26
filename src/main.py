import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.models.product import Product, SiteSettings
from src.routes.user import user_bp
from src.routes.product import product_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'mogdam_store_secret_key_2024'

# Enable CORS for all routes
CORS(app)

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(product_bp, url_prefix='/api')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Initialize database and create sample data
with app.app_context():
    db.create_all()
    
    # Create default settings if not exists
    if not SiteSettings.query.first():
        default_settings = SiteSettings()
        db.session.add(default_settings)
        db.session.commit()
    
    # Create sample products if none exist
    if Product.query.count() == 0:
        sample_products = [
            Product(
                name="ثوب مقدام الفاخر",
                description="ثوب تراثي فاخر مصنوع من أجود الأقمشة، يجمع بين الأناقة والراحة",
                price="299 ريال",
                image_url="https://images.unsplash.com/photo-1583743089695-4b816a340f82?w=400",
                whatsapp_message="أرغب في الاستفسار عن ثوب مقدام الفاخر",
                is_active=True
            ),
            Product(
                name="عباءة مقدام الأنيقة",
                description="عباءة نسائية أنيقة بتصميم عصري وخامات فاخرة",
                price="399 ريال",
                image_url="https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400",
                whatsapp_message="أرغب في الاستفسار عن عباءة مقدام الأنيقة",
                is_active=True
            ),
            Product(
                name="شماغ مقدام الأصيل",
                description="شماغ تراثي أصيل بجودة عالية وألوان متميزة",
                price="149 ريال",
                image_url="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400",
                whatsapp_message="أرغب في الاستفسار عن شماغ مقدام الأصيل",
                is_active=True
            )
        ]
        
        for product in sample_products:
            db.session.add(product)
        
        db.session.commit()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
