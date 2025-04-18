import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import find_product, add_product_to_cart, cart


def test_find_product_valid():
    product = find_product(1)
    assert product is not None
    assert product['name'] == 'Telefon'

def test_find_product_invalid():
    product = find_product(99)
    assert product is None

def test_add_product_to_cart_valid():
    cart.clear()  
    success = add_product_to_cart(2)
    assert success is True
    assert len(cart) == 1
    assert cart[0]['name'] == 'Laptop'

def test_add_product_to_cart_invalid():
    cart.clear()
    success = add_product_to_cart(999)
    assert success is False
    assert len(cart) == 0
