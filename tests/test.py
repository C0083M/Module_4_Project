# tests/test.py
from Module_4_Project.api.index import get_public_ip_info

class MockResponse:
    def json(self):
        return {
            "status": "success",
            "query": "192.168.1.1",
            "country": "United States",
            "isp": "Some ISP",
            "regionName": "California",
            "city": "Los Angeles"
        }

def test_get_public_ip_info_success():
    import requests
    import requests_mock

    with requests_mock.mock() as m:
        m.get("http://ip-api.com/json/", text="{}")

        result = get_public_ip_info()

    expected_result = (
        "Retrieved IP Address\n"
        "IPv4: 192.168.1.1\n"
        "Country: United States\n"
        "ISP: Some ISP\n"
        "Region: California\n"
        "City: Los Angeles\n"
    )

    assert result == expected_result

def test_get_public_ip_info_error():
    import requests
    import requests_mock

    with requests_mock.mock() as m:
        m.get("http://ip-api.com/json/", exc=requests.exceptions.RequestException)

        result = get_public_ip_info()

    expected_result = "Error: RequestException"

    assert result == expected_result
