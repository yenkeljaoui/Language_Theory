class InvalidDateException(Exception):
    def __init__(self , message):
        self.message=message
class InvalidTimeException(Exception):
    def __init__(self,message):
        self.message=message

class Date:
    def __init__(self,year,mounth,day):
        if year<=0:
           raise InvalidDateException("the year neet to be less 0")
        if mounth>=12 or mounth<=0:
           raise InvalidDateException("the mouth is neet to be between 0-12")
        if day>=30 or day<=0:
           raise InvalidDateException("the day is neet to be between 0-30")
        self.year = year
        self.mouth=mounth
        self.day=day

    def __str__(self):
        import calendar
        return (str(self.day)+"th of "+ str(calendar.month_name[self.mouth])+str(self.year)+'\n')

    def __repr__(self):
        return "Date({},{},{})".format(self.year, self.mouth, self.day)





class Time:
     def __init__(self,hour,minuts):
         if hour>=24 or hour<=0:
             raise InvalidTimeException("the hour neet to be between 1-24")
         if minuts>=60 or minuts<=0:
             raise InvalidTimeException("the minuts is neet to be  between 1-59")
         self.hour= hour
         self.minuts=minuts

     def __str__(self):
        x=str(self.hour)+':'+str(self.minuts)
        if self.minuts<10 :
            x=str(self.hour)+':'+'0'+str(self.minuts)
        if self.hour<10:
            x='0'+str(self.hour)+':'+str(self.minuts)
        if self.minuts<10 and self.hour<10:
            x='0'+str(self.hour)+':'+'0'+str(self.minuts)
        return x


     def __repr__(self):
         return "Time({},{})".format(self.hour,self.minuts)


class CalendarEntry(Date):
     tasks={}
     def __init__(self,year,mouth,day):
         self.date=Date(year,mouth,day)

     def addTask(self,namwwork,timestrt,timefinsih):
         timestrt=str(timestrt)
         timefinsih=str(timefinsih)
         tupletime=(timestrt,timefinsih)
         if tupletime in self.tasks:
             raise InvalidTimeException("The time is alerty Catch")
         self.tasks[tupletime]=namwwork





     def __repr__(self):
        return "CalendarEntry({},{},{})".format(self.date.year,self.date.mouth,self.date.day)


     def __str__(self):
         x=list(self.tasks.keys())
         y=""
         x.sort(key=lambda y:y[0])
         for i in (x):
             y+= str(i[0])+'-'+str(i[1])+'-'+self.tasks[i]+'\n'
         return "Todo list for "+self.date.__str__()+y



try:
   today = Date(8, 7, 20)
except InvalidDateException as os:
  print(os)
  exit()

print(repr(today))
print(today.year)
print(today)
try:
    todo = CalendarEntry(2017, 7, 20)
except InvalidDateException as os:
    print(os)
    exit()
try:
   t = Time(7,5)
except InvalidTimeException as os:
    print(os)
    exit()

print(repr(todo))
print(str(t))
try:
   todo.addTask("PPL lecture", t, Time(13,3))
   todo.addTask("PPL homework#4", Time(14,2), Time(16,5))
   todo.addTask("PPL homework#2", Time(14,1), Time(16,6))
   todo.addTask("PPL homework#1", Time(7,9), Time(16,8))
except InvalidTimeException as os:
    print(os)
    exit()
print(todo.tasks)
print(todo)
