from os import stat
from flask.json import jsonify
from .Database import Database

class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens
    
    @staticmethod
    def read_gewicht_van_drinken():
        sql = 'select gewicht from bak where baktypeid =1 and datum = "2021-06-02" group by hour(tijd)'
        return Database.get_rows(sql)

    @staticmethod
    def read_gewicht_van_voer():
        sql = 'select gewicht from bak where baktypeid =2 and datum = "2021-06-02" group by hour(tijd)'
        return Database.get_rows(sql)


    @staticmethod
    def read_last_temperatuur():
        sql = 'select temperatuur from bak where datum = (select max(datum)) and tijd = (select max(tijd)) and baktypeid =1 order by datum desc limit 1'
        return Database.get_rows(sql)

    @staticmethod
    def create_bak(BakTypeID, gewicht, Temperatuur, Datum, Tijd):
        sql = "INSERT INTO bak(BakTypeID, gewicht, Temperatuur, Datum, Tijd) VALUES(%s,%s,%s,%s,%s)"
        params = [BakTypeID, gewicht, Temperatuur, Datum, Tijd]
        return Database.execute_sql(sql, params)
    
    @staticmethod
    def read_temp(tempid):
        sql = "SELECT temperatuur from bak WHERE bakid = %s"
        params = [tempid]
        return Database.get_one_row(sql, params)

    @staticmethod
    def read_gewicht_drinkbak():
        sql = 'select gewicht_drinkbak from gewicht_bakken'
        return Database.get_rows(sql)

    @staticmethod
    def read_gewicht_voerbak():
        sql = 'select gewicht_voerbak from gewicht_bakken'
        return Database.get_rows(sql)

    @staticmethod
    def update_gewicht_drinkbak(drink,voer):
        sql='UPDATE gewicht_bakken set Gewicht_drinkbak = %s, gewicht_voerbak =%s where gewicht_bakkenID = 1'
        params = [drink,voer]
        return Database.execute_sql(sql, params)

    @staticmethod
    def read_all_kattenluik():
        sql ='SELECT datum, tijd FROM kattenluik order by KattenluikID desc limit 30 '
        return Database.get_rows(sql)


    @staticmethod
    def read_last_kattenluik():
        sql ='SELECT datum, tijd FROM kattenluik order by KattenluikID desc limit 1 '
        return Database.get_rows(sql)

    @staticmethod
    def create_kattenluik(datum,tijd):
        sql = "INSERT INTO kattenluik(Datum,Tijd) VALUES(%s,%s)"
        params = [datum,tijd]
        return Database.execute_sql(sql, params)

