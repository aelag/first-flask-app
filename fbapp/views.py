from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

#if __name__ == "__main__":
#    app.run(debug=True)
@app.route('/result/')
def result():
    return render_template('result.html')
