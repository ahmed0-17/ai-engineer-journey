from Project.async_api_collector import save_data
import json

# test save data



def test_save_data(tmp_path):
    processed_data=[
    {
        "id": 1,
        "name": "Ahmed",
        "email": "ahmed@example.com",
        "total_posts": 2,
        "total_todos": 3
    }
]

    save_data(tmp_path,processed_data)
    # check is file actually exist?
    file_path=tmp_path / "data.json"
    assert file_path.exists()

    # check is file data same as processed_data?
    with open(file_path,"r") as file:
        saved_data=json.load(file)
    assert saved_data==processed_data

           
