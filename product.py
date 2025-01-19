import pandas as pd
import polars as pl


class Product:

    # creo una classe per definire le caratteristiche del prodotto
    # per ora inserisco solo prodotti a premio unico
    # 1 - Cessione del quinto

    def __init__(self, premium_type, loading, pro_rata_net, pro_rata_loading):
        if premium_type not in ["single", "annual"]:
            raise ValueError("premium_type must be 'single' or 'annual'")
        if pro_rata_net not in ["linear", "rule 78"]:
            raise ValueError("pro_rata_net must be 'linear' or 'rule 78'")
        if pro_rata_loading not in ["linear", "rule 78"]:
            raise ValueError("pro_rata_loading must be 'linear' or 'rule 78'")
        if not isinstance(loading, float):
            raise ValueError("loading must be a float")

        self.premium_type = premium_type
        self.loading = loading
        self.pro_rata_net = pro_rata_net
        self.pro_rata_loading = pro_rata_loading

        def __str__(self):
            return (f"Product(premium_type={self.premium_type}, loading={self.loading}, "
                    f"pro_rata_net={self.pro_rata_net}, pro_rata_loading={self.pro_rata_loading})")

        def __repr__(self):
            return (f"Product(premium_type={self.premium_type!r}, loading={self.loading!r}, "
                    f"pro_rata_net={self.pro_rata_net!r}, pro_rata_loading={self.pro_rata_loading!r})")



