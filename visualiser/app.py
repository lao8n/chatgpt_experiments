from flask import Flask, jsonify, render_template
import random
import json
import math

app = Flask(__name__)

# This should be fetched from a database in a real application
with open('data.json', 'r') as f:
    data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')


def generate_clusters():
    types = {item['type'] for item in data}
    num_items = len(types)
    num_cols = math.ceil(math.sqrt(num_items))
    num_rows = math.ceil(num_items / num_cols)
    print(types, "num cols", num_cols, "num rows", num_rows)
    buffer = 0.1
    cell_size = min(1 - 2 * buffer, 1 / max(num_rows, num_cols))
    cluster_points = {}

    for i, t in enumerate(types):
        row_index = i // num_cols
        col_index = i % num_cols
        print(row_index, col_index)
        x = buffer + col_index * cell_size + cell_size / 2
        y = buffer + row_index * cell_size + cell_size / 2
        cluster_points[t] = (x, y)
    return cluster_points

cluster_points = generate_clusters()
    
@app.route('/framework-data')
def get_framework_data():
    data_with_positions = []
    for framework in data:
        translation = (random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2))
        position = (cluster_points[framework['type']][0] + translation[0], cluster_points[framework['type']][1] + translation[1])
        data_with_positions.append({**framework, 'x': position[0], 'y': position[1]})
    return jsonify(data_with_positions)

@app.route('/cluster-data')
def get_cluster_data():
    converted_data = []

    for category, values in cluster_points.items():
        x, y = values
        converted_data.append({
            "type": category,
            "x": x,
            "y": y
    })
    return jsonify(converted_data)

if __name__ == '__main__':
    app.run(debug=True)