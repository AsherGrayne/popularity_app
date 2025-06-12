from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('books datasets/top_books_final.csv')
    # Get the top 10 books with title, image, and average rating
    books = df[['Book-Title', 'Image-URL-M', 'Avg-Rating', 'Num-Ratings']].head(10).to_dict(orient='records')
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)