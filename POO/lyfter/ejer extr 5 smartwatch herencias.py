from datetime import datetime
class Clock:

    def show_time(self):
        self.time=datetime.now()
        #print(self.time)
        self.time.strftime("%H:%M:%S")
        return self.time
        


class Calendar:

    def show_date(self):
        self.only_date=datetime.now()
        self.date=self.only_date.date()
        self.date.strftime("%D/%M/%Y")
        return self.date


class Smartwatch(Clock,Calendar):
    
    def show_all(self):
        print("Welcome to your Smartwatch")
        self.time=self.show_time()
        print("Time:",self.time.strftime("%H:%M:%S"))
        self.date_now=self.show_date()
        print("Date:",self.date_now)

samsung=Smartwatch()
samsung.show_all()
