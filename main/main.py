from flask import Flask, render_template, request, session, redirect

from json_reader import JsonReader
from history import History


app = Flask(__name__)
reader = JsonReader
#f"http://api.weatherapi.com/v1/current.json?key&q=Brno"
api_key = "68870090a3624a80ba2104715242309"
base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Moscow"


reader = JsonReader(base_url, api_key)

history = History()
app.secret_key = "VerySecretKey123@!#"

response_data = reader.get_response_json()

#temperature = data.current.temp_c

@app.route("/", methods = ['POST', 'GET'])
def main_page(weather_data = response_data):
    # Create main page from template. Pass data to this page.
    if 'city' in session:
        city = session['city']
    else:
        city = 'Moscow'

    if request.method == 'GET':
        weather_data = reader.cityWeather(city)
        history.addRecord(city + ":" + str(weather_data))

    if request.method == 'POST':
        city = request.form['txt_city']
        session['city'] = city
        weather_data = reader.cityWeather(city)


    return render_template('main.html', data=weather_data, Wcity=city)

"""
Page shows history of main page usage. Reads this data from the file.
"""
@app.route("/history")
def history_page(history_data=None):
    if request.method == 'GET':
        history_data = history.getHistory()
    return render_template('history.html', data=history_data)

"""
Removes username from the session and returns 'Guest' instead. Then redirects to main page
"""
@app.route("/logout")
def logout():
    session.pop('username', 'Guest')
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)