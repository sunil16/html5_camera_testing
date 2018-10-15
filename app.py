from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
   return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.43.66', port=5000)
