from pydantic import BaseModel
from typing import Dict, List, Optional


class Comment(BaseModel):
    author: str
    comment: str
    likes: int

class Post(BaseModel):
    author: str
    co_author: Optional[str]
    date: str
    title: str
    content: str
    id: int
    likes: List[str]
    comments: List[Comment]

comments = [
    Comment(author="test@test.com", comment="test", likes=12)
]

post = Post(
    author="josh@test.com",
    co_author="test",
    date='01/01/2026',
    title='test',
    content="test",
    id=12,
    likes=["one"],
    comments=comments
)

print(post.comments[0].author)
