from network.api_client import api_client

def fetch_scripts(params=None):
    response = api_client.get("/script/", params=params)

    #validasi struktur api_client
    if not isinstance(response, dict):
        raise TypeError("Api response is not dict")

    if not response.get("success", False):
        raise ValueError("Api returned success=False")

    data = response.get("data", [])

    if not isinstance(data, list):
        raise TypeError("Api 'data' is not list")

    return data
