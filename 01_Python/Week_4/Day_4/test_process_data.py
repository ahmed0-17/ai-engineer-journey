from Project.async_api_collector import process_data,save_data
import pytest

def test_process_data():
    users = [
    {
        "id": 1,
        "name": "Ahmed",
        "email": "ahmed@example.com"
    }
]

    posts = [
    {"userId": 1},
    {"userId": 1},
    {"userId": 2}
]

    todos = [
    {"userId": 1},
    {"userId": 1},
    {"userId": 1}
]

    assert process_data(users,posts,todos)==[
    {
        "id": 1,
        "name": "Ahmed",
        "email": "ahmed@example.com",
        "total_posts": 2,
        "total_todos": 3
    }
]





    def test_process_data_empty_users():
     users = []
     posts = [{"userId": 1}]
     todos = [{"userId": 1}]

     assert process_data(users, posts, todos) == []



def test_process_data_zero_postsandtodos():
 users = [
    {
        "id": 1,
        "name": "Ahmed",
        "email": "ahmed@example.com"
    }
]

 posts = []
 todos = []
 assert process_data(users,posts,todos)==[
    {
        "id": 1,
        "name": "Ahmed",
        "email": "ahmed@example.com",
        "total_posts": 0,
        "total_todos": 0
    }
]




def test_process_data_missingid():
  users = [
    {
        "name": "Ahmed",
        "email": "ahmed@example.com"
    }
]

  posts = []
  todos = [] 
  assert process_data(users,posts,todos)==[]




  def get_user_email(user):
    return user["email"]





