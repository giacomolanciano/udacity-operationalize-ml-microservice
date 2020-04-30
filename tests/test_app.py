import json
import sys

import pytest

sys.path.append("..")
import app


@pytest.fixture()
def client():
    """Generic Flask application fixture"""

    app.app.testing = True
    return app.app.test_client()


def test_predict(client):
    """Test route /predict"""

    request_payload = {
        "CHAS": {
            "0": 0
        },
        "RM": {
            "0": 6.575
        },
        "TAX": {
            "0": 296.0
        },
        "PTRATIO": {
            "0": 15.3
        },
        "B": {
            "0": 396.9
        },
        "LSTAT": {
            "0": 4.98
        }
    }

    response = client.post("/predict", json=request_payload)

    # check response status code is 200
    assert response.status_code == 200

    # check response is well-formed
    response_data = json.loads(response.data)
    assert "prediction" in response_data

    # check prediction is a list of values
    prediction_list = response_data["prediction"]
    assert isinstance(prediction_list, list)

    # check prediction values are float
    assert all([isinstance(x, float) for x in prediction_list])
