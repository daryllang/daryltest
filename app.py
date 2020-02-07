from flask import Flask, render_template
import os
from random import sample

app = Flask(__name__)

chars = '56789ABCDEF'

@app.route("/")
def index():
   color = '#'+''.join(sample(chars,6))
   return render_template("index.html", color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
