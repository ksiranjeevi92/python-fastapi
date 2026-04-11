from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(
    prefix="/blog"
    ,tags=["blog"]
)

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]

@router.post("/new/{id}")
def create_blog(blog: BlogModel,id:int,version:int=1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }


@router.post("/new/{id}/comment")
def create_comment(blog: BlogModel,
                   id: int = Path(...),
                   comment_title: Optional[str] = Query(None,
                                        title='Title of the comment',
                                        description='Some description for comment_title',
                                        alias='comment_title',
                                        deprecated=True),
                   content: str = Body(..., min_length=1, max_length=30),
                   v: Optional[List[str]] = Query(['1.0', '1.1', '1.2']),
                   comment_id: int = Query(..., gt=5, le=10)):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id
    }