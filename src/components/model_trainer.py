import pandas as pd
import numpy as np
import os
from src.utils.logger import logging
from sklearn.ensemble import RandomForestClassifier
import joblib
from src.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = np.load(self.config.train_data_path)
        test_data = np.load(self.config.test_data_path)

        logging.info("Train and Test data loaded successfully")
        logging.info("Separate features (X) and target variable (y)")
        X_train = train_data[:, :-1]
        y_train = train_data[:, -1]

        X_test = test_data[:, :-1]
        y_test = test_data[:, -1]

        rfc = RandomForestClassifier(n_estimators=self.config.n_estimators, random_state=self.config.random_state)
        rfc.fit(X_train, y_train)
        logging.info("Trained the model on training dataset")

        joblib.dump(rfc, os.path.join(self.config.root_dir, self.config.model_name))
        logging.info("Model saved to file using joblib")
