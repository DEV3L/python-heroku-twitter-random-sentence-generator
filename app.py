from flask import Flask
from flask.ext.runner import Runner
from heroku_random_taylor_swift_lyrics.utils.facebook import post_to_facebook_page
from heroku_random_taylor_swift_lyrics.utils.sentence_generator import generate_sentence
from heroku_random_taylor_swift_lyrics.utils.twitter import post_to_twitter_account

app = Flask(__name__)
runner = Runner(app)


@app.route("/")
def index():
    return generate_sentence()


@app.route("/facebook")
def facebook():
    return post_to_facebook_page(generate_sentence())


@app.route("/twitter")
def facebook():
    return post_to_twitter_account()


if __name__ == "__main__":
    runner.run()