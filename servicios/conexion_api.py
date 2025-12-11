import requests


def obtener_posts():
    return requests.get("https://jsonplaceholder.typicode.com/posts").json()


def obtener_comments():
    return requests.get("https://jsonplaceholder.typicode.com/comments").json()