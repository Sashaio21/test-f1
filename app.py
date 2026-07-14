import fastf1
import matplotlib.pyplot as plt
from flask import Flask, render_template
import os

app = Flask(__name__)

fastf1.Cache.enable_cache("cache")


@app.route("/")
def index():

    session = fastf1.get_session(2024, "Monza", "Q")
    session.load()

    lec_lap = session.laps.pick_driver("LEC").pick_fastest()
    ver_lap = session.laps.pick_driver("VER").pick_fastest()

    lec_tel = lec_lap.get_car_data().add_distance()
    ver_tel = ver_lap.get_car_data().add_distance()

    plt.figure(figsize=(12, 6))

    plt.plot(
        lec_tel["Distance"],
        lec_tel["Speed"],
        label="Leclerc"
    )

    plt.plot(
        ver_tel["Distance"],
        ver_tel["Speed"],
        label="Verstappen"
    )

    plt.xlabel("Distance (m)")
    plt.ylabel("Speed (km/h)")
    plt.title("Monza 2024 Qualifying")
    plt.legend()

    os.makedirs("static", exist_ok=True)

    plt.savefig("static/speed.png")

    plt.close()

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)