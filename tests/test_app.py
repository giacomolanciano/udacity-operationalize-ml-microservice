import json
import sys

import pytest

sys.path.append("..")
import app


@pytest.fixture()
def client():
    app_client = app.app.test_client()
    yield app_client


def test_predict(client):
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

    response_json = client.post("/predict", json=request_payload)

    # check response is well-formed
    response_data = json.loads(response_json.data)
    assert "prediction" in response_data

    # check prediction is a list of values
    prediction_list = response_data["prediction"]
    assert isinstance(prediction_list, list)

    # check prediction values are float
    assert all([isinstance(x, float) for x in prediction_list])
