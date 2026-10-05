from flask import Flask, jsonify
import time

app = Flask(__name__)

total_requests = 0
failed_requests = 0
total_response_time = 0

@app.before_request
def start_timer():
    from flask import g
    g.start_time = time.time()

@app.after_request
def record_metrics(response):
    global total_requests, failed_requests, total_response_time

    duration = time.time() - __import__("flask").g.start_time

    total_requests += 1
    total_response_time += duration

    if response.status_code >= 400:
        failed_requests += 1

    response.headers["X-Response-Time"] = str(round(duration, 4))
    return response

@app.route("/")
def home():
    return "Student Management Application"

@app.route("/students")
def students():
    return jsonify([
        {"id": 1, "name": "Ram"},
        {"id": 2, "name": "Sita"}
    ])

@app.route("/error")
def error():
    return "Application Error", 500

@app.route("/metrics")
def metrics():
    avg_time = (
        total_response_time / total_requests
        if total_requests else 0
    )

    error_rate = (
        failed_requests / total_requests * 100
        if total_requests else 0
    )

    return jsonify({
        "total_requests": total_requests,
        "failed_requests": failed_requests,
        "average_response_time_seconds": round(avg_time, 4),
        "error_rate_percent": round(error_rate, 2)
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)