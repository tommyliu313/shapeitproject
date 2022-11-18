from flask import Flask, request, render_template, url_for
from coding import camera

app = Flask(__name__, template_folder='app/templates',static_folder="app/static")

@app.route('/')
def testing():
    return 'hello world'

@app.route('/index')
def index():
    return render_template('page/index.html')

def generate_frame():
    camera 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/error.html', errorstatus=404),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/error.html', errorstatus=500),500    

if __name__ == "__main__":
    app.run(debug=True)