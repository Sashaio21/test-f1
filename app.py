import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():

    url = (
        "https://livetiming.formula1.com/static/"
        "2024/2024-07-28_Belgian_Grand_Prix/"
        "2024-07-27_Qualifying/"
        "SessionInfo.jsonStream"
    )

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            url,
            # headers=headers,
            timeout=20
        )

        status = response.status_code

        data = response.text[:1000]

    except Exception as e:
        status = "ERROR"
        data = str(e)


    return render_template(
        "index.html",
        status=status,
        data=data
    )


if __name__ == "__main__":
    app.run(debug=True)