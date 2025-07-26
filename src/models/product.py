from src.models.user import db
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    whatsapp_message = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Product {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image_url': self.image_url,
            'whatsapp_message': self.whatsapp_message,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class SiteSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_title = db.Column(db.String(200), default='مقدام')
    site_logo = db.Column(db.String(500), default='logo.jpg')
    hero_title = db.Column(db.String(300), default='مرحباً بكم في مقدام')
    hero_subtitle = db.Column(db.Text, default='اكتشفوا مجموعتنا المميزة من الأزياء التراثية الفاخرة، حيث يلتقي التراث الأصيل بالجودة العالية')
    whatsapp_number = db.Column(db.String(20), default='966500000000')
    admin_password = db.Column(db.String(200), default='admin123')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<SiteSettings {self.site_title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'site_title': self.site_title,
            'site_logo': self.site_logo,
            'hero_title': self.hero_title,
            'hero_subtitle': self.hero_subtitle,
            'whatsapp_number': self.whatsapp_number,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

