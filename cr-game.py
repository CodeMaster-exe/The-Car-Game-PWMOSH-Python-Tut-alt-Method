repeat = 0
started = False
while repeat < 1:
    cmd = input('>').lower()

    if cmd == 'start':
        if started:
            print('Car is already started!')
        else:
            print('Car started - Ready to go!')
            started = True
    elif cmd == 'stop':
        if not started:
            print('Car is already stopped!')
        else:
            started = False
            print('Car stopped.')

    elif cmd == 'help':
        print('''
        start - to start the car
        stop - to stop the car
        quit - to exit
                ''')
    elif cmd == 'quit':
        print('Car self destructed')
        break
    else:
        print('I do not understand that')




