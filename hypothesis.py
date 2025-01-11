import pandas as pd

class Hypothesis:
    """
    Classe per rappresentare le ipotesi di una polizza (mortalità, lapse, etc.).
    """
    def __init__(self, mortality=None, lapse=0.02, loe=0.005, ci=0.0005):
        # La mortalità è una tabella (ad esempio un DataFrame pandas)
        self.mortality = mortality if mortality is not None else pd.DataFrame(columns=["age", "qx"])
        # commento: potrei avere lapse per età o per durata o per antidurata. come gestirlo?
        self.lapse = lapse if lapse is not None else pd.DataFrame()
        self.loe = loe  # Loss of employment
        self.ci = ci    # Critical Illness

    def __str__(self):
            return (f"Hypothesis:\n"
                    f"  Mortality:\n{self.mortality}\n"
                    f"  Lapse: {self.lapse}\n"
                    f"  Loss of Employment: {self.loe}\n"
                    f"  Critical Illness: {self.ci}")

    def get_mortality_for_age(self, age):
        """
        Restituisce il valore di mortalità (qx) per una specifica età.
        """
        if self.mortality is None or self.mortality.empty:
            raise ValueError("La tabella di mortalità è vuota.")
        result = self.mortality[self.mortality['age'] == age]
        if result.empty:
            raise ValueError(f"Età {age} non trovata nella tabella di mortalità.")
        return result['qx'].values[0]
        