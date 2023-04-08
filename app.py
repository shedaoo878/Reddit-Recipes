from flask import Flask, render_template
import praw
import markdown
from bs4 import BeautifulSoup

app = Flask(__name__)

reddit = praw.Reddit(client_id="RvKIuTpV9eEvAehe1ul97g",
                     client_secret="vdr2y6P2SzzpnA4ZXODCO-eSX9dQ0Q",
                     user_agent="my user agent")

# list of topics


# adding a blank line helps space out the output in an organized way


# def getPost():
#     # iterate through the sampletopics list
#
#     # this will search the topic in the recipes subreddit and will sort the posts by top
#     for submission in reddit.subreddit('recipes').top(time_filter="week" , limit = 10):
#
#         # ensures that the post taken is a recipe
#         if submission.link_flair_text == 'Recipe':
#             posts.append({
#                 "Title" : submission.title,
#                 "Image" : requests.get(submission.url),
#                 "Author" : "u/" + submission.author,
#                 "Recipe" : submission.comments[0].body
#             })
#
#             #uses requests to convert the image url from the post into a jpg file
#            # image = requests.get(submission.url)
#             # if (image.status_code == 200):
#             #     output_filehandle = open(submission.title + '.jpg', mode='bx')
#             #     output_filehandle.write(image.content)

def convert_markdown_to_plain_text(text):
    html_text = markdown.markdown(text)
    soup = BeautifulSoup(html_text, "html.parser")
    return soup.get_text()



@app.route('/', methods=['GET'])

def index():
    posts = []

    for submission in reddit.subreddit('recipes').top(time_filter="month" , limit = 5):

        # ensures that the post taken is a recipe

            posts.append({
                "title" : submission.title,
                "image" : submission.url,
                "author" : submission.author,
                "recipe" : submission.comments[0].body
            })

    for post in posts:
        post['recipe'] = convert_markdown_to_plain_text(post['recipe'])


    return render_template('index.html', posts = posts)


if __name__ == '__main__':
    app.run(debug=True)




