import requests

ECOSCORE_GRADE = 'd'


def mock_openfond_success(self, method, url):
    def monckey_json():
        return {
            'product': {
                'ecoscore_grade': ECOSCORE_GRADE
            }
        }

    response = requests.Response()
    response.status_code = 200
    response.json = monckey_json()
    return response