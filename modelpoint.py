import pandas as pd
import polars as pl
class ModelPoint:
    """
    Classe per rappresentare una tabella di model point per un gruppo omogeneo di polizze assicurative.
    """

    def __init__(self, data):
        """
        Inizializza un oggetto ModelPoint con un DataFrame pandas.

        :param data: DataFrame contenente i dati dei model point.
        :raises TypeError: Se data non è un DataFrame.
        :raises ValueError: Se mancano colonne richieste nel DataFrame.
        """
        if not isinstance(data, (pl.DataFrame, pd.DataFrame)):
            raise TypeError(f"L'input 'data' deve essere un oggetto pandas.DataFrame, non {type(data)}.")

        # Colonne richieste
        self.required_columns = ["age", "gender", "premium", "sum_insured", "duration"]
        missing_columns = [col for col in self.required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Mancano le colonne richieste nel DataFrame: {', '.join(missing_columns)}")

        # Imposta il DataFrame come attributo della classe
        self.data = data

    def __str__(self):
        return f"ModelPoint con {len(self.data)} record:\n{self.data}"

    def __repr__(self):
        return self.__str__()

    def to_dataframe(self):
        """
        Restituisce i dati del ModelPoint come un DataFrame pandas.
        """
        return self.data

    @classmethod
    def from_excel(cls, file_path, sheet_name=0):
        """
        Metodo di classe per creare un oggetto ModelPoint a partire da un file Excel.

        :param file_path: Percorso al file Excel.
        :param sheet_name: Nome o indice del foglio Excel da leggere (default: primo foglio).
        :return: Oggetto ModelPoint.
        """
        # Leggi il file Excel in un DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return cls(df)

    @staticmethod
    def validate_dataframe(df: pd.DataFrame, required_columns: list):
        """
        Valida che un DataFrame contenga le colonne richieste.

        :param df: DataFrame da validare.
        :param required_columns: Lista di colonne richieste.
        :raises ValueError: Se mancano colonne richieste.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f"L'input deve essere un oggetto pandas.DataFrame, non {type(df)}.")
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Mancano le colonne richieste nel DataFrame: {', '.join(missing_columns)}")