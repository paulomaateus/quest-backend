from urllib.parse import urlparse

from . app import app
from . sqlite import setup_bd

url = urlparse('http://0.0.0.0:8000')
host, port = url.hostname, url.port
setup_bd()
app.run(host=host, port=port, debug=True)
