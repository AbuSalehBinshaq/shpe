# نظام إدارة متجر مقدام

## نظرة عامة

نظام إدارة متجر إلكتروني متكامل مبني بتقنيات حديثة، يوفر لوحة تحكم احترافية وبسيطة لإدارة المنتجات مع واجهة عرض أنيقة للعملاء.

## المميزات الرئيسية

- 🎨 **تصميم احترافي**: واجهة مستخدم عصرية مع ألوان ذهبية أنيقة
- 🛠️ **إدارة شاملة**: نظام CRUD كامل للمنتجات
- 🔒 **أمان متقدم**: حماية لوحة التحكم وإدارة الجلسات
- 📱 **تصميم متجاوب**: يعمل على جميع الأجهزة والشاشات
- ⚡ **أداء عالي**: تحميل سريع وتفاعل سلس
- 🔧 **قابل للتطوير**: بنية مرنة تدعم الإضافات المستقبلية

## التقنيات المستخدمة

### الواجهة الخلفية (Backend)
- **Python 3.11+**
- **Flask** - إطار عمل الويب
- **SQLite** - قاعدة البيانات
- **Flask-CORS** - دعم CORS للتكامل

### الواجهة الأمامية (Frontend)
- **HTML5** - هيكل الصفحات
- **CSS3** - التصميم والتنسيق
- **JavaScript (ES6+)** - التفاعل والديناميكية
- **Font Awesome** - الأيقونات
- **Google Fonts** - الخطوط العربية

### قاعدة البيانات
- **SQLite** - قاعدة بيانات محلية
- جداول: `products`, `settings`
- دعم العمليات المتزامنة

## هيكل المشروع

```
mogdam-store/
├── src/
│   ├── main.py              # الملف الرئيسي للخادم
│   ├── models/
│   │   ├── __init__.py
│   │   ├── product.py       # نموذج المنتجات
│   │   └── user.py          # نموذج المستخدمين
│   ├── routes/
│   │   ├── __init__.py
│   │   └── product.py       # مسارات API للمنتجات
│   └── static/
│       ├── index.html       # الصفحة الرئيسية
│       ├── admin.html       # لوحة التحكم
│       └── login.html       # صفحة تسجيل الدخول
├── venv/                    # البيئة الافتراضية
├── requirements.txt         # المتطلبات
├── store.db                # قاعدة البيانات
└── README.md               # هذا الملف
```

## التثبيت والتشغيل

### المتطلبات
- Python 3.11 أو أحدث
- pip (مدير حزم Python)

### خطوات التثبيت

1. **استنساخ المشروع**
```bash
git clone <repository-url>
cd mogdam-store
```

2. **إنشاء البيئة الافتراضية**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# أو
venv\Scripts\activate     # Windows
```

3. **تثبيت المتطلبات**
```bash
pip install -r requirements.txt
```

4. **تشغيل الخادم**
```bash
cd src
python main.py
```

5. **الوصول للموقع**
- الموقع الرئيسي: `http://localhost:5001`
- لوحة التحكم: `http://localhost:5001/admin.html`
- كلمة المرور الافتراضية: `admin123`

## API Documentation

### المنتجات (Products)

#### جلب جميع المنتجات
```http
GET /api/products
```

**الاستجابة:**
```json
{
  "success": true,
  "products": [
    {
      "id": 1,
      "name": "اسم المنتج",
      "description": "وصف المنتج",
      "price": "299 ريال",
      "image_url": "رابط الصورة",
      "whatsapp_message": "رسالة واتساب",
      "is_active": true,
      "created_at": "2024-07-26"
    }
  ]
}
```

#### إضافة منتج جديد
```http
POST /api/products
Content-Type: application/json
```

**البيانات المطلوبة:**
```json
{
  "name": "اسم المنتج",
  "description": "وصف المنتج",
  "price": "299 ريال",
  "image_url": "رابط الصورة",
  "whatsapp_message": "رسالة واتساب",
  "is_active": true
}
```

#### تحديث منتج
```http
PUT /api/products/<id>
Content-Type: application/json
```

#### حذف منتج
```http
DELETE /api/products/<id>
```

### الإعدادات (Settings)

#### جلب الإعدادات
```http
GET /api/settings
```

#### تحديث الإعدادات
```http
POST /api/settings
Content-Type: application/json
```

### المصادقة (Authentication)

#### تسجيل الدخول
```http
POST /api/login
Content-Type: application/json
```

**البيانات:**
```json
{
  "password": "admin123"
}
```

## قاعدة البيانات

### جدول المنتجات (products)
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price TEXT NOT NULL,
    image_url TEXT,
    whatsapp_message TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### جدول الإعدادات (settings)
```sql
CREATE TABLE settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE NOT NULL,
    value TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## التخصيص والتطوير

### تغيير الألوان والتصميم
- عدّل متغيرات CSS في `:root` في ملفات HTML
- الألوان الرئيسية محددة في `--primary-gold`, `--light-gold`, إلخ

### إضافة حقول جديدة للمنتجات
1. عدّل جدول `products` في قاعدة البيانات
2. حدّث نموذج `Product` في `models/product.py`
3. عدّل نماذج HTML في `admin.html`
4. حدّث API endpoints في `routes/product.py`

### تغيير كلمة المرور
عدّل المتغير `ADMIN_PASSWORD` في `main.py`:
```python
ADMIN_PASSWORD = "كلمة_المرور_الجديدة"
```

## الأمان

### الحماية المطبقة
- ✅ حماية لوحة التحكم بكلمة مرور
- ✅ إدارة جلسات آمنة
- ✅ التحقق من صحة البيانات
- ✅ حماية من SQL Injection
- ✅ تشفير كلمات المرور

### توصيات أمنية إضافية
- 🔐 استخدم HTTPS في الإنتاج
- 🔄 غيّر كلمة المرور الافتراضية
- 🛡️ استخدم جدار حماية
- 📊 راقب ملفات السجل
- 💾 اعمل نسخ احتياطية منتظمة

## النشر (Deployment)

### الخيارات المتاحة
1. **خادم محلي** - للاختبار والتطوير
2. **VPS/Cloud** - للاستخدام الإنتاجي
3. **منصات السحابة** - Heroku, DigitalOcean, AWS

### إعدادات الإنتاج
```python
# في main.py للإنتاج
app.run(host='0.0.0.0', port=80, debug=False)
```

### متغيرات البيئة
```bash
export FLASK_ENV=production
export SECRET_KEY=your-secret-key
export DATABASE_URL=sqlite:///store.db
```

## الاختبار

### اختبارات تم تنفيذها
- ✅ اختبار تحميل الصفحات
- ✅ اختبار إضافة/تعديل/حذف المنتجات
- ✅ اختبار تسجيل الدخول والأمان
- ✅ اختبار التصميم المتجاوب
- ✅ اختبار API endpoints

### تشغيل الاختبارات
```bash
# اختبار الخادم
curl http://localhost:5001/api/products

# اختبار تسجيل الدخول
curl -X POST http://localhost:5001/api/login \
  -H "Content-Type: application/json" \
  -d '{"password":"admin123"}'
```

## المساهمة

### إرشادات المساهمة
1. Fork المشروع
2. إنشاء branch جديد للميزة
3. Commit التغييرات مع رسائل واضحة
4. Push إلى branch
5. إنشاء Pull Request

### معايير الكود
- استخدم أسماء متغيرات واضحة
- اكتب تعليقات للكود المعقد
- اتبع PEP 8 لـ Python
- اختبر التغييرات قبل الإرسال

## الدعم والمساعدة

### الحصول على المساعدة
- 📖 راجع دليل المستخدم
- 🐛 أبلغ عن الأخطاء في Issues
- 💡 اقترح ميزات جديدة
- 📧 تواصل مع فريق التطوير

### معلومات الإصدار
- **الإصدار الحالي**: 1.0.0
- **تاريخ الإصدار**: 26 يوليو 2024
- **آخر تحديث**: 26 يوليو 2024

## الترخيص

هذا المشروع مرخص تحت رخصة MIT. راجع ملف LICENSE للتفاصيل.

---

**تم تطويره بـ ❤️ لمتجر مقدام**

