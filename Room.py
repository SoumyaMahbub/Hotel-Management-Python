class Room:
    def __init__(self, number, number_of_beds, bed_size, wifi):
        self.room_number = number
        self.number_of_beds = number_of_beds
        self.bed_size = bed_size 
        self.wifi = wifi

    def print(self):
        print(f"Room number: {self.room_number}, number of beds: {self.number_of_beds}, bed size: {self.bed_size}, wifi: {self.wifi}")
    
    def get_line(self):
        wifi_str = 'Y'
        if wifi_str == False:
            wifi_str = 'N'
        return f'{self.room_number},{self.number_of_beds},{self.bed_size},{wifi_str}'
