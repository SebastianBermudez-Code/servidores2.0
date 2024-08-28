from flask import Flask, url_for, render_template

servidor2 = Flask(__name__)

@servidor2.route('/inicio')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    servidor2.run(debug=True)