from flask import Flask, render_template, request
from python3_data import Historic_Data

app = Flask(__name__)
bd = Historic_Data()


@app.route("/")
def main():
    ret = render_template("History_country_people.html")
    return ret

@app.route("/countries", methods=['GET', 'POST'])
def countries():
    if request.method == 'GET':
        countries_list = sorted(bd.get_countries(), key=lambda x: x[1])
        ret = render_template("countries.html", countries_list=countries_list)
    elif request.method == 'POST':
        name_filter = request.form['search_country_name']
        countries_list = sorted(bd.get_countries(name_filter=name_filter), key=lambda x: x[1])
        ret = render_template("countries.html", countries_list=countries_list)
    return ret

@app.route("/country/<country_id>")
def country(country_id=None):
    country_info = bd.get_countries(country_id=country_id)
    language_info = sorted(bd.get_language(country_id), key=lambda x: x[1], reverse=True)
    events_info = sorted(bd.get_events(country_id=country_id), key=lambda x: x[2])
    persons_info = sorted(bd.get_persons(country_id=country_id), key=lambda x: x[2])
    ret = render_template("country.html",country_info=country_info[0], language_info=language_info, events_info=events_info, persons_info=persons_info)
    return ret


@app.route("/persons", methods=['GET', 'POST'])
def persons():
    if request.method == 'GET':
        persons_list = sorted(bd.get_persons(), key=lambda x: x[1])
        ret = render_template("persons.html", persons_list=persons_list)
    elif request.method == 'POST':
        name_filter = request.form['search_person_name']
        persons_list = sorted(bd.get_persons(name_filter=name_filter), key=lambda x: x[1])
        ret = render_template("persons.html", persons_list=persons_list)
    return ret


@app.route("/person/<person_id>")
def person(person_id=None):
    person_info = bd.get_persons(person_id=person_id)
    countries_info = sorted(bd.get_countries(person_id=person_id), key=lambda x: x[2])
    events_info = sorted(bd.get_events(person_id=person_id), key=lambda x: x[2])
    ret = render_template("person.html", countries_info=countries_info, events_info=events_info, person_info=person_info[0])
    return ret


@app.route("/events", methods=['GET', 'POST'])
def events():
    if request.method == 'GET':
        events_list = sorted(bd.get_events(), key=lambda x: x[1])
        ret = render_template("events.html", events_list=events_list)
    elif request.method == 'POST':
        title_filter = request.form['search_event_title']
        events_list = sorted(bd.get_events(title_filter=title_filter), key=lambda x: x[1])
        ret = render_template("events.html", events_list=events_list)
    return ret


@app.route("/event/<event_id>")
def event(event_id=None):
    event_info = bd.get_events(event_id=event_id)
    persons_info = sorted(bd.get_persons(event_id=event_id), key=lambda x: x[2])
    countries_info = sorted(bd.get_countries(event_id=event_id), key=lambda x: x[1])
    ret = render_template("event.html", countries_info=countries_info, event_info=event_info[0], persons_info=persons_info)
    return ret


app.run(host='0.0.0.0', port=6011)
