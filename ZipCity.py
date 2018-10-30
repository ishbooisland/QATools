# Zip to City, 04/21/2014
# Created by Darrin Long


import zips
import cities
import states
import stateabbrev
import cityandstate

list1 = []
list2 = []
from Tkinter import Tk


def convertstate(x, y):
    if states.states.get(y.upper().strip()) != None:
        state = states.states.get(y.upper().strip())
        city_state_lookup(x.upper().strip(), state.upper().strip())


def zip_state_lookup(x):
    global list1
    citystate = zips.zips[x[:5]].split(',')
    city = citystate[0]
    state = citystate[1]
    print "The zip code %s is in the city %s and state %s\n" % (x, city, state)
    sql = "\tWhen Zip = '%s' then '%s'" % (x, city)
    list1.append(sql)
    sqlst = "\tWhen Zip = '%s' then '%s'" % (x, state)
    list2.append(sqlst)
    start()


def city_state_lookup(x, y):
    if cityandstate.cityandstate.get('%s,%s' % (x, y)) != None:
        print "The zip codes for %s, %s are as follows:" % (x, y)
        for key, value in zips.zips.items():
            citystate = value.split(',')
            if citystate[0] == x and citystate[1] == y:
                print key
                continue
            else:
                continue
    else:
        print "There is no %s in %s" % (x, y)
    print '\n', start()


def start():
    global list1
    global list2
    print "Please type a city or zip code"
    entry = raw_input("> ")

    if entry.replace("-", "").isdigit() == True and zips.zips.get(entry[:5]) != None:
        zip_state_lookup(entry)

    elif entry.isdigit() == True and zips.zips.get(entry) == None:
        print 'The zip code %s does not exist\n' % entry
        start()

    elif entry == 'exit':
        exit(0)

    elif entry == 'sql':
        y = raw_input("Which Column? > ")
        if y.upper() == "CITY":
            x = Tk()
            x.withdraw()
            x.clipboard_clear()
            for i in list1:
                x.clipboard_append(i + '\n')
                print i
            start()
        elif y.upper() == 'STATE':
            x = Tk()
            x.withdraw()
            x.clipboard_clear()
            for i in list2:
                x.clipboard_append(i + '\n')
                print i
            start()
        else:
            print "That column is not supported :("
            start()

    elif entry == 'clear':
        list1 = []
        list2 = []
        start()

    elif entry.isdigit() == False and cities.cities.get(entry.upper().strip()) != None:
        state = raw_input("State? > ")

        if len(state.strip()) > 2 and states.states.get(state.upper().strip()) != None:
            convertstate(entry, state)

        elif len(state.strip()) > 2 and states.states.get(state.upper().strip()) == None:
            print "The state %s does not exist\n" % state.upper().strip()
            start()

        elif len(state.strip()) == 2 and stateabbrev.stateabbrev.get(state.upper().strip()) != None:
            city_state_lookup(entry.upper().strip(), state.upper().strip())

        else:
            print "The state %s does not exist\n" % state.upper().strip()
            start()

    elif entry.isdigit() == False and cities.cities.get(entry.upper().strip()) == None:
        print "The city %s does not exist\n" % entry.upper().strip()
        start()

    else:
        start()


print start()
