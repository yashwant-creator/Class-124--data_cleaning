from flask import Flask,jsonify, request

app = Flask(__name__)
#creatig an array of tasks with each task with each task in it 
tasks = [
    {
        'id': 1,
        'name': "9790933484",
        'contact': "person 1", 
        'done': False
    },
    {
        'id': 2,
        'name': "9790975825",
        'contact': "person 2", 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)