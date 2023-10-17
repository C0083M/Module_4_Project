import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            ip_info = self.get_public_ip_info()
            self.wfile.write(ip_info.encode())
        else:
            self.send_response(404)
            self.send_header("Content-type")
            self.end_headers()
            self.wfile.write("Error".encode())
   
    def get_public_ip_info(self):
        url = "http://ip-api.com/json/"

        try:
            response = requests.get(url)
            response.raise_for_status()
            ip_info = response.json()

            if ip_info["status"] == "success":
                result = "<html><body style='font-family: Arial; color: red;'>"
                result += "<h1>Retrieved IP Information</h1>"
                result += f"<p>IP Address: {ip_info['query']}</p>"
                result += f"<p>Country: {ip_info['country']}</p>"
                result += f"<p>ISP: {ip_info['isp']}</p>"
                result += f"<p>Capital: {ip_info['capital']}</p>"
                result += "</body></html>"
                return result
            else:
                return "IP retrieval Error"

        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

def run_vercel_server():
    server_address = ("0.0.0.0", 3000)
    httpd = HTTPServer(server_address, IPCollectorHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run_vercel_server()