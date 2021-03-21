import os
import numpy as np
import pandas as pd
import joblib
import yaml
import json

params_path = "params.yaml"
schema_path = os.path.join("prediction_service","schema_in.json")

class NotInRange(Exception):
    def __init__(self,message = "values entered are not in range"):
        self.message = message
        super().__init__(self.message)
    
class NotInCols(Exception):
    def __init__(self,message = "entered feature is in the feature list"):
        self.message = message
        super().__init__(self.message)
    
def read_params(config_path=params_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config
    

def predict(data):
    config = read_params(params_path);
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data).tolist()[0]
    #return prediction
    try:
        if 3 <= prediction <= 8:
            return prediction
        else:
            raise NotInRange
    except NotInRange:
        return "Unexpected result"

def get_schema(schema_path=schema_path):
    with open(schema_path) as f:
        schema = json.load(f)
    return schema

def validate_input(dict_req):
    def _validate_cols(col):
        schema = get_schema()
        if col not in schema.keys():
            raise NotInCols
        
    def _validate_values(col,val):
        schema = get_schema()
        if not(schema[col]["min"] <= float(dict_req[col]) <= schema[col]["max"]):
            raise NotInRange
    
    for col,values in dict_req.items():
        _validate_cols(col)
        _validate_values(col,values)
    
    return True

def form_response(dict_req):
    if validate_input(dict_req):
        data = dict_req.values()
        data = [list(map(float,data))]
        responsne = predict(data)
        return responsne

def api_response(dict_req):
    try:
        if validate_input(dict_req):
            data = np.array([list(dict_req.values())])
            response = predict(data)
            response = {"response":response}
            return response
    
    except NotInRange as e:
        response = {"the_expected_range":get_schema(),"response": str(e)}
        return response
    
    except NotInCols as e:
        response = {"the_expected_cols":get_schema().keys(),"response" : str(e)}
        return response
    
    except Exception as e:
        response = {"response": str(e)}
        return response
            

    