import pandas as pd 

class Df_Interpreter():
    def __init__(self, filepath):
        self.df = pd.read_excel(filepath)

    def get_DataFrame(self):
        return self.df

    # Umwandlung der Datentypen 
    def typecasting_from_column(self, type, column):
        self.df[column] = self.df[column].astype(type)


    