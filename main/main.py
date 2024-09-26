import requests
from flask import Flask, render_template

app = Flask(__name__)

response = requests.get("https://catfact.ninja/fact")
print("status code: " + str(response.status_code))
data = response.json()

print(data)
print(data["length"])


@app.route("/")
def main_page(fact=data):
    return render_template('main.html', randomFact=fact)

@app.route("/history")
def history_page():
    return render_template('history.html')



if __name__ == '__main__':
    app.run()