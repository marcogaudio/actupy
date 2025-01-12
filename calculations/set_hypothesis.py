import pandas as pd
from modelpoint import ModelPoint   
from hypothesis import Hypothesis

def set_hypothesis(model_point, hypothesis):
    """
    Unisce i dati di un oggetto Hypothesis con un oggetto ModelPoint sulla base delle colonne in comune.
    
    Parameters:
    - model_point (ModelPoint): L'oggetto ModelPoint da aggiornare.
    - hypothesis (Hypothesis): L'oggetto Hypothesis contenente le ipotesi (es. mortalità).

    Returns:
    - ModelPoint: Un nuovo oggetto ModelPoint con le colonne aggiuntive di Hypothesis.

    Raises:
    - TypeError: Se gli input non sono oggetti ModelPoint o Hypothesis.
    - ValueError: Se la tabella di mortalità nell'oggetto Hypothesis è vuota.
    - KeyError: Se la colonna 'age' non è presente in uno dei due oggetti.
    """
    # Controllo dei tipi di input
    if not isinstance(model_point, ModelPoint):
        raise TypeError("Il parametro 'model_point' deve essere un oggetto della classe ModelPoint.")
    if not isinstance(hypothesis, Hypothesis):
        raise TypeError("Il parametro 'hypothesis' deve essere un oggetto della classe Hypothesis.")
    
    # Verifica che la tabella di mortalità non sia vuota
    if hypothesis.mortality.empty:
        raise ValueError("La tabella di mortalità nell'oggetto Hypothesis è vuota.")
    
    # Verifica che l'attributo 'age' sia presente in entrambi gli oggetti
    if 'age' not in model_point.data.columns:
        raise KeyError("La colonna 'age' non è presente nell'oggetto ModelPoint.")
    if 'age' not in hypothesis.mortality.columns:
        raise KeyError("La colonna 'age' non è presente nella tabella di mortalità di Hypothesis.")
    
    # Unisce la tabella di ModelPoint con la tabella di mortalità tramite il merge
    new_data = model_point.data.merge(hypothesis.mortality, on='age', how='left')
    
    # Crea un nuovo oggetto ModelPoint con i dati aggiornati
    updated_model_point = ModelPoint.from_dataframe(new_data)
    #updated_model_point = new_data
    return updated_model_point

