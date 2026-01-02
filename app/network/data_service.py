from network.api_client import ApiClient

class DataService:

    @staticmethod
    def fetch_scripts():
        return ApiClient.get("/script/")
