from sklearn.metrics import accuracy_score,f1_score,mean_squared_error,mean_absolute_error,r2_score
import os
from sklearn.linear_model import LogisticRegression,ElasticNet
from sklearn.model_selection import train_test_split
from get_data import read_params
import argparse
import joblib
import json
import sys
import pandas as pd
import pickle
import numpy as np
import json


def eval_metrics(actual,predicted):
    rmse = np.sqrt(mean_squared_error(actual,predicted))
    mae = mean_absolute_error(actual,predicted)
    r2= r2_score(actual,predicted)
    return rmse,mae,r2

def train_and_eval(config_path):
    config= read_params(config_path)
    train_set_path = config["split_data"]["train_path"]
    test_set_path = config["split_data"]["test_path"]
    model_dir=config["model_dir"]
    random_state_1 = config["base"]["random_state"]

    alpha_1 = config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio_1 = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]

    target = config["base"]["target_col"]

    train_set = pd.read_csv(train_set_path,sep=",")
    test_set = pd.read_csv(test_set_path,sep=",")

    x_cols = [col for col in train_set.columns if col != target]
    train_y=train_set[target]
    test_y=test_set[target]

    train_x=train_set[x_cols]
    test_x=test_set[x_cols]

    lr = ElasticNet(alpha=alpha_1,l1_ratio=l1_ratio_1,random_state=random_state_1)
    lr.fit(train_x, train_y)

    predicted_qualities = lr.predict(test_x)

    (rmse,mae,r2) = eval_metrics(test_y,predicted_qualities)

    print("Elastic model metrics")
    print(f"rmse : {rmse}")
    print(f"MAE : {mae}")
    print(f"r2 score : {r2}")

    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    with open(scores_file,"w") as f1:
        scores ={
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        }
        json.dump(scores,f1,indent=4)
    
    with open(params_file,"w") as f2:
        params={
            "alpha": alpha_1,
            "l1_ratio": l1_ratio_1
        }
        json.dump(params,f2,indent=4)
    
    os.makedirs(model_dir,exist_ok=True)
    #with os.path.join(model_dir,"elasticnet.pkl") as f:
    #    pickle.dump(lr,f)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(lr, model_path)


if __name__ ==  "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default='params.yaml')
    parsed_args = args.parse_args()
    train_and_eval(config_path=parsed_args.config)