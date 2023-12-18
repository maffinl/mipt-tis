from sqlalchemy import create_engine, text

class Historic_Data(object):
   
    def __init__(self):
        self._engine = create_engine(f"sqlite:///data.db", echo=True)
        
    def get_country(self, country_id=None, historic_person_id=None, event_id=None, name_filter=None):
        if country_id:
            sql = text(
                "Select * from countrys where country_id=" + str(country_id))
        elif person_id:
            sql = text(
                "Select * from contry_person_conect inner join countrys using(country_id) where historic_person_id=" + str(person_id))
        elif event_id:
            sql = text(
                "Select * from contry_event_conect inner join countrys using(country_id) where event_id=" + str(event_id))
        elif name_filter:
            sql = text(
                "Select * from countrys where country_name like '%{}%'".format(name_filter))
        else:
            sql = text(
                "Select * from countrys")
        sql_result = self._engine.connect().execute(sql)
        ret = []
        for record in sql_result:
            ret.append(list(record))
        return ret

def get_person(self, country_id=None, historic_person_id=None, event_id=None, name_filter=None):
        if country_id:
            sql = text(
                "Select * from contry_person_conect inner join historic_persons using(historic_person_id) where country_id=" + str(country_id))
        elif historic_person_id:
            sql = text(
                "Select * from historic_persons left join date_death using(historic_person_id) where historic_person_id=" + str(person_id))
        elif event_id:
            sql = text(
                "Select * from person_event_conect inner join historic_persons using(historic_person_id) where event_id=" + str(event_id))
        elif name_filter:
            sql = text(
                "Select * from historic_persons left join date_death using(historic_person_id) where person_name like '%{}%'".format(name_filter))
        else:
             sql = text(
                 "Select * from historic_persons left join date_death using(historic_person_id) ")
        sql_result = self._engine.connect().execute(sql)
        ret = []
        for record in sql_result:
            ret.append(list(record))
        return ret

 def get_events(self, country_id=None, person_id=None, event_id=None, name_filter=None):
        if event_id:
            sql = text(
                "Select * from historic_events inner join event_type using(event_type_id) left join date_event_end using(event_id) where event_id=" + str(event_id))
        elif country_id:
            sql = text(
                "Select * from contry_event_conect inner join historic_events using(event_id) where country_id=" + str(country_id))
        elif person_id:
            sql = text(
                "Select * from person_event_conect inner join historic_events using(event_id) where historic_person_id=" + str(person_id))
        elif name_filter:
            sql = text(
                "Select * from historic_events left join date_event_end using(event_id) where title like '%{}%'".format(name_filter))
        else:
            sql = text(
                "Select * from historic_events left join date_event_end using(event_id)")
        sql_result = self._engine.connect().execute(sql)
        ret = []
        for record in sql_result:
            ret.append(list(record))
        return ret

def get_language(self, country_id):
        sql = text(
            "select language_name, persent_speak from contry_language_conect inner join languages using(language_id) where country_id=" + str(country_id))
        sql_result = self._engine.connect().execute(sql)
        ret = []
        for record in sql_result:
            ret.append(list(record))
        return ret
