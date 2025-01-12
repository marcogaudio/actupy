import pandas as pd
from modelpoint import ModelPoint   
from hypothesis import Hypothesis

def set_hypothesis(model_points, hypothesis):
    """
    Unisce i dati di un oggetto Hypothesis con uno o più oggetti ModelPoint sulla base delle colonne in comune.
    
    Parameters:
    - model_points (ModelPoint | list[ModelPoint]): Un oggetto ModelPoint o una lista di oggetti ModelPoint da aggiornare.
    - hypothesis (Hypothesis): L'oggetto Hypothesis contenente le ipotesi (es. mortalità).

    Returns:
    - ModelPoint | list[ModelPoint]: Un oggetto ModelPoint (se l'input è singolo) o una lista di oggetti ModelPoint aggiornati.

    Raises:
    - TypeError: Se gli input non sono della classe corretta.
    - ValueError: Se la tabella di mortalità nell'oggetto Hypothesis è vuota.
    - KeyError: Se la colonna 'age' non è presente in uno degli oggetti.
    """
    # Controllo se l'input è un singolo ModelPoint e lo converto in lista
    is_single_modelpoint = isinstance(model_points, ModelPoint)
    if is_single_modelpoint:
        model_points = [model_points]
    
    # Controllo dei tipi di input
    if not isinstance(model_points, list) or not all(isinstance(mp, ModelPoint) for mp in model_points):
        raise TypeError("Il parametro 'model_points' deve essere un oggetto della classe ModelPoint o una lista di ModelPoint.")
    if not isinstance(hypothesis, Hypothesis):
        raise TypeError("Il parametro 'hypothesis' deve essere un oggetto della classe Hypothesis.")
    
    # Verifica che la tabella di mortalità non sia vuota
    if hypothesis.mortality.empty:
        raise ValueError("La tabella di mortalità nell'oggetto Hypothesis è vuota.")
    
    # Verifica che l'attributo 'age' sia presente nella tabella di mortalità
    if 'age' not in hypothesis.mortality.columns:
        raise KeyError("La colonna 'age' non è presente nella tabella di mortalità di Hypothesis.")
    
    updated_model_points = []
    for model_point in model_points:
        # Verifica che l'attributo 'age' sia presente nel singolo ModelPoint
        if 'age' not in model_point.data.columns:
            raise KeyError("La colonna 'age' non è presente in uno degli oggetti ModelPoint.")
        
        # Unisce la tabella di ModelPoint con la tabella di mortalità tramite il merge
        new_data = model_point.data.merge(hypothesis.mortality, on='age', how='left')
        
        # Crea un nuovo oggetto ModelPoint con i dati aggiornati
        updated_model_point = ModelPoint.from_dataframe(new_data)
        updated_model_points.append(updated_model_point)
    
    # Restituisci un singolo oggetto se l'input originale non era una lista
    if is_single_modelpoint:
        return updated_model_points[0]
    
    return updated_model_points

