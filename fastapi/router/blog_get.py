from fastapi import APIRouter,status, Response
from typing import Optional

from enum import Enum

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


@router.get("/all/new",
          summary="Retrieve all blogs",
         description="This API call simulate fetching all blogs")
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blog on page {page}"}

@router.get("/{id}/comments/{comment_id}", tags=["comment"])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulate retrieving a comment of blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path paramater

    """
    return {"message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"}

@router.get("/all", response_description="Retuen list of available blogs")
def get_all_blog():
    return "All blog"

class BlogType(str, Enum):
    short= 'short'
    story= 'story'
    howto= 'howto'

@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id:int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Get blog with ID {id}"}
    
