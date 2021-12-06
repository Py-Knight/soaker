from flask import Flask, render_template
from flask import request
import sys
from datetime import datetime, timedelta

disp_result = []

app = Flask(__name__)


@app.route('/')
def soaker():
    disp_result.clear()
    dur = request.args.get("duration", "")
    if dur:
        run = calc()
    else:
        run = ""
               
    return render_template('soaker.html', disp_result=disp_result)

@app.route("/")
def calc():
    st = request.args.get("start_time", "")
    dur = request.args.get("duration")
    #print(str(st))
    #print(str(dur))
    stc = (str(st))
    durc = (str(dur))
    formatter = '%H:%M'
    dt = datetime.strptime(stc, formatter)
    soaktime = timedelta(minutes=+int(durc))
    endsoak = dt + soaktime
    #Print just the time
    result = endsoak.strftime("%H:%M")
    disp_result.append(result)
    #print(endsoak.strftime("%H:%M"))
    #print(result) 
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

