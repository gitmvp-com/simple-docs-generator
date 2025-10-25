#!/usr/bin/env python3
"""Simple HTTP Server for Documentation Preview

Serves the built documentation on localhost:8000
"""

import http.server
import socketserver
import os
from pathlib import Path

PORT = 8000
BUILD_DIR = "build"

def serve():
    """Start a simple HTTP server"""
    build_path = Path(BUILD_DIR)
    
    if not build_path.exists():
        print(f"Error: {BUILD_DIR}/ directory not found!")
        print("Run 'python build.py' first to generate the documentation.")
        return
    
    # Change to build directory
    os.chdir(BUILD_DIR)
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\n✅ Documentation server running at http://localhost:{PORT}")
        print(f"Press Ctrl+C to stop\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped")

if __name__ == '__main__':
    serve()
