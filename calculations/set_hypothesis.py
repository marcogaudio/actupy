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
    # Controllo dei tipi di input
    if not isinstance(model_points, ModelPoint):
        raise TypeError("Il parametro 'model_points' deve essere un oggetto della classe ModelPoint")
    if not isinstance(hypothesis, Hypothesis):
        raise TypeError("Il parametro 'hypothesis' deve essere un oggetto della classe Hypothesis.")
    
    # Verifica che la tabella di mortalità non sia vuota
    #if hypothesis.mortality.empty:
    #    raise ValueError("La tabella di mortalità nell'oggetto Hypothesis è vuota.")
    #if model_points.data.empty:
    #    raise ValueError("La tabella model point nell'oggetto ModelPoint è vuota.")

        # Unisce la tabella di ModelPoint con la tabella di mortalità tramite il merge
    updated_model_points = model_points.data.merge(hypothesis.mortality, on='age', how='left')
        
        # Crea un nuovo oggetto ModelPoint con i dati aggiornati
    
    return updated_model_points

