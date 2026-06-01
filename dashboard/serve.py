import subprocess, sys, os, webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = 'localhost'
PORT = 8080

print("Generating dashboard data...")
subprocess.run([sys.executable, 'generate_data.py'], cwd=os.path.dirname(__file__))

os.chdir(os.path.dirname(__file__))
url = f'http://{HOST}:{PORT}'
print(f'Starting server at {url}')
webbrowser.open(url)

httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
