import requests
import json
{
 "ipinfo": {
        "api_key": "76fc0d7790488e"
}
}
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    #api_token = "76c0d7790488e"

        def get_ip_info():
            try:

                response = requests.get('https://ipinfo.io')

                if response.status_code == 200:
                    data = response.json()

                    ipv4 = data.get('ip')
                    ipv6 = data.get('ip6')

                    print(f'IPv4 Address: {ipv4}')
                    print(f'IPv6 Address: {ipv6}')
                else:
                    print(f'Error: {response.status_code}')
            except Exception as e:
                print(f'Error: {str(e)}')

        if __name__ == '__main__':
            get_ip_info()
