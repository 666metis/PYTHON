
import requests

base_url = "https://ru.yougile.com/api-v2/projects"

token = "ZYE62mffbD4eJ4e5rlcpIefyH8SYi5yZM6zvpUOYLm9FtKeGCYsKhj3aTVp8GxSc"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
    }
def test_add_new():
    body = {
    "title": "Новый проект",
    "users": {
        "6ad7bcac-946f-44f3-b201-48ea14ed7dca": "admin"
    }
    }

    response = requests.post(base_url, headers=headers, json=body)
    assert response.status_code == 201

def test_list_project():
    response = requests.get(base_url, headers=headers)
    assert response.status_code == 200

def test_list_project_negative():
    response = requests.post(base_url, headers=headers)
    assert response.status_code == 400

def test_put_project():
    body = {
        "title": "Новый проект",
        "users": {
            "6ad7bcac-946f-44f3-b201-48ea14ed7dca": "admin"
        }
    }

    response = requests.post(base_url, headers=headers, json=body)
    assert response.status_code == 201
    project_id = response.json()["id"]

    body = {
    "title": "Новый проект - моей компании"
    }

    response = requests.put(base_url+"/"+project_id, headers=headers, json=body)
    assert response.status_code == 200

def test_put_project_negative():
    body = {
        "title": "Новый проект",
        "users": {
            "6ad7bcac-946f-44f3-b201-48ea14ed7dca": "admin"
        }
    }

    response = requests.post(base_url, headers=headers, json=body)
    assert response.status_code == 201
    project_id = response.json()["id"]

    body = {
    "title": ''
    }

    response = requests.put(base_url+"/"+project_id, headers=headers, json=body)
    assert response.status_code == 400


def test_get_project_id():
    body = {
        "title": "Новый проект",
        "users": {
            "6ad7bcac-946f-44f3-b201-48ea14ed7dca": "admin"
        }
    }

    response = requests.post(base_url, headers=headers, json=body)
    assert response.status_code == 201
    project_id = response.json()["id"]

    response = requests.get(base_url+"/"+project_id, headers=headers)
    assert response.status_code == 200

def test_get_project_id_negative():
    body = {
        "title": "Новый проект",
        "users": {
            "6ad7bcac-946f-44f3-b201-48ea14ed7dca": "admin"
        }
    }

    response = requests.post(base_url, headers=headers, json=body)
    assert response.status_code == 201
    project_id = response.json()["id"]

    response = requests.get(base_url+"/"+project_id)
    assert response.status_code == 401