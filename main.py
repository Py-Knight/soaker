from flask import Flask, render_template, request
from datetime import datetime, timedelta

display_result = []

app = Flask(__name__)


@app.route('/')
def soaker():
    display_result.clear()
    duration = request.args.get("duration")
    if duration:
        calculate_soak()
               
    return render_template('soaker.html', display_result=display_result)


def calculate_soak():
    start = request.args.get("start_time", "")
    duration = request.args.get("duration")
    started = (str(start))
    period = (str(duration))
    formatter = '%H:%M'
    dt = datetime.strptime(started, formatter)
    soaktime = timedelta(minutes=+int(period))
    endsoak = dt + soaktime
    result = endsoak.strftime("%H:%M")
    display_result.append(result)
    

if __name__ == "__main__":
    app.run(debug=False)

