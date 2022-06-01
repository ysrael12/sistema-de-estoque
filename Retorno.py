import pandas as pd

class Retorno:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def LerArquivo(self):
        df = pd.read_csv(self.arquivo)
        return df.to_json()

    def FrangosAbatidos(self):
        df = pd.read_csv(self.arquivo)
        return df.iloc[2, 1]

    def FrangosVendidos(self):
        df = pd.read_csv(self.arquivo)
        return df.iloc[2, 3]

    def PreçoDeRetorno(self):
        df = pd.read_csv(self.arquivo)
        return df.iloc[5, 3]

    def PreçoDoKG(self):
        df = pd.read_csv(self.arquivo)
        return df.iloc[5, 1]

