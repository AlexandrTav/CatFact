from flask import Flask, render_template, request, session, redirect

from json_reader import JsonReader
from history import History


app = Flask(__name__)
reader = JsonReader("https://catfact.ninja/fact", "")
history = History()
app.secret_key = "VerySecretKey123@!#"

response_data = reader.get_response_json()

""" 
Create main page from template
User can login to add his name to history, and can work as a Guest.
Username is saved to the session.
Accepts POST and GET requests. 
POST request is for accepting username.
GET request for all other requests
Cat image width depends on fact length
"""
@app.route("/", methods = ['POST', 'GET'])
def main_page(cat_data = response_data):
    # Create main page from template. Pass data to this page.
    if 'username' in session:
        username = session['username']
    else:
        username = 'Guest'

    if request.method == 'GET':
        cat_data = reader.get_response_json()
        history.addRecord(username + ":" + str(cat_data))
    if request.method == 'POST':
        session['username'] = request.form['txt_username']
        return render_template("main.html", data=cat_data, user=session['username'])

    return render_template('main.html', data=cat_data, user=username)

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