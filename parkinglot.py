class Parking_lot:

    def __init__(self, size):
        self.size = size
        self.slots = [(0, 0)] * self.size

    def park_car(self, Registration_no, Color):

        Empty_slot = self.get_slot()
        if Empty_slot == -1:
            print("Parking space is full, no slots available!")
            return None
        self.slots[Empty_slot] = (Registration_no, Color)
        print(f"Please park your Car in slot number : {Empty_slot}")

    def Exit(self, Registration_no):
        for slot in range(self.size):
            if self.slots[slot][0] == Registration_no:
                self.slots[slot] = (0, 0)
                return slot

    def slot_of_car_by_Reg_no(self, Registration_no):

        for slot in range(self.size):
            if self.slots[slot][0] == Registration_no:
                print(
                    f"The Car with Registration number '{Registration_no}' is parked in slot no. {slot}")
                break
        else:
            print("There is no such car parked here")

    def slots_of_cars_by_color(self, Color):
        Same_colored_cars = []

        for i in range(self.size):
            if self.slots[i][1] == Color:
                Same_colored_cars.append(i)
        print(Same_colored_cars)
        print(
            f"The cars with color {Color} is present is following slots: {Same_colored_cars}")

    def get_slot(self):
        for slot in range(self.size):
            if self.slots[slot] == (0, 0):
                return slot
        else:
            return -1
