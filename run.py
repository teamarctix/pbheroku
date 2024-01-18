from gunicorn import version_info

if version_info < (20, 0):
    print("Gunicorn version 20.0.0 or higher is required.")
    exit(1)

workers = 4  # You can adjust the number of workers based on your needs
bind = "0.0.0.0:8000"  # Change the host and port accordingly
timeout = 120

from app import app  # Assuming your app instance is named 'app' and is in the 'app.py' file

if __name__ == "__main__":
    from gunicorn.app.wsgiapp import WSGIApplication
    WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]").run()
