from hypothesis import Hypothesis
from modelpoint import ModelPoint
from calculations.set_hypothesis import set_hypothesis
import pandas as pd
import polars as pl

# definisco model point in pandas df
data = pl.DataFrame(
    {
        'age': [30, 40],
        'gender': ['M', 'F'],
        'premium': [1000, 1500],
        'sum_insured': [50000, 60000],
        'duration': [10, 15],
        #'seniority': [5, 10],
        'qx': [0.01, 0.02],
        'lx': [1000, 2000]
    }
) 

# inizializzo oggetto ModelPoint
mp = ModelPoint(data)


mortality_data = pl.DataFrame({'age': [30, 40, 50], 'qx': [0.01, 0.02, 0.03]})
hypothesis = Hypothesis(mortality_data)
#print(hypothesis)

#hypothesis.mortality.empty

print(
    (mp.data
     .join(hypothesis.mortality, on = "age", how = "left")
     
    )
)