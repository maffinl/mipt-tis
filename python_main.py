from flask import Flask, render_template, request
from python_data import Historic_Data

app = Flask(__name__)
bd = Historic_Data()


@app.route("/")
def main():
    ret = render_template("History_country_people.html")
    return ret

@app.route("/")
def country(country_id=None):
    country_info = bd.get_country(country_id=country_id)
    language_info = sorted(bd.get_language(country_id), key=lambda x: x[1], reverse=True)
    events_info = sorted(bd.get_events(country_id=country_id), key=lambda x: x[2])
    persons_info = sorted(bd.get_person(country_id=country_id), key=lambda x: x[2])
    ret = render_template('country.html', country_info=country_info, language_info=language_info,>    return ret


app.run(host='0.0.0.0', port=6011)