# Need requests to use the API, need BaseHTTPRequestHandler to use vercel serverless function
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

# Class handler invokes a serverless function in vercel. I had to read up on their documentation to figure this out
class handler(BaseHTTPRequestHandler):
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
   
    # Our original IP function from part 1
    def get_public_ip_info(self):
        url = "http://ip-api.com/json/"

        try:
            response = requests.get(url)
            response.raise_for_status()
            ip_info = response.json()

            if ip_info["status"] == "success":
                result = "Public IP Address Information:\n"
                result += f"IP Address: {ip_info['query']}\n"
                result += f"City: {ip_info['city']}\n"
                result += f"Region: {ip_info['regionName']}\n"
                result += f"Country: {ip_info['country']}\n"
                result += f"ISP: {ip_info['isp']}"
                return result
            else:
                return "Failed to retrieve IP information."

        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

# The serverless function definition and function itself
def run_vercel_server():
    server_address = ("0.0.0.0", 3000)
    httpd = HTTPServer(server_address, IPCollectorHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run_vercel_server()