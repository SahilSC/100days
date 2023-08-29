from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('index.html')
@app.route('/contactinfo.html')
def contactwebpage():
    return render_template('contactinfo.html')

@app.route('/hobbies.html')
def hobbies():
    return render_template('hobbies.html')

if __name__=='__main__':
    app.run(debug=True)