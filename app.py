from flask import Flask, request, render_template, url_for, jsonify

app = Flask(__name__, template_folder='app/templates',static_folder="app/static")

@app.route('/')
def testing():
    return 'hello world'

@app.route('/index')
def index():
    return render_template('page/index.html')

@app.route('/simple')
def simple():
    return jsonify(message = 'Hello from the Planetary API.')

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message = "Sorry" + name + ", you are not old enough.")
    else:
        return jsonify(message="Welcome "+ name + ", you are old enough!")



@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/error.html', errorstatus=404),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/error.html', errorstatus=500),500    

if __name__ == "__main__":
    app.run(debug=True)