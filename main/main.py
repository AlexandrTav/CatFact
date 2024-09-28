from flask import Flask, render_template, request

from json_reader import JsonReader

app = Flask(__name__)
reader = JsonReader("https://catfact.ninja/fact", "")

response_data = reader.get_response_json()

@app.route("/", methods = ['POST', 'GET'])
def main_page(response_data = response_data):
    if request.method == 'GET':
        response_data = reader.get_response_json()
    return render_template('main.html', data=response_data)

@app.route("/history")
def history_page():
    return render_template('history.html')



if __name__ == '__main__':
    app.run(debug=True)