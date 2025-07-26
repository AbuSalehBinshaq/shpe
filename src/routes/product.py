from flask import Blueprint, request, jsonify, session
from src.models.user import db
from src.models.product import Product, SiteSettings
from datetime import datetime

product_bp = Blueprint('product', __name__)

# Helper function to check admin authentication
def is_admin():
    return session.get('admin_logged_in', False)

# Products endpoints
@product_bp.route('/products', methods=['GET'])
def get_products():
    """جلب جميع المنتجات النشطة"""
    try:
        products = Product.query.filter_by(is_active=True).order_by(Product.created_at.desc()).all()
        return jsonify({
            'success': True,
            'products': [product.to_dict() for product in products]
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'خطأ في جلب المنتجات: {str(e)}'
        }), 500

@product_bp.route('/admin/products', methods=['GET'])
def get_all_products():
    """جلب جميع المنتجات (للإدارة)"""
    if not is_admin():
        return jsonify({'success': False, 'message': 'غير مصرح بالوصول'}), 401
    
    try:
        products = Product.query.order_by(Product.created_at.desc()).all()
        return jsonify({
            'success': True,
            'products': [product.to_dict() for product in products]
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'خطأ في جلب المنتجات: {str(e)}'
        }), 500

@product_bp.route('/admin/products', methods=['POST'])
def create_product():
    """إضافة منتج جديد"""
    if not is_admin():
        return jsonify({'success': False, 'message': 'غير مصرح بالوصول'}), 401
    
    try:
        data = request.get_json()
        
        # التحقق من البيانات المطلوبة
        if not data.get('name') or not data.get('price'):
            return jsonify({
                'success': False,
                'message': 'اسم المنتج والسعر مطلوبان'
            }), 400
        
        # إنشاء منتج جديد
        product = Product(
            name=data['name'],
            description=data.get('description', ''),
            price=data['price'],
            image_url=data.get('image_url', ''),
            whatsapp_message=data.get('whatsapp_message', ''),
            is_active=data.get('is_active', True)
        )
        
        db.session.add(product)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'تم إضافة المنتج بنجاح',
            'product': product.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'خطأ في إضافة المنتج: {str(e)}'
        }), 500

@product_bp.route('/admin/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """تعديل منتج موجود"""
    if not is_admin():
        return jsonify({'success': False, 'message': 'غير مصرح بالوصول'}), 401
    
    try:
        product = Product.query.get_or_404(product_id)
        data = request.get_json()
        
        # تحديث البيانات
        if 'name' in data:
            product.name = data['name']
        if 'description' in data:
            product.description = data['description']
        if 'price' in data:
            product.price = data['price']
        if 'image_url' in data:
            product.image_url = data['image_url']
        if 'whatsapp_message' in data:
            product.whatsapp_message = data['whatsapp_message']
        if 'is_active' in data:
            product.is_active = data['is_active']
        
        product.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'تم تحديث المنتج بنجاح',
            'product': product.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'خطأ في تحديث المنتج: {str(e)}'
        }), 500

@product_bp.route('/admin/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """حذف منتج"""
    if not is_admin():
        return jsonify({'success': False, 'message': 'غير مصرح بالوصول'}), 401
    
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'تم حذف المنتج بنجاح'
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'خطأ في حذف المنتج: {str(e)}'
        }), 500

# Settings endpoints
@product_bp.route('/settings', methods=['GET'])
def get_settings():
    """جلب إعدادات الموقع"""
    try:
        settings = SiteSettings.query.first()
        if not settings:
            # إنشاء إعدادات افتراضية
            settings = SiteSettings()
            db.session.add(settings)
            db.session.commit()
        
        return jsonify({
            'success': True,
            'settings': settings.to_dict()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'خطأ في جلب الإعدادات: {str(e)}'
        }), 500

@product_bp.route('/admin/settings', methods=['PUT'])
def update_settings():
    """تحديث إعدادات الموقع"""
    if not is_admin():
        return jsonify({'success': False, 'message': 'غير مصرح بالوصول'}), 401
    
    try:
        settings = SiteSettings.query.first()
        if not settings:
            settings = SiteSettings()
            db.session.add(settings)
        
        data = request.get_json()
        
        # تحديث الإعدادات
        if 'site_title' in data:
            settings.site_title = data['site_title']
        if 'site_logo' in data:
            settings.site_logo = data['site_logo']
        if 'hero_title' in data:
            settings.hero_title = data['hero_title']
        if 'hero_subtitle' in data:
            settings.hero_subtitle = data['hero_subtitle']
        if 'whatsapp_number' in data:
            settings.whatsapp_number = data['whatsapp_number']
        if 'admin_password' in data:
            settings.admin_password = data['admin_password']
        
        settings.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'تم تحديث الإعدادات بنجاح',
            'settings': settings.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'خطأ في تحديث الإعدادات: {str(e)}'
        }), 500

# Authentication endpoints
@product_bp.route('/admin/login', methods=['POST'])
def admin_login():
    """تسجيل دخول الإدارة"""
    try:
        data = request.get_json()
        password = data.get('password')
        
        if not password:
            return jsonify({
                'success': False,
                'message': 'كلمة المرور مطلوبة'
            }), 400
        
        # جلب كلمة المرور من الإعدادات
        settings = SiteSettings.query.first()
        if not settings:
            settings = SiteSettings()
            db.session.add(settings)
            db.session.commit()
        
        if password == settings.admin_password:
            session['admin_logged_in'] = True
            return jsonify({
                'success': True,
                'message': 'تم تسجيل الدخول بنجاح'
            })
        else:
            return jsonify({
                'success': False,
                'message': 'كلمة المرور غير صحيحة'
            }), 401
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'خطأ في تسجيل الدخول: {str(e)}'
        }), 500

@product_bp.route('/admin/logout', methods=['POST'])
def admin_logout():
    """تسجيل خروج الإدارة"""
    session.pop('admin_logged_in', None)
    return jsonify({
        'success': True,
        'message': 'تم تسجيل الخروج بنجاح'
    })

@product_bp.route('/admin/check', methods=['GET'])
def check_admin():
    """التحقق من حالة تسجيل الدخول"""
    return jsonify({
        'success': True,
        'logged_in': is_admin()
    })

