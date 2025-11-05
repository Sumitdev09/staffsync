"""
Top-level app entry so WSGI servers can import `app:app`.
Render sometimes uses `gunicorn app:app` by default; this file forwards to the real app in `src/app.py`.
"""
from src.app import app


if __name__ == '__main__':
    # Run the app locally for quick tests (do not use this in production)
    app.run(host='0.0.0.0', port=5000, debug=True)
