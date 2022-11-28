import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


"this function makes features to numerics and extracts features from other features"
class MakeNumericExtractAndDrop:

    def __int__(self, df):
        self.df = df

    "here are the features we convert to numeric / boolean"
    def sex(self):
        #TODO - make bool

    def blood_type(self):
        self.df['A'] = self.df["blood_type"].isin(["A+", "A-"]).apply(lambda x: int(x))
        self.df['A'] = self.df["blood_type"].isin(["A+", "A-"]).apply(lambda x: int(x))
        self.df['B'] = self.df["blood_type"].isin(["B+", "B-", "AB+", "AB-"]).apply(lambda x: int(x))
        self.df['O'] = self.df["blood_type"].isin(["O+", "O-"]).apply(lambda x: int(x))
        self.df.drop('blood_type', 1)

    def current_location(self):
        self.df["current_location_x"] = self.df["current_location"].apply(lambda x: (x.split(","))[0][2:-1])
        self.df["current_location_y"] = self.df["current_location"].apply(lambda x: (x.split(","))[1][2:-2])
        self.df.drop('current_location', 1)

    def symptoms(self):
        self.df["low_appetite"] = self.df["symptoms"].str.contains("low_appetite").fillna(value = False).apply(lambda x: int(x))
        self.df["cough"] = self.df["symptoms"].str.contains("cough").fillna(value = False).apply(lambda x: int(x))
        self.df["shortness_of_breath"] = self.df["symptoms"].str.contains("shortness_of_breath").fillna(value = False).apply(lambda x: int(x))
        self.df["fever"] = self.df["symptoms"].str.contains("fever").fillna(value = False).apply(lambda x: int(x))
        self.df["sore_throat"] = self.df["symptoms"].str.contains("sore_throat").fillna(value = False).apply(lambda x: int(x))
        self.df.drop('symptoms', 1)

    def pcr_date(self):










#TODO - main function
def prepare_data(training_data, new_data):


    return
