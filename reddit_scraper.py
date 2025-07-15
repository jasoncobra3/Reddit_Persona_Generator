# Reddit Scraper Module ,Fetches user comments and posts from Reddit using the PRAW API.
import os
from typing import Dict, List
from dotenv import load_dotenv
import praw

load_dotenv()

# Initialize Reddit client using PRAW
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("USER_AGENT"),
)


def extract_username(profile_url: str) -> str:
    '''Extract the Reddit username from the profile URL.'''

    return profile_url.rstrip("/").split("/")[-1]


def get_user_data(profile_url: str) -> Dict[str, List[Dict]]:
    '''Fetches user data from Reddit including comments and posts.'''
    username = extract_username(profile_url)
    user = reddit.redditor(username)
    print(f"[DEBUG] Checking user: {user}")
    comments = []
    posts = []

    try:
        for comment in user.comments.new(limit=None):
            comments.append({
                "body": comment.body,
                "url": f"https://www.reddit.com{comment.permalink}"
            })

        for submission in user.submissions.new(limit=None):
            posts.append({
                "title": submission.title,
                "selftext": submission.selftext,
                "url": f"https://www.reddit.com{submission.permalink}"
            })

    except Exception as error:
        print(f"[ERROR] Failed to fetch data for user '{username}': {error}")

    return {
        "username": username,
        "comments": comments,
        "posts": posts
    }
