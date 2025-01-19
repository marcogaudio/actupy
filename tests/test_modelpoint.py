from modelpoint import ModelPoint
from hypothesis import Hypothesis
import pandas as pd
import polars as pl
import pytest
from product import Product

# test colonne mancanti
# test inizializzazione
# Test that the type is changed from pd to pl
def test_type_conversion():
    mp = ModelPoint(pd.DataFrame({
        'age': [30, 40],
        'gender': ['M', 'F'],
        'premium': [1000, 1500],
        'sum_insured': [50000, 60000],
        'duration': [10, 15],
        'qx': [0.01, 0.02],
        'lx': [1000, 2000]
    }))
    assert isinstance(mp.data, pl.DataFrame)

# Test missing columns
def test_missing_columns():
    with pytest.raises(ValueError):
        ModelPoint(pd.DataFrame({
            'age': [30, 40],
            'gender': ['M', 'F'],
            'premium': [1000, 1500]
        }))

# Test initialization
def test_initialization():
    data = pd.DataFrame({
        'age': [30, 40],
        'gender': ['M', 'F'],
        'premium': [1000, 1500],
        'sum_insured': [50000, 60000],
        'duration': [10, 15],
        'qx': [0.01, 0.02],
        'lx': [1000, 2000]
    })
    mp = ModelPoint(data)
    assert mp.data.shape == (2, 7)
    assert isinstance(mp.data, pl.DataFrame)
    assert isinstance(mp, ModelPoint)

# Test set_hypothesis method
def test_set_hypothesis():
    data = pd.DataFrame({
        'age': [30, 40],
        'gender': ['M', 'F'],
        'premium': [1000, 1500],
        'sum_insured': [50000, 60000],
        'duration': [10, 15],
        'qx': [0.01, 0.02],
        'lx': [1000, 2000]
    })
    hypothesis_data = pd.DataFrame({
        'age': [30, 40],
        'qx': [0.005, 0.007]
    })
    hypothesis = Hypothesis(mortality=pl.from_pandas(hypothesis_data))
    mp = ModelPoint(data)
    mp_with_hypothesis = mp.set_hypothesis(hypothesis)
    assert 'qx' in mp_with_hypothesis.data.columns
    assert isinstance(mp_with_hypothesis, ModelPoint)

# Test apply_BE method
def test_apply_BE():
    data = pd.DataFrame({
        'age': [30, 40],
        'gender': ['M', 'F'],
        'premium': [1000, 1500],
        'sum_insured': [50000, 60000],
        'duration': [10, 15],
        'qx': [0.01, 0.02],
        'lx': [1000, 2000]
    })
    mp = ModelPoint(data)
    mp_with_BE = mp.apply_BE(1.1)
    assert 'BE' in mp_with_BE.data.columns
    assert 'BE_qx' in mp_with_BE.data.columns

    # Test apply_BE method with invalid input
    def test_apply_BE_invalid_input():
        data = pd.DataFrame({
            'age': [30, 40],
            'gender': ['M', 'F'],
            'premium': [1000, 1500],
            'sum_insured': [50000, 60000],
            'duration': [10, 15],
            'qx': [0.01, 0.02],
            'lx': [1000, 2000]
        })
        mp = ModelPoint(data)
        with pytest.raises(TypeError):
            mp.apply_BE([1.1, 1.2])

    # Test add_product_features method
    def test_add_product_features():
        data = pd.DataFrame({
            'age': [30, 40],
            'gender': ['M', 'F'],
            'premium': [1000, 1500],
            'sum_insured': [50000, 60000],
            'duration': [10, 15],
            'qx': [0.01, 0.02],
            'lx': [1000, 2000]
        })
        product = Product(
            premium_type='annual',
            loading=0.05,
            pro_rata_net=0.95,
            pro_rata_loading=0.05
        )
        mp = ModelPoint(data)
        mp_with_product = mp.add_product_features(product)
        assert 'premium_type' in mp_with_product.data.columns
        assert 'loading' in mp_with_product.data.columns
        assert 'pro_rata_net' in mp_with_product.data.columns
        assert 'pro_rata_loading' in mp_with_product.data.columns
        assert isinstance(mp_with_product, ModelPoint)

    # Test add_product_features method with invalid input
    def test_add_product_features_invalid_input():
        data = pd.DataFrame({
            'age': [30, 40],
            'gender': ['M', 'F'],
            'premium': [1000, 1500],
            'sum_insured': [50000, 60000],
            'duration': [10, 15],
            'qx': [0.01, 0.02],
            'lx': [1000, 2000]
        })
        mp = ModelPoint(data)
        with pytest.raises(TypeError):
            mp.add_product_features("invalid_product")