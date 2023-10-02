import requests
from http.server import BaseHTTPRequestHandler
from typing import Dict

def get_ip_info() -> Dict[str, str]:
    try:
        response = requests.get('https://ipinfo.io')
        if response.status_code == 200:
            data = response.json()
            ipv4 = data.get('ip')
            ipv6 = data.get('ip6')
            return {
                "IPv4 Address": ipv4,
                "IPv6 Address": ipv6
            }
        else:
            return {
                "Error": f"HTTP Error {response.status_code}"
            }
    except Exception as d:
        return {
            "Error": str(d)
        }

def handler(event, context):
    ip_info = get_ip_info()
    return {
        "statusCode": 200,
        "body": ip_info
    }
