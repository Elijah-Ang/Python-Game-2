# Vercel Python Serverless Function
# This file exports the FastAPI app for Vercel's native ASGI support

import sys
import os

# Add the api directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import app

# Vercel will use this ASGI app directly
