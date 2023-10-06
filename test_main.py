from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_send_email():
    email_data = {
        "to": "skylinenissanhinata@gmail.com",
        "subject": "My future job",
        "message": "Hello my job"
    }
    response = client.post("/send_email", json=email_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Email sent succesfully"}
