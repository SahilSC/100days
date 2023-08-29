from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    print(request.form.get('username'))
    print(request.form.get('password'))
    return 'Form submitted successfully'
if __name__=='__main__':
    app.run(debug=True)