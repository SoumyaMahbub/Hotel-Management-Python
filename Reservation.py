from datetime import datetime

class Reservation():
    def __init__(self, number, date, guest_name):
        self.room_number = number
        self.date = date
        self.guest_name = guest_name

    def get_line(self):
        line = f'{self.room_number},{datetime.strftime(self.date, "%d.%m.%Y")},{self.guest_name}'
        return line
    