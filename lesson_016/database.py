import peewee as peewee

database = peewee.SqliteDatabase("weather_data/ForecastWeather.db")


class Weather(peewee.Model):
    date = peewee.CharField()
    icon = peewee.CharField()
    condition = peewee.CharField()
    day_temp = peewee.CharField()
    night_temp = peewee.CharField()

    class Meta:
        database = database


class DatabaseUpdater:

    def __init__(self, data):
        self.data = data

    Weather.create_table()

    def delete_category(self, date):
        try:
            _date = Weather.get(Weather.date == date)
        except:
            return
        else:
            _date.delete_instance()

    def update_database(self, date):
        self.delete_category(date)
        data = self.data[date]
        icon = data['icon']
        condition = data['condition']
        day = data['day']
        night = data['night']
        db = Weather()
        db.create(
            date=date,
            icon=icon,
            condition=condition,
            day_temp=day,
            night_temp=night
        )

    def extract_data(self, date):
        db = Weather.select().where(Weather.date == date)
        _date = db.get().date
        icon = db.get().icon
        condition = db.get().condition
        day = db.get().day_temp
        night = db.get().night_temp
        data = {'icon': icon, 'day': day, 'night': night, 'condition': condition}
        return _date, data
