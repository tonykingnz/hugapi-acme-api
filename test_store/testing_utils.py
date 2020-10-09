def create_store_statuscode_verification(response):
    assert response.json().get("status_code") == 201
