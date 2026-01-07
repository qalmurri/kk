#from core.session import Session
#import requests
#
#class ApiClient:
#    @staticmethod
#    def get_headers():
#        token = Session.get_access_token()
#        return {
#            "Authorization": f"Bearer {token}"
#        } if token else {}
#    
#    @staticmethod
#    def get(url: str):
#        return requests.get(
#            f"http://{Session.get_backend_ip()}{url}",
#            headers=ApiClient.get_headers(),
#            timeout=10
#        )
#    
