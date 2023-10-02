import requests

from http.server import HTTPServer, BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):


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

def server():
    server_address = ("0.0.0.0", 3000)
    httpd = HTTPServer(server_address, IPCollectorHandler)
    httpd.server()

    if __name__ == "__main__":
        server()