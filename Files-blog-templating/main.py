from flask import Flask, render_template
import requests

app = Flask(__name__)

BLOGS_URL = ' https://api.npoint.io/c790b4d5cab58020d391'
respone = requests.get(url=BLOGS_URL)
respone.raise_for_status()
data = respone.json()
print(data)

@app.route('/')
def home():
    return render_template("index.html", blogs=data)

@app.route('/post/<blog_id>')
def get_blog(blog_id):
    # blog_id is a string here
    return render_template('post.html', id=blog_id, blog=data[int(blog_id)-1])

if __name__ == "__main__":
    app.run(debug=True)
