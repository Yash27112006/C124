from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {
        'id':1,
        'title':'buy groceries',
        'description': 'milk, cheese, pizza',
        'done': False
    },
    {
        'id':2,
        'title': 'homework',
        'description': 'maths, english, physics',
        'done': False
    },
]

@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify(
            {
            "status": 'error',
            "message": "Please provide the data"
            },
            400
        )

    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    tasks.append(task)
    return jsonify(
        {
            "status": 'Success',
            "message": "Task Added Successfully"
        }
    )
    
@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })

if __name__ == "__main__":
    app.run(debug=True)