from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = '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'  # Replace with your OpenAI API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['user_query']

    # Generate responses using ChatGPT
    response_1 = openai.Completion.create(
        engine='text-davinci-003',  # Replace with the appropriate ChatGPT model
        prompt=f'What frameworks and models should I analyze {user_query} with?',
        max_tokens=100
    )

    response_2 = openai.Completion.create(
        engine='text-davinci-003',  # Replace with the appropriate ChatGPT model
        prompt=f'Analyze {user_query} with {response_1.choices[0].text}',
        max_tokens=100
    )

    return render_template('index.html', query=user_query, response_1=response_1.choices[0].text, response_2=response_2.choices[0].text)

if __name__ == '__main__':
    app.run(debug=True)