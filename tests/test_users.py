from firebase_admin import auth
from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_create_user_success():
    res = client.post("/auth/signup", json={
        "email": "test.user1@gmail.com", "password": "password"})
    assert res.status_code == 200

# added so that we dont have residual users in the database from tests
@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """Cleanup a testing directory once we are finished."""
    def remove_test_users():
        users = auth.list_users().iterate_all()
        for user in users:
            if user.email.startswith("test.user"):
                auth.delete_user(user.uid)
    request.addfinalizer(remove_test_users)   

#exercise
# def test_create_user_conflict():
#     client.post("/auth/signup", json={
#         "email": "test.user2@gmail.com", "password": "password"})
#     res= client.post("/auth/signup", json={
#         "email": "test.user2@gmail.com", "password": "password"})
#     assert res.status_code == 409