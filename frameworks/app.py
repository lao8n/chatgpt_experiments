from flask import Flask, render_template, request
import openai, os

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')  # Replace with your OpenAI API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['user_query']

    # Generate responses using ChatGPT
    response_1 = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  # Replace with your ChatGPT model ID
        messages=[
            {"role": "system", "content": "Use a list of frameworks to analyse" + user_query},
        ]
    )
    frameworks = response_1.choices[0].message.content.strip().split("\n")
    frameworks = [f for f in frameworks[1:-1] if f != '']
    print(frameworks)

    return render_template('index.html', query=user_query, frameworks=frameworks)

if __name__ == '__main__':
    app.run(debug=True)