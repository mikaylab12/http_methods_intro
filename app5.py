from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def log():
    dict_items = {'Godwin':47, 'Karabo': 22, 'Thabo':17, 'Malik':30, 'Zaid':19}
    # return jsonify(dict_items)
    return render_template('login1.html', dict_items=dict_items)


@app.route('/login', methods=['POST'])
def login():
    uname = request.form['username']
    passwrd = request.form['userpass']
    if uname == "mikayla" and passwrd == "1234":
        return "Welcome %s" % uname + request.method
    else:
        return "Error in logging in " + request.method


if __name__ == '__main__':
    app.run(debug=True)
