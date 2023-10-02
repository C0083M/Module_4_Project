import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            ip_info = self.get_public_ip_info()
            self.wfile.write(ip_info.encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Not Found".encode())
   
    def get_public_ip_info(self):
        url = "http://ip-api.com/json/"

        try:
            response = requests.get(url)
            response.raise_for_status()
            ip_info = response.json()

            if ip_info["status"] == "success":
                result += f"IPv4: {ip_info['query']}\n"
                return result
            else:
                return "Error retrieving IP Address"

        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

def run_vercel_server():
    server_address = ("0.0.0.0", 3000)
    httpd = HTTPServer(server_address, IPCollectorHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run_vercel_server()