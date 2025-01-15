import pandas as pd
import polars as pl
class Hypothesis:
    """
    Classe per rappresentare le ipotesi di una polizza (mortalità, lapse, etc.).
    """
    def __init__(self, mortality=None, lapse=None):
        # Mortality: può essere una tabella (pandas, polars, etc..) o un valore costante
        if isinstance(mortality, pd.DataFrame):
            mortality = pl.from_pandas(mortality)
        if isinstance(mortality, pl.DataFrame):
            if not set(["age", "qx"]).issubset(mortality.columns):
                raise ValueError("La tabella di mortalità deve avere le colonne 'age' e 'qx'.")
            self.mortality = mortality
        else:
            self.mortality = mortality  # Può essere un valore costante o None
        
        # Lapse: può essere una tabella o un valore costante
        if isinstance(lapse, pd.DataFrame):
            # Definire le colonne attese, ad esempio per durata, età, antidurata
            # years è l'antidurata, duration è la durata
            expected_columns = {"age", "seniority", "years", "duration", "rx"}
            if not expected_columns.intersection(lapse.columns):
                raise ValueError(f"La tabella di lapse deve avere almeno una di queste colonne: {expected_columns}.")
            self.lapse = lapse
        else:
            self.lapse = lapse  # Può essere un valore costante o None
        
    def __str__(self):
        mortality_str = f"Mortality: {self.mortality}" if not isinstance(self.mortality, pd.DataFrame) else f"\n{self.mortality}"
        lapse_str = f"Lapse: {self.lapse}" if not isinstance(self.lapse, pd.DataFrame) else f"\n{self.lapse}"
        return f"Hypothesis:\n  {mortality_str}\n  {lapse_str}"

    def get_mortality_for_age(self, age):
        """
        Restituisce il valore di mortalità (qx) per una specifica età.
        """
        if isinstance(self.mortality, pd.DataFrame):
            if self.mortality.empty:
                raise ValueError("La tabella di mortalità è vuota.")
            result = self.mortality[self.mortality['age'] == age]
            if result.empty:
                raise ValueError(f"Età {age} non trovata nella tabella di mortalità.")
            return result['qx'].values[0]
        elif isinstance(self.mortality, (int, float)):
            # Se la mortalità è un valore costante, restituirlo direttamente
            return self.mortality
        else:
            raise ValueError("La mortalità non è definita correttamente.")

    def get_lapse_rate(self, age=None, duration=None):
        """
        Restituisce il tasso di lapse in base agli input forniti.
        """
        if isinstance(self.lapse, pd.DataFrame):
            query = pd.Series(True, index=self.lapse.index)  # Filtro iniziale (tutto True)
            if age is not None and 'age' in self.lapse.columns:
                query &= self.lapse['age'] == age
            if duration is not None and 'duration' in self.lapse.columns:
                query &= self.lapse['duration'] == duration
            result = self.lapse[query]
            if result.empty:
                raise ValueError("Nessun tasso di lapse trovato per i criteri forniti.")
            return result['lapse_rate'].values[0]
        elif isinstance(self.lapse, (int, float)):
            # Se il lapse è un valore costante, restituirlo direttamente
            return self.lapse
        else:
            raise ValueError("Il lapse non è definito correttamente.")