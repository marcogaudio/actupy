import pandas as pd

class ModelPoint:
    """
    Classe per rappresentare un singolo model point per una gruppo omogeneo di polizze assicurative.
    """

    def __init__(self, age, gender, premium, sum_insured, duration, seniority=None):
        """
        Inizializza un ModelPoint con i dati forniti.
        """
        self.age = age
        self.gender = gender
        self.premium = premium
        self.sum_insured = sum_insured
        self.duration = duration
        self.seniority = seniority

    def __str__(self):
        return (
            f"ModelPoint(\n"
            f"  age={self.age},\n"
            f"  gender={self.gender},\n"
            f"  premium={self.premium},\n"
            f"  sum_insured={self.sum_insured},\n"
            f"  duration={self.duration},\n"
            f"  seniority={self.seniority}\n"
            f")"
        )
    
    def __repr__(self):
        return self.__str__()

    @staticmethod
    def from_dataframe(df):
        """
        Metodo statico per creare una lista di ModelPoint a partire da un DataFrame pandas.
        
        :param df: DataFrame contenente i dati di model point
        :return: Lista di oggetti ModelPoint
        """
        # Verifica che le colonne richieste siano presenti
        required_columns = ["age", "gender", "premium", "sum_insured", "duration"]
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Mancano le colonne richieste nel DataFrame: {', '.join(missing_columns)}")

        # Crea la lista di ModelPoint
        model_points = []
        for _, row in df.iterrows():
            model_points.append(ModelPoint(
                age=row["age"],
                gender=row["gender"],
                premium=row["premium"],
                sum_insured=row["sum_insured"],
                duration=row["duration"],
                seniority=row.get("seniority")  # Seniority è opzionale
            ))

        return model_points

    @staticmethod
    def from_excel(file_path, sheet_name=0):
        """
        Metodo statico per creare una lista di ModelPoint a partire da un file Excel.
        
        :param file_path: Percorso al file Excel
        :param sheet_name: Nome o indice del foglio Excel da leggere (default: primo foglio)
        :return: Lista di oggetti ModelPoint
        """
        # Leggi il file Excel in un DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Verifica che le colonne richieste siano presenti
        required_columns = ["age", "gender", "premium", "sum_insured", "duration"]
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Mancano le colonne richieste nel file Excel: {', '.join(missing_columns)}")

        # Crea la lista di ModelPoint
        model_points = []
        for _, row in df.iterrows():
            model_points.append(ModelPoint(
                age=row["age"],
                gender=row["gender"],
                premium=row["premium"],
                sum_insured=row["sum_insured"],
                duration=row["duration"],
                seniority=row.get("seniority")  # Seniority è opzionale
            ))
        
        return model_points