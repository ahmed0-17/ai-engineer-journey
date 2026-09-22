import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from Project.async_api_collector import get_data

@pytest.mark.anyio
async def test_get_data():

    users_response = MagicMock()
    posts_response = MagicMock()
    todos_response = MagicMock()


    users_response.json.return_value = [
    {
        "id": 1,
        "name": "Ahmed",
        "email": "ahmed@example.com"
    }
]

    posts_response.json.return_value = [
    {
        "userId": 1
    }
]

    todos_response.json.return_value = [
    {
        "userId": 1
    }
]


    mock_get = AsyncMock(
        side_effect=[
            users_response,
            posts_response,
            todos_response
        ]
    )

    mock_client = MagicMock()
    mock_client.__aenter__.return_value = mock_client
    mock_client.get = mock_get    

    with patch(
     "Project.async_api_collector.httpx.AsyncClient",
     return_value=mock_client
    ):
     result = await get_data()

    assert result["users"] == users_response.json.return_value
    assert result["posts"] == posts_response.json.return_value
    assert result["todos"] == todos_response.json.return_value
    mock_get.call_count==3

    mock_get.assert_any_call(
    "https://jsonplaceholder.typicode.com/users"
)

    mock_get.assert_any_call(
    "https://jsonplaceholder.typicode.com/posts"
)

    mock_get.assert_any_call(
    "https://jsonplaceholder.typicode.com/todos"
)





@pytest.mark.anyio
async def test_get_data_http_error():
    pass    