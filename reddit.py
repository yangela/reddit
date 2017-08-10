## Playing around with the Reddit API

import praw
import pdb
import re
import os

reddit = praw.Reddit(client_id='[clientID]',
                     client_secret='[clientSecret]',
                     password='[password]',
                     user_agent='[useragent]',
                     username='[username]')

## Printing the first 5 posts in specific subreddit

subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("-------------\n")

## Auto-responding to certain phrases in specific subreddits

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=2):
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("me too!")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

f = open("posts_replied_to.txt")
print(f.read())
