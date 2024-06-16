class Date:
    """
    she built the object
    """
    def __init__(self,year,mounth,day):
        self.year=year
        self.mouth=mounth
        self.day=day

    def __str__(self):
        """
        she return the str for us
        """
        import calendar
        return (str(self.day)+"th of "+ str(calendar.month_name[self.mouth])+str(self.year)+'\n')

    def __repr__(self):
        """
        she return the reper for build anoder object
        """
        return "Date({},{},{})".format(self.year, self.mouth, self.day)





class Time:
     """
       she built the object
     """
     def __init__(self,hour,minuts):
         self.hour= hour
         self.minuts=minuts

     """
           she return the str for us
     """
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
         """
        she return the reper for build anoder object
         """
         return "Time({},{})".format(self.hour,self.minuts)


class CalendarEntry(Date):
     tasks={}
     """
     she built the object use the init Date
     """
     def __init__(self,year,mouth,day):
         self.date=Date(year,mouth,day)

     """
     she add one Task to do
     """
     def addTask(self,namwwork,timestrt,timefinsih):
         timestrt=str(timestrt)
         timefinsih=str(timefinsih)
         tupletime=(timestrt,timefinsih)
         self.tasks[tupletime]=namwwork

     """
           she return the reper for build anoder object
     """
     def __repr__(self):
        return "CalendarEntry({},{},{})".format(self.date.year,self.date.mouth,self.date.day)

     """
                she return the str for us
     """
     def __str__(self):
         x=list(self.tasks.keys())
         y=""
         x.sort(key=lambda y:y[0])
         for i in x:
             y+= str(i[0])+'-'+str(i[1])+'-'+self.tasks[i]+'\n'
         return "Todo list for "+self.date.__str__()+y




today = Date(2017, 1, 20)
print(repr(today))
print(today.year)
print(today)
todo = CalendarEntry(2017, 1, 20)
t = Time(10,0)
print(repr(todo))
print(str(t))
todo.addTask("PPL lecture", t, Time(13,0))
todo.addTask("PPL homework#4", Time(14,0), Time(16,0))
todo.addTask("PPL homework#2", Time(14,0), Time(16,0))
todo.addTask("PPL homework#1", Time(7,0), Time(16,0))
print(todo.tasks)
print(todo)




