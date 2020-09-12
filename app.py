__author__ = 'T.J.'

from database import Database
from models.post import Post

Database.initialize()

post = Post('Post #1', 'Learn Python', 'T.J')
post2 = Post('Post #2', 'Learn 2 Hack!!!', 'T.J')


print(post.content)

print(post2.content)
