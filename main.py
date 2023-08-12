from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = "Lyrics Go Here"

    if request.method == 'POST':
        try:
            response = requests.get("https://taylorswiftapi.onrender.com/get")
            response.raise_for_status()
            data = response.json()
            quote = data["quote"]
        except requests.exceptions.RequestException as e:
            quote = "Error fetching quote."

    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
