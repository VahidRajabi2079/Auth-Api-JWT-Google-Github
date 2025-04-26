# 🚀   Authentication 
> پروژه احراز هویت به قابلیت های ثبت نام، ورود، فعال سازی حساب کاربری،تغییر رمز عبور، تغییر نام کاربری، و قابلیت ورود با حساب گوگل و گیت هاب

## پکیج های استفاده شده
- django 
- djangorestframework 
- djangorestframework-simplejwt 
- djoser 
- mysqlclient 
- social-auth-app-django 
- drf-yasg 
- python-dotenv 
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "djoser",
    "social_django",
    "drf_yasg",
    # Apps
    "core.apps.CoreConfig",
]
```

___
## مراحل راه انداری پروژه
> #### 1️⃣   نصب پکیج ها
 برای نصب پکیج‌ها از فایل Pipfile در پروژه‌ای که از pipenv استفاده می‌کند، می‌توانید از دستور زیر در ترمینال استفاده کنید:
```bash
pipenv install 
```
این دستور تمام پکیج‌هایی که در فایل Pipfile مشخص شده‌اند را نصب خواهد کرد.

برای نصب پکیج‌ها از فایل Pipfile.lock (که نسخه‌های دقیق‌تر پکیج‌ها را ذخیره می‌کند)، از دستور زیر استفاده کنید:
```bash
pipenv install --dev
```

> ### 2️⃣  اکتیو کردن محیط مجازی

```bash
pipenv shell
```
❗  اگر میخوای ببینی که پکیج ها به درستی نصب شدن دستر زیر رو بعد از اکتیو کردن بزن.
```bash
pipenv graph
```
یک نمودار میکشه از پکیج هایی که نصب شده در این محیط که ساختی

> ### 3️⃣ ساخت یک دیتابیس در MYSQL
یک دیتابیس به ساز با هر نامی که خواستی داخل تنظمیات پروژه هست

⚠️ فقط یاد باشه من از فایل .env استفاده کردم
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DJANGO_DB_NAME"),
        "HOST": os.getenv("DJANGO_DB_HOST"),
        "USER": os.getenv("DJANGO_DB_USER"),
        "PASSWORD": os.getenv("DJANGO_DB_PASSWORD"),
    }
}
```

> ### 4️⃣ تنظیمات ایمیل 
```python
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS") == "True"
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
```

> ### 4️⃣ برای ورود با حساب کاربری گوگل و گیت هاب تنظیمات زیر و تنظیم کنید

⚠️ فقط یاد باشه وقتی میخوای از این قایلیت استفاده کنی وقت داخل گوگل و گیت هاب داخل  **OAuth Apps** 
برای هر کدام فرق میکنه
> Google = Authorized redirect URIs
> Github = Authorization callback URL

آدرس های زیر رو دقیقا کپی کن

```python
DJOSER = {",
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
        "http://localhost:8000/auth/o/google-oauth2/",
        "http://localhost:8000/auth/o/github/",
    ], 
}
```
برای تست آدرس زیر رو وارد کد 
[Google](http://localhost:8000/auth/o/google-oauth2/?redirect_uri=http://localhost:8000/auth/o/google-oauth2/, "Google Account") 


[Google](http://localhost:8000/auth/o/github/?redirect_uri=http://localhost:8000/auth/o/github/, "Github Account") 



> ### 4️⃣ Makemigrations and Migrate
```bash
python manage.py makemigrations
python manage.py migrate
```

> ### 5️⃣  اجرای برنامه
```bash
pythin manage.py runserver
```

___
🐍  models ==> CustomUser

```python
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        max_length=255,
    )
    username = models.CharField(
        max_length=50,
        unique=True,
    )
    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=50,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} | {self.email}"
```
___
# Endpoints API

- Swagger UI → [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- ReDoc UI → [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)
 
___
## 👨‍💻 توسعه‌دهنده

تهیه شده با ❤️ توسط **وحید رجبی** برای یادگیری و توسعه پروژه‌های واقعی با Django

---

> 💡 اگر پیشنهادی دارید یا با مشکلی مواجه شدید، خوشحال می‌شوم از طریق ایمیل vahidrajabi.software@gmail.com یا https://www.linkedin.com/in/vahidrajabi2000/ یا در گیت‌هاب در ارتباط باشید.


