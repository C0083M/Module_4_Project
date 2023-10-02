import requests
import json

from http.server import HTTPServer, BaseHTTPRequestHandler

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
            except Exception as d:
                print(f'Error: {str(d)}')

        if __name__ == '__main__':
            get_ip_info()

def run_vercel_server():
    server_address = ("0.0.0.0", 3000)
    httpd = HTTPServer(server_address, IPCollectorHandler)
    httpd.serve_forever()

    if __name__ == "__main__":
        run_vercel_server()