#Datapackage
import pandas as pd
import numpy as np

class DataPrepkit:
    def __init__(self, data=None):
        self.data = data
        
    def read_file(self, file_path, fformat):
            if fformat.lower() == "json":
                self.data =pd.read_json(file_path)
            elif fformat.lower() == "excel":
                self.data =pd.read_excel(file_path)
            elif fformat.lower() == "csv":
                self.data =pd.read_csv(file_path)
            else:
                raise Exception("please enter a valid format [csv, excel or json]")
        

    def data_summary(self):
        print("processing the data")
        print("="*20)
        summary = {
        'Mean': self.data.mean(),
        'Mode': self.data.mode().iloc[0],
        'Describe': self.data.describe(),
        'Head': self.data.head(8),
        'Tail': self.data.tail(8),
        'Data types': self.data.dtypes,
        'Missing Values': self.data.isnull().sum(),
        'Unique Values': self.data.nunique()
        }
        for key, value in summary.items():
            print(key)
            print("===============")
            print(value)
            print(" ")
            
    def remove_duplicates(self):
        self.data.drop_duplicates(inplace=True)
    
    def handle_missing_values(data, method):
        df = pd.DataFrame(data)
        if method == 'mean':
            return df.fillna(data.mean())
        elif method == 'median':
            return df.fillna(data.median())
        elif method == 'drop':
            return df.dropna()
        else:
            raise ValueError("this type is not available please choose one of the following[mean, median , mode]")
    
    def encode(self):
        encoded_data = pd.get_dummies(
            self.data, columns=self.data.select_dtypes(include='object').columns)
        self.data = encoded_data
            