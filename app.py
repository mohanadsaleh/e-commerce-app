from flask import Flask, render_template, request

app = Flask(__name__)

# المنتجات المتاحة
products = [
    {'id': 1, 'name': 'Telefon', 'price': 1000},
    {'id': 2, 'name': 'Laptop', 'price': 5000}
]

# السلة (متغير عام لتجميع المنتجات المضافة)
cart = []

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    if add_product_to_cart(product_id):
        product = find_product(product_id)
        return f"{product['name']} sepete eklendi!"
    return "Ürün bulunamadı."

# المسار الجديد لاستقبال Webhook من GitHub
@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    data = request.get_json()
    print(f"Received data: {data}")  # هنا يمكنك إضافة منطق لمعالجة البيانات إذا أردت
    return '', 200  # استجابة إيجابية (رمز 200)

def find_product(product_id):
    return next((p for p in products if p['id'] == product_id), None)

def add_product_to_cart(product_id):
    product = find_product(product_id)
    if product:
        cart.append(product)
        return True
    return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
