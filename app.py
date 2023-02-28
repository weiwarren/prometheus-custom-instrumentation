from flask import Flask
from prometheus_client import Counter, Gauge, Summary, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('myapp_request_count', 'Total number of requests')
REQUEST_LATENCY = Summary('myapp_request_latency_seconds', 'Request latency in seconds')
ACTIVE_REQUESTS = Gauge('myapp_active_requests', 'Number of active requests')

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/request')
def request():
    REQUEST_COUNT.inc()
    ACTIVE_REQUESTS.inc()
    with REQUEST_LATENCY.time():
        # Simulate a request that takes some time
        import time
        time.sleep(1)
    ACTIVE_REQUESTS.dec()
    return 'Request complete!'

if __name__ == '__main__':
    ACTIVE_REQUESTS.set(0)
    app.run(debug=True, host='0.0.0.0', port=8001)