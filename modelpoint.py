import pandas as pd
import polars as pl
from hypothesis import Hypothesis
from product import Product

class ModelPoint:
    """
    Classe per rappresentare una tabella di model point per un gruppo omogeneo di polizze assicurative.
    """

    def __init__(self, data):
        """
        Inizializza un oggetto ModelPoint con un DataFrame polars.

        :param data: DataFrame contenente i dati dei model point.
        :raises TypeError: Se data non è un DataFrame.
        :raises ValueError: Se mancano colonne richieste nel DataFrame.
        """
        
        # se non è df (pandas o polars), restituisco errore
        if not isinstance(data, (pl.DataFrame, pd.DataFrame)):
            raise TypeError(f"L'input 'data' deve essere un oggetto pandas.DataFrame, non {type(data)}.")
        # se è pandas, trasformo in polars
        if isinstance(data, pd.DataFrame):
            data = pl.from_pandas(data)

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

    ## UPLOAD METHOD
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
    
    # OTHER METHODS

    def set_hypothesis(self, hypothesis):

        # check su tipo Hypothesis
        # inserire come input attr. on
        # forse devo aggiornare data?

        update_data = (
            self.data.
            join(hypothesis.mortality, on = "age", how = "left")
            )
        
        return ModelPoint(update_data)
    
    # in teoria potrei gestire le BE direttamente con polars
    def apply_BE(self, BE_factor):

        if not isinstance(BE_factor, float):
            # per adesso accetto solo un valore numerico
            # potrei aggiungere un parametro per gestire il join con un altro df
            raise ValueError("BE_factor deve essere un singolo valore numerico.")
        
        update_data = (
            self.data
            # non funziona
            .with_columns(BE = BE_factor)
            .with_columns((pl.col("qx") * pl.col("BE")).alias("BE_qx"))
        )


        return ModelPoint(update_data)
    

    def add_product_features(self, product: Product):
        """
        Aggiunge le caratteristiche del prodotto al ModelPoint.

        :param product: Oggetto Product contenente le caratteristiche del prodotto.
        :return: ModelPoint con le caratteristiche del prodotto aggiunte.
        """
        # Check se product è un oggetto Product
        if not isinstance(product, Product):
            raise TypeError(f"product deve essere un oggetto Product, non {type(product)}")
        
        # Aggiungi le colonne del prodotto al DataFrame
        update_data = (
            self.data
            .with_columns(
                premium_type = pl.lit(product.premium_type),
                loading = pl.lit(product.loading),
                pro_rata_net = pl.lit(product.pro_rata_net),
                pro_rata_loading = pl.lit(product.pro_rata_loading)
            )
        )
        
        return ModelPoint(update_data)
