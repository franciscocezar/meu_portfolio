from flask import Flask, render_template
#from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'vlksdv0w9g09g4gkmwr,vw-e2///z-0+%#4asld'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
