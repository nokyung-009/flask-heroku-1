from flask import Flask, jsonify

app = Flask(_name_)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

if _name_ == "_main_":
    app.run(debug=False)
