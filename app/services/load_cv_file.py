import json

def load_cv_file(file_path: str):
    with open(file_path) as f:
        cv = json.load(f)
    return cv
