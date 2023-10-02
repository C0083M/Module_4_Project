import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

class IPCollectorHandler(BaseHTTPRequestHandler):

    def get_ip_info(self):
        try:
            response = requests.get('https://ipinfo.io')
            if response.status_code == 200:
                data = response.json()
                ipv4 = data.get('ip')
                ipv6 = data.get('ip6')
                return f'IPv4 Address: {ipv4}\nIPv6 Address: {ipv6}'
            else:
                return f'Error: {response.status_code}'
        except Exception as d:
            return f'Error: {str(d)}'

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response = self.get_ip_info()
        self.wfile.write(response.encode())

def run_server():
    server_address = ("0.0.0.0", 3000)
    httpd = HTTPServer(server_address, IPCollectorHandler)
    print("Server is running on port 3000")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
