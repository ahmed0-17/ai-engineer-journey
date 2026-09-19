import asyncio
import httpx
import logging
import json
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    filename="01_Python/Week_4/Day_3/app.log",
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)


async def get_data():
    urls = [
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/todos"
        ]
    try:

        logger.info("Start fetching data")

        async with httpx.AsyncClient() as client:

            tasks=[asyncio.create_task(client.get(url))   for url in urls]

            users, posts, todos = await asyncio.gather(*tasks)

            users.raise_for_status()
            posts.raise_for_status()
            todos.raise_for_status()

            result1 = users.json()
            result2 = posts.json()
            result3 = todos.json()

            logger.info("Data fetched successfully")

            return {
              "users":result1,
              "posts":result2,
               "todos":result3
          }

    except httpx.RequestError as error:
        logger.error(f"Request Error: {error}")

    except httpx.HTTPStatusError as error:
        logger.error(f"Status Error: {error}")

def process_data(users,posts,todos):
   logger.info("Processing users data")
   processed_users=[]
   for user in users:
          if "id" not in user:
             logger.error("User data missing 'id'")
             continue
          user_id=user["id"]

          user_posts=[post for post in posts if user_id==post["userId"]]
          user_todos=[todo for todo in todos if user_id==todo["userId"]]

  
          processed_users.append({
              "id":user_id,
              "name":user["name"],
              "email":user["email"],
              "total_posts":len(user_posts),
              "total_todos":len(user_todos)

          })
   logger.info("Users data processed successfully")
   return processed_users


def save_data(data_dir,processed_data):
     data_dir.mkdir(exist_ok=True,parents=True)
     file_path= data_dir / "data.json"   
     with open(file_path,"w") as file:
           json.dump(processed_data,file,indent=4)
           logger.info(f"Saved {len(processed_data)} users")        
    

async def main():
    result = await get_data()

    if result is None:
     logger.error("Failed to fetch data")
     return

    users=result["users"]
    posts=result["posts"]
    todos=result["todos"]
    data_dir= Path("01_Python/Week_4/Day_3/Data")

    processed_data=process_data(users,posts,todos)
    save_data(data_dir,processed_data)


asyncio.run(main())