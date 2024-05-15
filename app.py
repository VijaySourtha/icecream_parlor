from flask import Flask
from routes.icecreamRoute import blueprint

app = Flask(__name__)



app.register_blueprint(blueprint, url_prefix='/api/icecream')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"