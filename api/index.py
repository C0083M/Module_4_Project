import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

class IPCollectorHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            ip_info = self.get_public_ip_info()
            self.wfile.write(ip_info.encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Not Found".encode())

    def get_public_ip_info(self):
        try:
            response = requests.get('https://ipinfo.io')
            if response.status_code == 200:
                data = response.json()
                ipv4 = data.get('ip')
                ipv6 = data.get('ip6')
                return f'IPv4 Address: {ipv4}\nIPv6 Address: {ipv6}'
            else:
                return f'Error: {response.status_code}'
        except Exception as e:
            return f'Error: {str(e)}'

def run_vercel_server():
    server_address = ("0.0.0.0", 3000)
    httpd = HTTPServer(server_address, IPCollectorHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run_vercel_server()
