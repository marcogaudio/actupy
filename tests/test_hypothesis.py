from hypothesis import Hypothesis
import pandas as pd
import pytest

def test_mortality_is_integer():
    with pytest.raises(TypeError):
        Hypothesis(mortality=123)

def test_mortality_is_double():
    with pytest.raises(TypeError):
        Hypothesis(mortality=123.456)

def test_mortality_is_none():
    hypothesis = Hypothesis(mortality=None)
    assert hypothesis.mortality.empty



test = Hypothesis(mortality=None, lapse=0.02, loe=0.005, ci=0.0005)
print(test)


""""
# Crea un DataFrame con i valori di mortalità
mortality_table = pd.DataFrame({
    "age": [20, 21, 22, 23, 24, 25],
    "qx": [0.001, 0.0012, 0.0015, 0.0017, 0.002, 0.0022]
})

# Inizializza l'oggetto Hypothesis con la tabella di mortalità
hypothesis = Hypothesis(mortality=mortality_table, lapse=0.02, loe=0.005, ci=0.0005)

# Stampa l'oggetto
print(hypothesis)

# Ottieni il valore di mortalità per un'età specifica
qx_for_age_23 = hypothesis.get_mortality_for_age(23)
print(f"Probabilità di morte all'età di 23 anni: {qx_for_age_23}")
"""