from flask import Flask, render_template
import requests
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    url = 'https://my2.raceresult.com/247805/RRPublish/data/list?key=96a9b4dbef71b91bc80a5df753aca94f&listname=Online%7CSBYU%20Results%20Mobile&page=results&contest=0&r=all&l=0'
    response = requests.get(url)
    if response.status_code == 304:
        return {}, 304
    
    # const lineGraph = $('<div>').addClass('line-graph');

    response_obj = response.json()['data']
    athletes = []

    string = "[img:flags/GB.gif]"
    pattern = r'\b([A-Z]{2})\b'

    for athlete in response_obj:
        country_code = "un"
        match = re.search(pattern, athlete[7])
        if match:
            country_code = match.group(1).lower()

        list.append(athletes, {
            'countryCode': country_code,
            'name': athlete[4],
            'position': athlete[1],
            'lastLapTime': athlete[8],
            'numberOfLaps': athlete[14],
            'totalTime': athlete[16],
            'status': athlete[2]
        })

    return {'athletes': athletes}, 200

if __name__ == '__main__':
    app.run(debug=True)
