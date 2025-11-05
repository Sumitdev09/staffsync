Deploying StaffSync (quick guide)

This project is a small Flask app using SQLite. Below are simple steps to deploy to Render (recommended) or run locally with gunicorn.

1) Quick checklist before deploy
   - Ensure `requirements.txt` contains `gunicorn` (already added).
   - Make sure `Procfile` exists (already added):
     web: gunicorn src.app:app --workers 2 --bind 0.0.0.0:$PORT
   - Set a strong `SECRET_KEY` in environment variables on the host.

2) Deploy on Render
   - Create a Render account and connect your GitHub repo.
   - Create a new Web Service and select your repository + `main` branch.
   - For Build Command use:
     pip install -r requirements.txt
   - Start Command (Render will populate $PORT for you):
     gunicorn src.app:app --bind 0.0.0.0:$PORT
   - Add Environment variables:
     - SECRET_KEY: a long random string
     - FLASK_ENV: production
   - Create the service. Render will give you a public URL you can share.

3) Run locally with gunicorn (to validate before pushing)
   ```bash
   pip install -r requirements.txt
   SECRET_KEY='change-to-a-secure-value' gunicorn src.app:app --bind 0.0.0.0:5000
   # then open http://localhost:5000
   ```

4) Notes & caveats
   - SQLite: The app uses a local SQLite DB by default. PaaS file systems may be ephemeral. For production with persistence, switch to Postgres and use a DATABASE_URL environment variable.
   - To migrate to Postgres: add `psycopg2-binary` to `requirements.txt`, update DB connection code to parse `DATABASE_URL`, and run migration scripts.
   - Security: set a strong `SECRET_KEY` and never commit secrets to the repo.

If you want, I can prepare a Postgres migration branch and update the code to read `DATABASE_URL` automatically.
