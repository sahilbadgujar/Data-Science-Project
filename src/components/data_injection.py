''' In this components we will create a code which will able to read
 the data from any datasource 
 We also here divide data into training and testing purpose
 '''

import os 
import sys
from src.exception_handling import CustomException
from src.login import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


# inside a class to define class variable you have to use __init__ but with decorator class which is here @dataclass
#you can directly define the varaiable

@dataclass
class DataInjectionConfig:
    # when we train or test or raw data some data and if we want to see that data we can save it in a special folder that is done below
    train_data_path: str=os.path.join('artifact',"train.csv")
    test_data_path: str=os.path.join('artifact',"test.csv")
    raw_data_path: str=os.path.join('artifact',"data.csv")

class DataInjection:
    def __init__(self):
        self.injection_config = DataInjectionConfig()

    def initiate_data_injection(self):
        logging.info("Entered the data injection or component")
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the Dataset as dataframe")

            os.makedirs(os.path.dirname(self.injection_config.train_data_path),exist_ok=True) # it saves the file to desired path 

            df.to_csv(self.injection_config.raw_data_path,index=False,header=True) # save the raw data to this path

            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state = 24)
            train_set.to_csv(self.injection_config.train_data_path,index=False,header=True) # save the train data to this path
            test_set.to_csv(self.injection_config.test_data_path,index=False,header=True)  # save the test data to this path

            logging.info("Injection of data is completed")

            return{
                self.injection_config.train_data_path,
                self.injection_config.test_data_path
            }


        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj=DataInjection()
    train_data, test_data = obj.initiate_data_injection()

    data_tranformation = DataTransformation()
    data_tranformation.initiate_data_transformation(train_data, test_data)