"""
Debug server: serves static site and writes NDJSON logs to .cursor/debug.log
for diagnosing ERR_CONNECTION_REFUSED.
"""
import json
import os
import sys
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

_SCRIPT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
LOG_PATH = os.path.join(_SCRIPT_DIR, ".cursor", "debug.log")
PORT = 8000
HOST = "127.0.0.1"

def log(msg, data=None, hypothesis_id=None):
    # #region agent log
    payload = {
        "id": f"log_{msg}_{hash(str(data))}",
        "timestamp": __import__("time").time() * 1000,
        "location": "serve_debug.py",
        "message": msg,
        "data": data or {},
        "hypothesisId": hypothesis_id,
    }
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload) + "\n")
    # #endregion

request_logged = False

class LoggingHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # suppress default console log

    def do_GET(self):
        global request_logged
        # #region agent log
        if not request_logged:
            request_logged = True
            log(
                "request_received",
                {"path": self.path, "client_address": list(self.client_address), "port": PORT},
                "H2_H3",
            )
        # #endregion
        return SimpleHTTPRequestHandler.do_GET(self)

def main():
    # #region agent log
    log("attempting_start", {"port": PORT, "host": HOST, "cwd": os.getcwd(), "log_path": LOG_PATH}, "H1_H4")
    # #endregion

    os.chdir(os.path.join(_SCRIPT_DIR, "static"))

    try:
        server = HTTPServer((HOST, PORT), LoggingHandler)
    except OSError as e:
        # #region agent log
        log("server_bind_failed", {"error": str(e), "errno": getattr(e, "errno", None)}, "H4")
        # #endregion
        print(f"Failed to start server: {e}", file=sys.stderr)
        sys.exit(1)

    # #region agent log
    log("server_listening", {"host": HOST, "port": PORT, "url": f"http://{HOST}:{PORT}/"}, "H1_H2")
    # #endregion

    print(f"Serving at http://{HOST}:{PORT}/  (logs: {LOG_PATH})")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.shutdown()

if __name__ == "__main__":
    main()
