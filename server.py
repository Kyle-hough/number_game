from flask import Flask, render_template, session, request, redirect
app= Flask(__name__)
import random
app.secret_key = 'password'

@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    if request.form['guess'].isnumeric():
        session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)