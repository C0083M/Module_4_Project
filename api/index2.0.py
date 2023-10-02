from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def get_ip_info():
    try:
        response = requests.get('https://ipinfo.io')
        if response.status_code == 200:
            data = response.json()
            ipv4 = data.get('ip')
            ipv6 = data.get('ip6')
            return jsonify({"IPv4 Address": ipv4, "IPv6 Address": ipv6})
        else:
            return jsonify({"Error": response.status_code}), response.status_code
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
