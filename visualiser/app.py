from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# This should be fetched from a database in a real application
data = [
  {"name": "Framework 1", "type": "economic"},
  {"name": "Framework 2", "type": "economic"},
  {"name": "Framework 3", "type": "political"},
  {"name": "Framework 4", "type": "political"},
  {"name": "Framework 5", "type": "technology"},
  {"name": "Framework 6", "type": "technology"},
  # ... More data here ...
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    data_with_positions = []
    for framework in data:
        if framework['type'] == 'economic':
            position = (random.uniform(0, 0.3), random.uniform(0, 1))
        elif framework['type'] == 'political':
            position = (random.uniform(0.3, 0.6), random.uniform(0, 1))
        else:  # technology
            position = (random.uniform(0.6, 1), random.uniform(0, 1))
        data_with_positions.append({**framework, 'x': position[0], 'y': position[1]})
    return jsonify(data_with_positions)

if __name__ == '__main__':
    app.run(debug=True)