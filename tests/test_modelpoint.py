from modelpoint import ModelPoint
import pandas as pd
import pytest

def test_modelpoint_initialization():
    mp = ModelPoint(age=30, gender='M', premium=1000, sum_insured=50000, duration=10, seniority=5)
    assert mp.age == 30
    assert mp.gender == 'M'
    assert mp.premium == 1000
    assert mp.sum_insured == 50000
    assert mp.duration == 10
    assert mp.seniority == 5

def test_modelpoint_str():
    mp = ModelPoint(age=30, gender='M', premium=1000, sum_insured=50000, duration=10, seniority=5)
    assert str(mp) == "ModelPoint(age=30, gender=M, premium=1000, sum_insured=50000, duration=10, seniority=5)"

def test_modelpoint_from_dataframe():
    data = {
        'age': [30, 40],
        'gender': ['M', 'F'],
        'premium': [1000, 1500],
        'sum_insured': [50000, 60000],
        'duration': [10, 15],
        'seniority': [5, 10]
    }
    df = pd.DataFrame(data)
    model_points = ModelPoint.from_dataframe(df)
    assert len(model_points) == 2
    assert model_points[0].age == 30
    assert model_points[0].gender == 'M'
    assert model_points[0].premium == 1000
    assert model_points[0].sum_insured == 50000
    assert model_points[0].duration == 10
    assert model_points[0].seniority == 5
    assert model_points[1].age == 40
    assert model_points[1].gender == 'F'
    assert model_points[1].premium == 1500
    assert model_points[1].sum_insured == 60000
    assert model_points[1].duration == 15
    assert model_points[1].seniority == 10

def test_modelpoint_from_dataframe_missing_columns():
    data = {
        'age': [30, 40],
        'gender': ['M', 'F'],
        'premium': [1000, 1500],
        'sum_insured': [50000, 60000]
        # 'duration' column is missing
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Mancano le colonne richieste nel DataFrame: duration"):
        ModelPoint.from_dataframe(df)