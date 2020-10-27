from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
   return render_template('s9private.html', name="Seja bem vindo!")
