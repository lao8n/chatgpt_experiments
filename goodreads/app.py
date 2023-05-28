from flask import Flask, render_template, request
import openai, os
import pandas as pd

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')  # Replace with your OpenAI API key
# Load the book data into a DataFrame
book_df = pd.read_csv('goodreads_library_export.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['user_query']

    # Extract book titles and authors
    df_read = book_df[book_df['Exclusive Shelf'] == 'read']
    books = df_read[['Title', 'Author']].values.tolist()
    # Create a string representation of the book data
    book_str = '\n'.join(f'Title: {title}, Author: {author}' for title, author in books)
    # Combine the book data with the user query
    prompt = f'Use the main frameworks and models in these books:\n{book_str}\n\n '+ \
        f' to analyse the following query:\n{query}'
    print(len(prompt), prompt)
    response_1 = openai.ChatCompletion.create(
        model='gpt-4',  # Replace with your ChatGPT model ID
        messages=[
            {"role": "system", "content": prompt},
        ]
    )
    frameworks = response_1.choices[0].message.content.strip().split("\n")
    frameworks = [f for f in frameworks[1:-1] if f != '']

    return render_template('index.html', query=user_query, frameworks=frameworks)

if __name__ == '__main__':
    app.run(debug=True)