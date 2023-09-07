from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_read_main():
    response = client.post(
        "/predict/",
        json={
            "features": {
                "avg_area_income": 79545.45857431678,
                "avg_area_house_age": 5.682861321615587,
                "avg_area_number_of_rooms": 7.009188142792237,
                "avg_area_number_of_bedrooms": 4.09,
                "area_population": 23086.800502686456,
                "address": "208 Michael Ferry Apt. 674 Laurabury, NE 37010-5101",
            },
            "provider": "payment-api",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "features": {
            "avg_area_income": 79545.45857431678,
            "avg_area_house_age": 5.682861321615587,
            "avg_area_number_of_rooms": 7.009188142792237,
            "avg_area_number_of_bedrooms": 4.09,
            "area_population": 23086.800502686456,
            "address": "208 Michael Ferry Apt. 674 Laurabury, NE 37010-5101",
        },
        "provider": "payment-api",
        "output": 1244892.8,
    }
