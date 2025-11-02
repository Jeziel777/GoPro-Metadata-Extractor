# gunicorn_config.py

bind = "127.0.0.1:8000"
workers = 3  # Number of worker processes for handling requests
accesslog = "-"  # Log access to stdout
errorlog = "-"  # Log errors to stdout

