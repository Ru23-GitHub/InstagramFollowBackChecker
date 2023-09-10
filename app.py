from flask import Flask, render_template, request, url_for
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

    try:
        followers_file = request.files["followers_file"]
        followers_data = json.load(followers_file)
        followers_set = set()
        for follower in followers_data:
            followers_set.add((follower["string_list_data"][0]['value'],follower["string_list_data"][0]['href']))

        print("GOT HERE 1")

        following_file = request.files["following_file"]
        following_data = json.load(following_file)
        following_set = set()
        for follower in following_data["relationships_following"]:
            following_set.add((follower["string_list_data"][0]['value'],follower["string_list_data"][0]['href']))

        print("GOT HERE 2")

        title = "IFBC - Results"

        print("GOT HERE 3")
        return render_template("form.html", title=title, names = get_follow_difference(followers_set,following_set))
    except:
        title = "IFBC - Error"
        return render_template("error.html", title=title)
