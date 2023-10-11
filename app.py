from flask import (Flask, redirect, session, render_template, request, send_from_directory, url_for)
import os

#from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
#app.config.from_object('config.DevelopmentConfig')
#db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')
            
with app.app_context():
      pass
    #db.create_all()
    #testeando()

if __name__ == '__main__':
	app.run()
