from flask import Flask
from blu_printes.email_routes import bp_email
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


app.register_blueprint(bp_email)


if __name__ == '__main__':
    app.run()
