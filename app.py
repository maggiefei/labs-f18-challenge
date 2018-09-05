from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/pokemon/<query>', methods=["GET"])
def main(query):
    url = "http://pokeapi.co/api/v2/pokemon/" + query
    response_dict = requests.get(url).json()
    try:
        int(query)
        return render_template("resultsId.html", api_data=response_dict['name'].capitalize(), search=query)
    except ValueError:
        return render_template("resultsName.html", api_data=response_dict, search=query.capitalize())

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
