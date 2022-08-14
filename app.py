from flask import Flask, render_template, request, redirect
import json



def get_follow_difference(follower_set,following_set,d_type = True):
    if d_type == True:
        return following_set - follower_set
    if d_type == False:
        return follower_set - following_set
app = Flask(__name__)

@app.route('/')
def index():
    title = "Instagram Follow Back Checker"
    return render_template("index.html", title = title)


@app.route("/form", methods = ["POST"])
def form():
    followers_file = request.files["followers_file"]
    followers_data = json.load(followers_file)
    followers_set = set()
    for follower in followers_data["relationships_followers"]:
        followers_set.add((follower["string_list_data"][0]['value'],follower["string_list_data"][0]['href']))

    following_file = request.files["following_file"]
    following_data = json.load(following_file)
    following_set = set()
    for follower in following_data["relationships_following"]:
        following_set.add((follower["string_list_data"][0]['value'],follower["string_list_data"][0]['href']))

    title = "IFBC - Results"
    return render_template("form.html", title=title, names = get_follow_difference(followers_set,following_set))