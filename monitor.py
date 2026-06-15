from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stats")
def stats():
    cpu_percent = psutil.cpu_percent(interval = 1)
    cpu_temp = None

    try:
        # for x86 architecture
        temps = psutil.sensors_temperatures()
        if "coretemp" in temps:
            cpu_temp = temps["coretemp"][0].current
        # for ARM architecture
        elif "cpu_thermal" in temps:
            cpu_temp = temps["cpu_thermal"][0].current
    except AttributeError:
        pass

    ram = psutil.virtual_memory()

    disk = psutil.disk_usage("/")

    return jsonify ({
        "cpu": {
            "percent" : cpu_percent,
            "cores" : psutil.cpu_count(),
            "temp_celsius" : cpu_temp
        },
        "ram": {
            "total_gb" : round(ram.total / 1e9, 2),
            "used_gb" : round(ram.used / 1e9, 2),
            "percent": ram.percent
        },
        "disk": {
            "total_gb" : round(disk.total / 1e9, 2),
            "used_gb" : round(disk.used / 1e9, 2),
            "percent" : disk.percent
        }
    })

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8000)
