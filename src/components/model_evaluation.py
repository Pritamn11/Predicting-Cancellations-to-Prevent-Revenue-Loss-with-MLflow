import os 
import pandas as pd 
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score 
from urllib.parse import urlparse 
import mlflow 
import mlflow.sklearn 
import joblib
from src.utils.common import *
from src.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config=ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred) 
        r2 = r2_score(actual, pred) 
        return rmse, mae, r2 
    
    def log_into_mlflow(self):
        print('Engineering features...')
        test_data = np.load(self.config.test_data_path)

        print('Loading model...')
        model = joblib.load(self.config.model_path) 

        X_test = test_data[:,:-1]
        y_test = test_data[:, -1]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # mlflow
        with mlflow.start_run() as run:
            y_pred = model.predict(X_test)

            (rmse, mae, r2) = self.eval_metrics(y_test, y_pred)

            # savings metrics as local 
            scores = {"rmse": rmse, "mae": mae, "r2":r2}
            save_json(path_tosave=Path(self.config.metric_file_name), data=scores)

            # Log parameters and metrics using the MLflow APIs
            mlflow.log_params(self.config.all_params)


            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

                # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                # https://mlflow.org/docs/1.24.0/tutorials-and-examples/tutorial.html
                mlflow.sklearn.log_model(model, "model", registered_model_name="RandomForestClassifier")
            else:
                mlflow.sklearn.log_model(model, "model")

