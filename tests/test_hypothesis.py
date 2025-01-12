from hypothesis import Hypothesis
import pandas as pd
import pytest

def test_mortality_is_dataframe():
    mortality_table = pd.DataFrame({
        "age": [20, 21, 22, 23, 24, 25],
        "qx": [0.001, 0.0012, 0.0015, 0.0017, 0.002, 0.0022]
    })
    hypothesis = Hypothesis(mortality=mortality_table)
    assert hypothesis.mortality.equals(mortality_table)

def test_mortality_is_dataframe_wrong_attributes():
    mortality_table = pd.DataFrame({
        "current_AGE": [20, 21, 22, 23, 24, 25],
        "prob": [0.001, 0.0012, 0.0015, 0.0017, 0.002, 0.0022]
    })
    with pytest.raises(ValueError):
        Hypothesis(mortality=mortality_table)

def test_mortality_is_integer():
    with pytest.raises(TypeError):
        Hypothesis(mortality=123)

def test_mortality_is_double():
    with pytest.raises(TypeError):
        Hypothesis(mortality=123.456)

def test_mortality_is_none():
    hypothesis = Hypothesis(mortality=None)
    assert hypothesis.mortality.empty

# lapse

def test_lapse_is_dataframe():
    lapse_table = pd.DataFrame({
        "duration": [1, 2, 3, 4, 5, 6],
        "rx": [0.05, 0.04, 0.03, 0.02, 0.01, 0.005]
    })
    hypothesis = Hypothesis(lapse=lapse_table)
    assert hypothesis.lapse.equals(lapse_table)

def test_lapse_is_dataframe_wrong_attributes():
    lapse_table = pd.DataFrame({
        "time": [1, 2, 3, 4, 5, 6],
        "rate": [0.05, 0.04, 0.03, 0.02, 0.01, 0.005]
    })
    with pytest.raises(ValueError):
        Hypothesis(lapse=lapse_table)

def test_lapse_is_integer():
    with pytest.raises(TypeError):
        Hypothesis(lapse=123)

def test_lapse_is_double():
    with pytest.raises(TypeError):
        Hypothesis(lapse=123.456)

def test_lapse_is_none():
    hypothesis = Hypothesis(lapse=None)
    assert hypothesis.lapse.empty