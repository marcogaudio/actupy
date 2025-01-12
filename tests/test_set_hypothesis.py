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

        def test_set_hypothesis_valid_input_list():
            model_point_data_1 = pd.DataFrame({'age': [30, 40, 50], 'value': [100, 200, 300]})
            model_point_data_2 = pd.DataFrame({'age': [35, 45, 55], 'value': [150, 250, 350]})
            mortality_data = pd.DataFrame({'age': [30, 35, 40, 45, 50, 55], 'mortality_rate': [0.01, 0.015, 0.02, 0.025, 0.03, 0.035]})
            
            model_point_1 = ModelPoint(model_point_data_1)
            model_point_2 = ModelPoint(model_point_data_2)
            hypothesis = Hypothesis(mortality_data)
            
            updated_model_points = set_hypothesis([model_point_1, model_point_2], hypothesis)
            
            expected_data_1 = pd.DataFrame({
                'age': [30, 40, 50],
                'value': [100, 200, 300],
                'mortality_rate': [0.01, 0.02, 0.03]
            })
            
            expected_data_2 = pd.DataFrame({
                'age': [35, 45, 55],
                'value': [150, 250, 350],
                'mortality_rate': [0.015, 0.025, 0.035]
            })
            
            pd.testing.assert_frame_equal(updated_model_points[0].data, expected_data_1)
            pd.testing.assert_frame_equal(updated_model_points[1].data, expected_data_2)

        def test_set_hypothesis_invalid_model_point_list():
            hypothesis = Hypothesis(pd.DataFrame({'age': [30, 40, 50], 'mortality_rate': [0.01, 0.02, 0.03]}))
            
            with pytest.raises(TypeError):
                set_hypothesis(["not_a_model_point"], hypothesis)

        def test_set_hypothesis_empty_model_point_list():
            hypothesis = Hypothesis(pd.DataFrame({'age': [30, 40, 50], 'mortality_rate': [0.01, 0.02, 0.03]}))
            
            with pytest.raises(TypeError):
                set_hypothesis([], hypothesis)

        def test_set_hypothesis_missing_age_in_model_point_list():
            model_point_data_1 = pd.DataFrame({'value': [100, 200, 300]})
            model_point_data_2 = pd.DataFrame({'age': [35, 45, 55], 'value': [150, 250, 350]})
            mortality_data = pd.DataFrame({'age': [30, 35, 40, 45, 50, 55], 'mortality_rate': [0.01, 0.015, 0.02, 0.025, 0.03, 0.035]})
            
            model_point_1 = ModelPoint(model_point_data_1)
            model_point_2 = ModelPoint(model_point_data_2)
            hypothesis = Hypothesis(mortality_data)
            
            with pytest.raises(KeyError):
                set_hypothesis([model_point_1, model_point_2], hypothesis)