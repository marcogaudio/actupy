from calculations.set_hypothesis import set_hypothesis
from hypothesis import Hypothesis
from modelpoint import ModelPoint
import pandas as pd
import pytest

def test_set_hypothesis_valid_input():
    model_point_data = pd.DataFrame({'age': [30, 40, 50], 'value': [100, 200, 300]})
    mortality_data = pd.DataFrame({'age': [30, 40, 50], 'mortality_rate': [0.01, 0.02, 0.03]})
    
    model_point = ModelPoint(model_point_data)
    hypothesis = Hypothesis(mortality_data)
    
    updated_model_point = set_hypothesis(model_point, hypothesis)
    
    expected_data = pd.DataFrame({
        'age': [30, 40, 50],
        'value': [100, 200, 300],
        'mortality_rate': [0.01, 0.02, 0.03]
    })
    
    pd.testing.assert_frame_equal(updated_model_point.data, expected_data)

def test_set_hypothesis_invalid_model_point():
    hypothesis = Hypothesis(pd.DataFrame({'age': [30, 40, 50], 'mortality_rate': [0.01, 0.02, 0.03]}))
    
    with pytest.raises(TypeError):
        set_hypothesis("not_a_model_point", hypothesis)

def test_set_hypothesis_invalid_hypothesis():
    model_point = ModelPoint(pd.DataFrame({'age': [30, 40, 50], 'value': [100, 200, 300]}))
    
    with pytest.raises(TypeError):
        set_hypothesis(model_point, "not_a_hypothesis")

def test_set_hypothesis_empty_mortality():
    model_point = ModelPoint(pd.DataFrame({'age': [30, 40, 50], 'value': [100, 200, 300]}))
    hypothesis = Hypothesis(pd.DataFrame(columns=['age', 'mortality_rate']))
    
    with pytest.raises(ValueError):
        set_hypothesis(model_point, hypothesis)

def test_set_hypothesis_missing_age_in_model_point():
    model_point = ModelPoint(pd.DataFrame({'value': [100, 200, 300]}))
    hypothesis = Hypothesis(pd.DataFrame({'age': [30, 40, 50], 'mortality_rate': [0.01, 0.02, 0.03]}))
    
    with pytest.raises(KeyError):
        set_hypothesis(model_point, hypothesis)

def test_set_hypothesis_missing_age_in_hypothesis():
    model_point = ModelPoint(pd.DataFrame({'age': [30, 40, 50], 'value': [100, 200, 300]}))
    hypothesis = Hypothesis(pd.DataFrame({'mortality_rate': [0.01, 0.02, 0.03]}))
    
    with pytest.raises(KeyError):
        set_hypothesis(model_point, hypothesis)


model_point=ModelPoint(age=30, gender='M', premium=1000, sum_insured=50000, duration=10, seniority=5)
hypothesis=Hypothesis(mortality=pd.DataFrame({'age': [30, 40, 50], 'qx': [0.01, 0.02, 0.03]}))

new_mp = set_hypothesis(model_point, hypothesis)
print(new_mp)