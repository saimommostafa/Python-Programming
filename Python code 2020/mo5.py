a = ""
started = True
while True:
    a = raw_input("-> ").lower()
    if a == 'start':
        if started:
            print 'Car started.'
            started = False
        else:
            print 'Car is already started.'
        
    elif a == 'stop':
        if started:
            print 'Car is already stopped.'
        else:
            print "Car stopped."
            started = True
    
    elif a == 'help':
        print'''
start - to start the car 
stop - to stop the car
quit - to exit '''
            
    elif a == 'quit':
        break  
    else:
        print "I don't understand that..."
