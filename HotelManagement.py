from Room import Room
from Reservation import Reservation
from datetime import datetime

def write_rooms(rooms):
    f = open('Hotel Management/rooms.txt', 'w+')
    number_of_elements = len(rooms)
    i = 1
    for room in rooms:
        line = room.get_line()
        if i != number_of_elements:
            line = line + '\n'
        f.write(line)
        i += 1
    f.close()

def read_rooms():
    f = open('Hotel Management/rooms.txt', 'r+')
    rooms = []
    for line in f.readlines():
        parts = line.strip().split(',')
        room = Room(int(parts[0]), int(parts[1]), parts[2], parts[3] == 'Y')
        rooms.append(room)
    f.close()
    return rooms

def read_reservations():
    r = open('Hotel Management/reservations.txt', 'r+')
    reservations = []
    for rline in r.readlines():
        rparts = rline.strip().split(',')
        reserved_room = Reservation(int(rparts[0]), datetime.strptime(rparts[1], '%d.%m.%Y'), rparts[2])
        reservations.append(reserved_room)
    r.close()
    return reservations

def write_reservations(reservations):
    r = open('Hotel Management/reservations.txt', 'w+')
    number_of_elements = len(reservations)
    i = 1
    for reservation in reservations:
        line = reservation.get_line()
        if i != number_of_elements:
            line = line + '\n'
        r.write(line)
        i += 1
    r.close()

def room_exists(room_number, existing_rooms):
    for room in existing_rooms:
        if room.room_number == room_number:
            return True
    return False

def room_reserved_on_date(room_number, date, reservations):
    for reservation in reservations:
        if reservation.room_number == room_number and reservation.date == date:
            return True
    return False

while True:

    print('--------------------')
    print('MAIN MENU')
    print('--------------------')
    print('1) List all rooms')
    print('2) Reserve a room')
    print('3) List unoccupied rooms')
    print('4) Show reserved rooms')
    print('5) Create room')
    print('6) Cancel reservation')
    print('7) Exit')
    print('--------------------')
    val = input("Enter an option and press enter: ")
    options = ["1", "2", "3", "4", "5", "6", "7"]

    if val in options:

        rooms = read_rooms()
        reservations = read_reservations()

        #list all rooms
        if val == "1":    
            print('
            ')  
            print('--------------------')
            print('LIST OF ROOMS')
            print('--------------------')
            for room in rooms:
                room.print()
        
        #reserve a room2
        elif val == "2":

            reserve_room_number = input("Which room would you like to reserve?: ")

            while True:
                if reserve_room_number.isdigit() == False:
                    reserve_room_number = input("Please enter a valid integer: ")
                else:
                    if not room_exists(int(reserve_room_number), rooms):
                        reserve_room_number = input("The room doesn't exist. Try another room: ")
                    else:
                        reserve_room_number = int(reserve_room_number)
                        break
            
            reserve_date = input("Which date would you like to reserve it?(DD.MM.YYYY): ")

            while True:
                try:
                    date = datetime.strptime(reserve_date, '%d.%m.%Y')
                    if room_reserved_on_date(reserve_room_number, date, reservations):
                        reserve_date = input("The room is already reserved at that day. Try another date (DD.MM.YYYY): ")
                    else:
                        break
                except:
                    reserve_date = input("Please enter valid date format (DD.MM.YYYY): ")

            reserve_guest = input("What is the guest's name: ")
            while True:
                if reserve_guest == "" or len(reserve_guest) < 2:
                    reserve_date = input("Please type a valid name: ")
                else:
                    reservations.append(Reservation(reserve_room_number, datetime.strptime(reserve_date, '%d.%m.%Y'), reserve_guest))
                    write_reservations(reservations)
                    print('Room reserved successfully\n\n')
                    break 
                    
        #show unoccupied rooms
        elif val == "3":

            unocc_date = input("Which date would you like to see? : ")
            while True:
                try:
                    unocc_date = datetime.strptime(unocc_date, '%d.%m.%Y') 
                    for room in rooms:
                        reserved = False
                        for reservation in reservations:
                            if room.room_number == reservation.room_number and reservation.date == unocc_date:
                                reserved = True
                        if reserved == False:
                            room.print()
                    break
                except:
                    unocc_date = input("Please enter a valid date : ")  

        #show reserved rooms
        elif val == "4":
            print("\n")
            for reservation in reservations:
                print(reservation.get_line())
            print("\n")

        #creating room
        elif val == "5":
            
            #enter new room number
            room_val = input("Enter room number: ")

            while True:
                error_message = "You haven't entered a valid number, try again: "
                if room_val.isdigit() == True:
                    if not room_exists(int(room_val), rooms):
                        break
                    else:
                        error_message = "Room already exists, try again: "
                room_val = input(error_message)
            
            #enter bed number
            room_bedval = input("Enter bed number: ")

            while True:
                if room_bedval.isdigit() == True:
                    break
                room_bedval = input("You haven't entered a valid number, try again: ")
            #enter bed size 
            room_bedsize = input("Enter bed size: ").upper()

            bed_sizes = ['K', 'Q', 'D', 'S']
            while room_bedsize not in bed_sizes:
                room_bedsize = input("You have to enter a valid bed size (K, Q, S, D), try again: ").upper()
            
            #enter wifi availabilty
            room_wifi = input("Enter wifi availability (Y/N): ").upper()

            room_wifi_options = ['Y', 'N']
            while room_wifi not in room_wifi_options:
                room_wifi = input("You have to enter a valid value (Y/N), try again: ").upper()
            
            rooms.append(Room(room_val, room_bedval, room_bedsize, room_wifi == 'Y'))
            write_rooms(rooms)
            print("Room added successfully")

        #cancel reservation
        elif val == "6":
            cancel_room = input("Which room would you like to cancel reservation?: ")

            while True:
                if(cancel_room.isdigit() == False):
                    cancel_room = input("Please enter a number: ")
                else:
                    if(room_exists(int(cancel_room), rooms) == False):
                        cancel_room = input("The room doesn't exist. Try again: ")
                    else:
                        if(room_exists(int(cancel_room), reservations) == False):
                            cancel_room = input("The room hasn't been reserved. Try again: ")
                        else:
                            break
                                        
            cancel_date = input(f"Which date would you like to cancel reservation of room number {cancel_room}?: ")                

            while True:

                # try:
                cancel_date = datetime.strptime(cancel_date, '%d.%m.%Y')
                if (room_reserved_on_date(int(cancel_room), cancel_date, reservations) == False):
                    cancel_date = input(f"Room number {cancel_room} is not reserved on that date. Try another date: ")
                else:
                    # Create a new array of reservations.
                    new_reservations = []

                    # Search for the reservatons in `reservations` array to keep.
                    for reservation in reservations:
                        if reservation.room_number != int(cancel_room) or reservation.date != cancel_date:
                            new_reservations.append(reservation)

                    # Write the new array of reservations in the file.
                    write_reservations(new_reservations)
                    print('Reservation cancelled successfully')
                    break
                # except:
                #     cancel_date = input("Please enter a valid date : ")


        #exit
        elif val == "7":
            exit() 

    else:
        print("Incorrect input.")


