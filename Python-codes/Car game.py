started = False
while True:
    command = input('>').lower()
    if command == 'start':
        if started:
            print('Car has already started')
        else:
            started = True
            print('car has started')
    elif command == 'stop':
        if not started:
            print('car is already stopped')
        else:
            started = False
            print('car has stopped')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car 
quit - to quit''')
    elif command == 'quit':
        break
    else:
        print("sorry i don't understand this...")
