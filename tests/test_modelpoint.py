from modelpoint import ModelPoint
import pandas as pd
import polars as pl
import pytest

# testo che il tipo venga cambiato da pd a pl
mp = ModelPoint(pd.DataFrame
                ({
                    'age': [30, 40],
                    'gender': ['M', 'F'],
                    'premium': [1000, 1500],
                    'sum_insured': [50000, 60000],
                    'duration': [10, 15],
                    #'seniority': [5, 10],
                    'qx': [0.01, 0.02],
                    'lx': [1000, 2000]
                })
)
print(type(mp.data))

# test colonne mancanti
# test inizializzazione

