from http.server import BaseHTTPRequestHandler
import json
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.app.main import app

# For Vercel Python runtime, we need to use Mangum adapter
try:
    from mangum import Mangum
    handler = Mangum(app, lifespan="off")
except ImportError:
    # Fallback - create a basic WSGI-ish handler
    class handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Mangum not installed"}).encode())
