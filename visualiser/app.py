from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# This should be fetched from a database in a real application
# add a third dimension to the data call text with lorem ipsum text
lorem_ipsum_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna 
aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
data = [
  {"name": "Framework 1", "type": "economic", "body": lorem_ipsum_text},
  {"name": "Framework 2", "type": "economic", "body": lorem_ipsum_text},
  {"name": "Framework 3", "type": "political", "body": lorem_ipsum_text},
  {"name": "Framework 4", "type": "political", "body": lorem_ipsum_text},
  {"name": "Framework 5", "type": "technology", "body": lorem_ipsum_text},
  {"name": "Framework 6", "type": "technology", "body": lorem_ipsum_text},
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