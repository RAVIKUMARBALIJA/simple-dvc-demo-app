from flask import Flask, render_template, request, jsonify
import os
import yaml
import joblib
import numpy as np
from prediction_service import prediction

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

"""
def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    print(prediction)
    return prediction[0]

def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response":response}
        print(response)
        return response
    except Exception as e:
        print(e)
        error = {"error": "Something went wrong!! Try again"}
        return error
"""
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                #data = dict(request.form).values()
                #print(dict(request.form))
                dict_req = dict(request.form)
                print(dict_req)
                #print(data)
                #data = [list(map(float, data))]
                #response = predict(data)
                response = prediction.form_response(dict_req)
                return render_template("index.html", response=response)

            elif request.json:
                print(request.json)
                response = prediction.api_response(request.json)
                return jsonify(response)

        except Exception as e:
            print(e)
            error_msg = {"error": "Something went wrong!! Try again"}
            print(error_msg)
            error = {"error":e}
            return render_template("404.html", error=error)
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)