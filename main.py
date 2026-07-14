import fastf1
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2024, "Spa", "Q")
session.load(laps=True, telemetry=True, weather=True, messages=True)

lap = session.laps.pick_driver("NOR").pick_fastest()

tel = lap.get_car_data().add_distance()

plt.figure(figsize=(12, 6))

plt.plot(
    tel['Distance'],
    tel['Throttle'],
    label='Throttle'
)

plt.plot(
    tel['Distance'],
    tel['Brake'] * 100,
    label='Brake'
)

plt.xlabel("Distance")
plt.ylabel("Usage %")
plt.title("Throttle / Brake")
plt.legend()

plt.show()