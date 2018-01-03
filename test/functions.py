
from Keys import *

def initial(flights):
    '''
    Iniliaziez flight list with items
    '''
    flights.append(['3244',43,'Cluj','London'])
    flights.append(['324',48,'Moscow','Bucharest'])
    flights.append(['6547',23,'Cluj','Budapest'])
    flights.append(['fds',93,'Cluj','Nyc'])
    flights.append(['f09ds',21,'Cluj','San Francisco'])
    flights.append(['aaa',90,'Moscow','Madrid'])
    flights.append(['jas',98,'Buchurest','Barcelona'])
    flights.append(['cda',73,'Cluj','Prague'])
    flights.append(['abc',64,'Moscow','Paris'])
    flights.append(['24',31,'Cluj','Berlin'])

def delete(code,flight):
    '''
    Deletes the flight with the given code
    by going through all the flights
    '''
    ln = len(flight)
    for i in range(0,ln):
        if flight[i][getCode()] == code:
            for j in range(i,ln-1):
                flight[j]=flight[j+1]
    flight.pop()


def show_dept(dept_city,flights):
    '''
    Shows all the flights from a given city
    '''
    newest= []
    for i in flights:
        if i[getDept()] == dept_city:
            newest.append(i)
    ln = len(newest)
    '''
    Sorts the city increasing by destination
    '''
    for i in range(0,ln):
        for j in range(i,ln):
            if newest[i][getDest()] > newest[j][getDest()]:
                aux = newest[i]
                newest[i] = newest[j]
                newest[j]= aux
    if len(newest) == 0:
        print("We don't have any flights from that city")
    else:
        print("From ",dept_city," we have this flights:")
        for i in newest:
            print("Code: ",i[getCode()],"\nDuration: ",i[getDur()],"\nDestination city: ",i[getDest()])

def addDelay(delay,dest_city,flights):
    '''
    Adds a given delay to all dept flighsts
    '''
    for i in flights:
        if i[getDept()] == dest_city:
            newdur = int(i[getDur()] + int(delay))
            i[getDur()] = newdur
    return flights

def searchCode(code,flights):
    '''
    Search if we have a code
    if we have the code return false
    '''
    for i in flights:
        if i[getCode()] == code:
            return False
    return True

def searchCity(city,flights):
    '''
    Search if we have a city
    if we have the code return false
    '''
    for i in flights:
        if i[getDept()] == city:
            return False
    return True

def case_1in(flights):
    '''
    Reads and verify all the date that we need for case 1
    '''
    ok = True
    code = duration = dep_city = dest_city = 0
    while ok:
        code = input("The flight code: ")
        if len(code) < 3:
            print("Invalid input")
        else:
            if searchCode(code,flights) == False:
                print("We already have that flight!")
            else:
                ok = False
    ok = True
    while ok:
        duration = input("Duration of the flight: ")
        ok = False
        try:
            int(duration)
        except ValueError:
            print("This must be a number!")
            ok = True
        if ok == False:
            if int(duration) < 20:
                print("Invalid input")
                ok= True
    ok = True
    while ok:
        dep_city = input("Departure city: ")
        if len(dep_city) > 2:
            ok = False
        else:
            print("Invalid input")
    ok = True
    while ok:
        dest_city = input("Destination city: ")
        if len(dest_city) > 2:
            ok = False
        else:
            print("Invalid input")
    return [code, int(duration), dep_city, dest_city]

def case_1(flights,fin):
    flights.append(fin)



def readDelay():
    '''
    Reads and verify the given delay time
    '''
    ok = True
    duration = 0
    while ok:
        duration = input("Duration of the delay: ")
        ok = False
        try:
            int(duration)
        except ValueError:
            print("This must be a number!")
            ok = True
        if ok == False:
            if int(duration) > 60 or int(duration) < 10:
                print("Invalid input")
                ok = True
    dept_city = input("The departure city: ")
    return duration,dept_city


def tests(flights):
    assert searchCode('abc',flights) == False
    delete('abc',flights)
    assert searchCity('Cluj',flights) == False
    assert len(flights) == 9 and searchCode('abc',flights) == True
    delete('fds', flights)
    delete('24', flights)
    assert len(flights) == 7 and searchCode('fds', flights) == True
    case_1(flights,['870',987,'iuyhiun','ghub'])
    case_1(flights,['0983',97,'fds','34'])
    case_1(flights,['420000a',54,'iuyhiun','ghub'])
    assert searchCode(870,flights)
    assert len(flights) == 10
