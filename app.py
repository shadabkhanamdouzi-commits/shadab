from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# Example fake news headlines
news_data = [
    "Aliens spotted in New York!",
    "Scientists discover chocolate cures all diseases!",
    "Man claims to have time-traveled to 2050!",
    "Cats take over local government!"
]

@app.route('/', methods=['GET', 'POST'])
def home():
    headline = ""
    if request.method == 'POST':
        # Randomly pick a news headline
        headline = random.choice(news_data)
    return render_template('index.html', headline=headline)

if __name__ == "__main__":
    app.run(debug=True)
