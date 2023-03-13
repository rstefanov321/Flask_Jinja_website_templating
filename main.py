from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("index.html", posts=all_posts)


@app.route("/blog/<int:num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("post.html",
                           posts=all_posts,
                           num=num)

    # for blog in all_posts:
    #     if blog['id'] == num:
    #         chosen_title = blog['title']
    #         chosen_subtitle = blog['subtitle']
    #         chosen_body = blog['body']
    #
    #         return render_template("post.html",
    #                                title=chosen_title,
    #                                subtitle=chosen_subtitle,
    #                                ch_body=chosen_body)


if __name__ == "__main__":
    app.run(debug=True)
