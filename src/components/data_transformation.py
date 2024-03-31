import os
import sys
from src.utils.logger import logging
from src.utils.exception import CustomException
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import  train_test_split
import pandas as pd
import numpy as np
from src.entity.config_entity import DataTransformationConfig
 

class DataTransformation:
    def __init__(self, config=DataTransformationConfig):
        self.config = config 
    
    
    def save_preprocessing_data(self):
        try:
            df = pd.read_csv(self.config.data_path)
            df["booking status"] = df["booking status"].apply(lambda x : 1 if x=='Not_Canceled' else 0) 

            df = df[~df["date of reservation"].str.contains("-")]

            df["date of reservation"] = pd.to_datetime(df["date of reservation"])
            df["month"] = df["date of reservation"].dt.month

            df.drop(['Booking_ID','date of reservation'], axis=1, inplace=True)

            df.to_csv(self.config.preprocessing_data, index=False, header=True)
            logging.info("Saving pre processing data")

            return "Preprocessing data saved successfully"

        except Exception as e:
            logging.info("Error occured in saving preprocess data")
            raise CustomException(e,sys)
        


    def get_data_transformer_object(self):
        try:
            self.save_preprocessing_data()

            df = pd.read_csv(self.config.preprocessing_data)
            X = df.drop('booking status',axis=1)
            y = df['booking status']

            num_feature = X.select_dtypes(exclude="object").columns 
            cat_feature = X.select_dtypes(include="object").columns

            numeric_transformer = StandardScaler()
            oh_transformer = OneHotEncoder()

            data_transformer = ColumnTransformer(
                [
                    ("OneHotEncoder", oh_transformer, cat_feature),
                    ("StandardScaler", numeric_transformer, num_feature),        
                ]
            )
            
            preprocessor = Pipeline(steps=[("data_transformer", data_transformer)])

            return preprocessor

        except Exception as e:
            logging.info(f"Error in creating data transformation object: {e}")
            raise CustomException(e,sys)
        


    def train_test_split(self):
        try:
            df = pd.read_csv(self.config.preprocessing_data)
            logging.info("Reading dataset as dataframe")

            logging.info("Initiate splitting dataset as train & test set")
            train_set, test_set = train_test_split(df)

            train_set.to_csv(
                os.path.join(self.config.root_dir,"train.csv"), index=False
            )

            test_set.to_csv(
                os.path.join(self.config.root_dir,"test.csv"), index=False
            )

            logging.info("Dataset splitted into train and test set")
            logging.info(f"{train_set.shape}")
            logging.info(f"{test_set.shape}")

            return (
                self.config.train,
                self.config.test
            )
        
        except Exception as e:
            logging.info("Error in splitting train and test set")
            raise CustomException(e,sys)


    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_set = pd.read_csv(train_path)
            test_set = pd.read_csv(test_path)
            logging.info("Reading train and test dataset completed")

            logging.info("Obtaining preprocessor object")

            preprocessor_obj =  self.get_data_transformer_object() 

            target_feature = "booking status"
            
            independent_feature = list(['number of adults', 'number of children', 'number of weekend nights',
            'number of week nights', 'type of meal', 'car parking space',
            'room type', 'lead time', 'market segment type', 'repeated', 'P-C',
            'P-not-C', 'average price', 'special requests', 'month'])
            
            logging.info("Dropping target feature from train and test dataframe")
            input_train_df = train_set.drop(columns=[target_feature], axis=1)
            target_train_df = train_set[target_feature]

            input_test_df = test_set.drop(columns=[target_feature], axis=1)
            target_test_df = test_set[target_feature]

            logging.info("Applying preprocessor object on training and test dataframe")
            
            train_df = preprocessor_obj.fit_transform(input_train_df)
            test_df = preprocessor_obj.transform(input_test_df)
            
            logging.info("Successfully applied preprocessor object on train and test data")

            train_arr = np.c_[train_df, np.array(target_train_df)]
            test_arr = np.c_[test_df, np.array(target_test_df)]
            logging.info("Returning train and test array")
            
            logging.info("Saving train and test set in numpy file")
            np.save(os.path.join(self.config.root_dir,"train_arr.npy"), train_arr)
            np.save(os.path.join(self.config.root_dir,"test_arr.npy"), test_arr)

            return (
                train_arr,
                test_arr
            )

        except Exception as e:
            logging.info("Error occured in data transformation")
            raise CustomException(e,sys)
