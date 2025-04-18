# استخدام صورة Python خفيفة
FROM python:3.9-slim

# تثبيت Rust و Cargo وأدوات البناء المطلوبة
RUN apt-get update && apt-get install -y \
    rustc \
    cargo \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملف المتطلبات أولاً (لاستفادة من الكاش)
COPY requirements.txt .

# تثبيت المتطلبات
RUN pip install --upgrade pip && pip install -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# فتح المنفذ
EXPOSE 5000

# الأمر الافتراضي لتشغيل التطبيق باستخدام gunicorn (وضع الإنتاج)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
