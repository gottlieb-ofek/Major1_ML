import pandas as pd
import numpy as np
import datetime
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


"this function makes features to numerics and extracts features from other features"
class MakeNumericExtractAndDrop:

    def __int__(self, df):
        self.df = df

    "here are the features we convert to numeric / boolean"
    def sex(self):
        self.df['sex'] = self.df['sex'].replace(['M'], 0)
        self.df['sex'] = self.df['sex'].replace(['F'], 1)

    def blood_type(self):
        self.df['A'] = self.df["blood_type"].isin(["A+", "A-"]).apply(lambda x: int(x))
        self.df['A'] = self.df["blood_type"].isin(["A+", "A-"]).apply(lambda x: int(x))
        self.df['B'] = self.df["blood_type"].isin(["B+", "B-", "AB+", "AB-"]).apply(lambda x: int(x))
        self.df['O'] = self.df["blood_type"].isin(["O+", "O-"]).apply(lambda x: int(x))
        self.df = self.df.drop('blood_type', 1)

    def current_location(self):
        self.df["current_location_x"] = self.df["current_location"].apply(lambda x: (x.split(","))[0][2:-1])
        self.df["current_location_y"] = self.df["current_location"].apply(lambda x: (x.split(","))[1][2:-2])
        self.df = self.df.drop('current_location', 1)

    def symptoms(self):
        self.df["low_appetite"] = self.df["symptoms"].str.contains("low_appetite").fillna(value = False).apply(lambda x: int(x))
        self.df["cough"] = self.df["symptoms"].str.contains("cough").fillna(value = False).apply(lambda x: int(x))
        self.df["shortness_of_breath"] = self.df["symptoms"].str.contains("shortness_of_breath").fillna(value = False).apply(lambda x: int(x))
        self.df["fever"] = self.df["symptoms"].str.contains("fever").fillna(value = False).apply(lambda x: int(x))
        self.df["sore_throat"] = self.df["symptoms"].str.contains("sore_throat").fillna(value = False).apply(lambda x: int(x))
        self.df = self.df.drop('symptoms', 1)

    def pcr_date(self):
        self.df["time_stamp_pcr"] = self.df["pcr_date"].apply(lambda x: (datetime.datetime(int(x[0:4]),int(x[5:7]),int(x[8:10]),0,0) - datetime.datetime(1970,1,1)).total_seconds())
        self.df = self.df.drop('pcr_date', 1)

    def stdNormal(self, feature):
        df = self.df[[feature]]
        scaler = StandardScaler()
        scaler.fit(df)
        normalaized = scaler.transform(df)
        self.df[feature] = normalaized

    def minMaxNormal(self, feature):
        df = self.df[[feature]]
        scaler = MinMaxScaler((-1,1))
        scaler.fit(df)
        normalaized = scaler.transform(df)
        self.df[feature] = normalaized

    def normalization(self):
        self.minMaxNormal("num_of_siblings")
        self.stdNormal("weight")
        self.minMaxNormal("age")
        self.minMaxNormal("num_of_siblings")
        self.minMaxNormal("happiness_score")
        self.minMaxNormal("household_income")
        self.minMaxNormal("conversations_per_day")
        self.stdNormal("sugar_levels")
        self.minMaxNormal("sport_activity")
        for i in range(1,10):
            if i != 6:
                self.minMaxNormal("PCR_0"+str(i))
        self.stdNormal("PCR_06")
        self.stdNormal("PCR_10")
        self.minMaxNormal("current_location_x")
        self.minMaxNormal("current_location_y")
        self.minMaxNormal("time_stamp_pcr")



#TODO - main function
def prepare_data(training_data, new_data):


    return
