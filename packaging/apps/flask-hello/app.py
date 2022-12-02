from flask import Flask
import os

app = Flask(__name__)

argo_env = os.environ.get("ARGO_ENV")
argo_env2 = os.environ.get("ARGO_ENV2")
argo_env3 = os.environ.get("ARGO_ENV3")


@app.route('/')
def hello():
    return f"<h1>Hello, World env {argo_env} env2 {argo_env2} env3 {argo_env3}!</h1>"