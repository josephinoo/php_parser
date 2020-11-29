import logging
import sys
import threading

from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)

# Defaults to stdout
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
try:
    log.info('Logging to console')
except:
    _, ex, _ = sys.exc_info()
    log.error(ex.message)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
