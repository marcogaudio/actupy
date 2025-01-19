import pytest
from product import Product

def test_product_initialization():
    product = Product("single", 0.1, "linear", "linear")
    assert product.premium_type == "single"
    assert product.loading == 0.1
    assert product.pro_rata_net == "linear"
    assert product.pro_rata_loading == "linear"

def test_invalid_premium_type():
    with pytest.raises(ValueError, match="premium_type must be 'single' or 'annual'"):
        Product("monthly", 0.1, "linear", "linear")

def test_invalid_pro_rata_net():
    with pytest.raises(ValueError, match="pro_rata_net must be 'linear' or 'rule 78'"):
        Product("single", 0.1, "non-linear", "linear")

def test_invalid_pro_rata_loading():
    with pytest.raises(ValueError, match="pro_rata_loading must be 'linear' or 'rule 78'"):
        Product("single", 0.1, "linear", "non-linear")

def test_invalid_loading_type():
    with pytest.raises(ValueError, match="loading must be a float"):
        Product("single", "0.1", "linear", "linear")

def test_product_str():
    product = Product("single", 0.1, "linear", "linear")
    assert str(product) == "Product(premium_type=single, loading=0.1, pro_rata_net=linear, pro_rata_loading=linear)"

def test_product_repr():
    product = Product("single", 0.1, "linear", "linear")
    assert repr(product) == "Product(premium_type='single', loading=0.1, pro_rata_net='linear', pro_rata_loading='linear')"