def make_class(sttatic_attributes, base_class=None):
    def get_value(name):
        #מחזיר את הערך של המשתנה באופייקט
        if name in sttatic_attributes:
            return sttatic_attributes[name]
        #זה בודק באבא אם אין בבן
        elif base_class is not None:
            return base_class['get'](name)

    def set_value(name, value):
        #מכניס לתוך
        sttatic_attributes[name] = value

    def new(*args):
        #*args=make me one args for all the variables
        return init_instance(cls, *args)

    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls


def init_instance(cls, *args):
    instance = make_instance(cls)
    init = cls['get']('__init__')
    #init=she have the building func
    if init:
        init(instance, *args)
    return instance


""""""

def make_instance(cls):
    attributes = {}
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)

    def set_value(name, value):
        attributes[name] = value

    instance = {'get': get_value, 'set': set_value}
    return instance


def bind_method(value, instance):
    if callable(value):
       def method(*args):
          return value(instance, *args)
       return method
    else:
        return value



""""""

def make_date_class():
    def __init__(self,year,mouth,day):
        self['set']('year',year)
        self['set']('mouth', mouth)
        self['set']('day', day)

    return make_class({'__init__':__init__, 'x' :0})#אם אני רוצה לשים משתנה סטטי})

def make_time_class():
    def __init__(self,hour,minuts):
        self['set']('hour',hour)
        self['set']('minuts',minuts)

    def __str__(self):
        x = str(self['get']('hour'))+ ':' +str( self['get']('minuts'))
        if self['get']('minuts') < 10:
            x = str(self['get']('hour'))+ ':' + '0' + str(self['get']('minuts'))
        if self['get']('hour')< 10:
            x = '0' + str(self['get']('hour')) + ':' + str(self['get']('minuts'))
        if self['get']('minuts') < 10 and self['get']('hour')< 10:
            x = '0' + str(self['get']('hour')) + ':' + '0' + str(self['get']('minuts'))
        return x

    return make_class({'__init__': __init__,'__str__':__str__})


def make_calentry_class():
    dic={}
    def __init__(self,year,mouth,day):
        Date=make_date_class()
        today=Date['new'](year,mouth,day)
        self['set']('Date',today)
        self['set']('year',year)
        #self['get']('Date')['get']('year')



    def addTask(self,name,timestart,timefinsh):
        tuple=(timestart['get']('__str__')(),timefinsh['get']('__str__')())
        x = self['get']('tasks')
        x[tuple] = name

        if tuple in dic:
            return False
        else:
            dic[tuple] =str(name)




    return make_class({'__init__':__init__,'addTask':addTask,'tasks':{},})






Date = make_date_class()
today = Date['new'](2017, 1, 20)
print(today['get']('x'))#להדפיס משתנה סטטי
print(today['get']('year'))
Time = make_time_class()
t = Time['new'](1,0)
print(t['get']('__str__')())
CalendarEntry = make_calentry_class()
todo = CalendarEntry['new'](2017, 1, 20)
todo['get']('addTask')("PPL lecture", t, Time['new'](13,0))
todo['get']('addTask')("PPL lecture", Time['new'](17,50), Time['new'](18,0))
print(todo['get']('tasks'))



