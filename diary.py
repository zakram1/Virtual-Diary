import sys, time, requests, json

while True:
    time.sleep(0.7)
    print("------------------ Welcome to the main menu ------------------")
    time.sleep(0.7)
    print("(m) make a new entry \n(d) remove an entry \n(r) read an entry \n(q) quit")
    time.sleep(0.7)
    mainmenuinput = input("Select an option: ")
    if mainmenuinput == "m":
        print("Now, enter your diary entry name: ")
        first_entry = input("")
        print("Finally, enter your diary entry: ")
        second_entry = input("")
        geturl = 'http://127.0.0.1:8000/publishentry/'+first_entry
        getentryobj = {"DiaryName": first_entry, 
                       "DiaryEntries": second_entry}
        r = requests.post(geturl, json = getentryobj)
        if r.status_code == 200:
            print('..........')
            print('Entry added!')
        else:
            print('Error! Try again.')
    elif mainmenuinput == "d":
        print("Which entry would you like to delete?")
        remove_diary = input("")
        delurl = 'http://127.0.0.1:8000/removeentry/'+remove_diary
        getdelobj = {"DiaryName": remove_diary}
        r = requests.delete(delurl, json = getdelobj)
        if r.status_code == 200:
            print ('Entry deleted!')
        else:
            print ('Error! Try again.')
    elif mainmenuinput == "r":
        print("What is the name of the entry you would like to read?")
        read_diary = input("")
        readurl = 'http://127.0.0.1:8000/readentry/'+read_diary
        getreadobj = {"DiaryName": read_diary}
        r = requests.get(readurl, json = getreadobj)
        if r.status_code == 200:
            print ('Here is your entry!')
        else:
            print ('Error! Try again.')
        json_str = json.dumps(r.json(),
                              indent = 5)
        print(json_str)
    elif mainmenuinput == "q":
        print("Data saving...")
        sys.exit()      
    else:
        print("You did not select an option! Please try again")
        print("Rebooting menu... ")