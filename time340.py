# Jason Sy
# CSS 340: Applied Computing
# April 22 2022
# 
# Program creates TimeSpan Class representing duration of time in seconds, minutes and hours 
# Can perform Operator Overloading

class TimeSpan():

    #constructor
    def __init__(self, seconds = 0, minutes = 0, hours = 0):
        self._seconds = int(seconds)
        self._minutes = int(minutes)
        self._hours = int(hours)
        print(self, end = "\r")

    #return the number of seconds
    def get_seconds(self):
        return self._seconds

    #return the number of minutes
    def get_minutes(self):
        return self._minutes

    #return the number of hours
    def get_hours(self):
        return self._hours

    #range rule
    def in_range(self, seconds, minutes, hours):
        if seconds < 60 and seconds > -60:
            return True
        if minutes < 60 and minutes > -60:
            return True
        else:
            return False
    
    #total seconds
    def totalSeconds(self):
        return (self._seconds) + (self._minutes * 60) + (self._hours * 3600)

    #converter
    def convert(self):
        negative = False
        seconds = self.totalSeconds()
        if(seconds < 0):
           seconds = (seconds * -1)
           negative = True
        hours = seconds // 3600
        minutes = (seconds - (hours * 3600)) // 60
        seconds = (seconds - (hours * 3600) - (minutes * 60))
        if(negative):
            self._seconds = seconds * -1
            self._minutes = minutes * -1
            self._hours = hours * -1
        else:
            self._seconds = seconds
            self._minutes = minutes
            self._hours = hours

    #set the number of hours, minutes, seconds
    def set_time(self, seconds, minutes, hours):
        if self.in_range(seconds, minutes, hours):
            self._seconds = seconds
            self._minutes = minutes
            self._hours = hours
            self.convert()
            return True
        else:
            self.convert()
            return False

    #addition operator
    def __add__(self, time):
        timeTotal = TimeSpan(time.get_seconds(), time.get_minutes(), time.get_hours())
        timeTotal.set_time(self.get_seconds() + time.get_seconds(), self.get_minutes() + time.get_minutes(), self.get_hours() + time.get_hours())
        return timeTotal

    #subtraction operator
    def __sub__(self, time):
        timeTotal = TimeSpan(time.get_seconds(), time.get_minutes(), time.get_hours())
        timeTotal.set_time(self.get_seconds() - time.get_seconds(), self.get_minutes() - time.get_minutes(), self.get_hours() - time.get_hours())
        return timeTotal
    
    #multiplication operator
    def __mul__(self, time):
        timeTotal = TimeSpan(time.get_seconds(), time.get_minutes(), time.get_hours())
        timeTotal.set_time(self.get_seconds() * time.get_seconds(), self.get_minutes() * time.get_minutes(), self.get_hours() * time.get_hours())
        return timeTotal

    #floor division operator
    def __floordiv__(self, time):
        timeTotal = TimeSpan(time.get_seconds(), time.get_minutes(), time.get_hours())
        timeTotal.set_time(self.get_seconds() // time.get_seconds(), self.get_minutes() // time.get_minutes(), self.get_hours() // time.get_hours())
        return timeTotal

    #true division operator
    def __truediv__(self, time):
        timeTotal = TimeSpan(time.get_seconds(), time.get_minutes(), time.get_hours())
        timeTotal.set_time(self.get_seconds() / time.get_seconds(), self.get_minutes() / time.get_minutes(), self.get_hours() / time.get_hours())
        return timeTotal
    
    #power operator
    def __pow__(self, time):
        timeTotal = TimeSpan(time.get_seconds(), time.get_minutes(), time.get_hours())
        timeTotal.set_time(self.get_seconds() ** time.get_seconds(), self.get_minutes() ** time.get_minutes(), self.get_hours() ** time.get_hours())
        return timeTotal
    
    #modulo operator
    def __mod__(self, time):
        timeTotal = TimeSpan(time.get_seconds(), time.get_minutes(), time.get_hours())
        timeTotal.set_time(self.get_seconds() % time.get_seconds(), self.get_minutes() % time.get_minutes(), self.get_hours() % time.get_hours())
        return timeTotal

    #unary negation/inverse operator
    def __neg__(self):
        timeTotal = TimeSpan(-1 * self.get_seconds(),-1 * self.get_minutes(), -1 * self.get_hours())
        return timeTotal
        
    #equality operator
    def __eq__(self, time):
        selfTotalSeconds = self.totalSeconds()
        timeTotalSeconds = time.totalSeconds()
        if selfTotalSeconds == timeTotalSeconds:
            return True
        else:
            return False

    #less than operator
    def __ne__(self, time):
        selfTotalSeconds = self.totalSeconds()
        timeTotalSeconds = time.totalSeconds()
        if selfTotalSeconds != timeTotalSeconds:
            return True
        else:
            return False

    #less than operator
    def __lt__(self, time):
        selfTotalSeconds = self.totalSeconds()
        timeTotalSeconds = time.totalSeconds()
        if selfTotalSeconds < timeTotalSeconds:
            return True
        else:
            return False

    #less than or equal to operator
    def __le__(self, time):
        selfTotalSeconds = self.totalSeconds()
        timeTotalSeconds = time.totalSeconds()
        if selfTotalSeconds < timeTotalSeconds or selfTotalSeconds == timeTotalSeconds:
            return True
        else:
            return False

    #greater than operator
    def __gt__(self, time):
        selfTotalSeconds = self.totalSeconds()
        timeTotalSeconds = time.totalSeconds()
        if selfTotalSeconds > timeTotalSeconds:
            return True
        else:
            return False

    #greater than or equal to operator
    def __ge__(self, time):
        selfTotalSeconds = self.totalSeconds()
        timeTotalSeconds = time.totalSeconds()
        if selfTotalSeconds > timeTotalSeconds or selfTotalSeconds == timeTotalSeconds:
            return True
        else:
            return False

    def __str__(self):
        self.set_time(self._seconds, self._minutes, self._hours)
        return "Hours: " + str(round(self._hours)) + ", Minutes: " + str(round(self._minutes)) + ", Seconds: " + str(round(self._seconds))
