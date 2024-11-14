from flask import Flask
from blu_printes.email_routes import bp_email
from db import engine, Base

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
def check_db_connection():
    try:
        with engine.connect() as conn:
            print("Connection to database is successful.")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

with app.app_context():
    check_db_connection()

Base.metadata.create_all(bind=engine)

app.register_blueprint(bp_email)


if __name__ == '__main__':
    app.run()
