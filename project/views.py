from flask import render_template
from . import app
from . import nouns
import random

@app.route("/")
def root():
  foo = len(nouns.nouns)
  bar = random.sample(nouns.nouns, 3)
  return render_template('index.html',nouns=bar)
