import pytest
import yaml
import os
import json

params_path = "params.yaml"

@pytest.fixture
def config(config_path=params_path):
    with open(params_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
        return config
    
@pytest.fixture
def schema_in(schema_path="schema_in.json"):
    with open(schema_path) as f:
        schema = json.load(f)
        return schema