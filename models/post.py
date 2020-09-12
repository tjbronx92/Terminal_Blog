__author__ = 'T.J.'

from database import Database


class Post(object):

    def __init__(self, blog_id, title, content, author, post_id):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = post_id

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    def json(self):
        return{
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title
        }

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts', query={'id': id})

    @staticmethod
    def from_blog
        return [Database.find(collection='posts', query={'blog_id': id})]