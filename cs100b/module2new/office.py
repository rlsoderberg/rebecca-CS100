from teacher import Teacher

class Office(Teacher):
    def __init__(self, building, name="unassigned", roomnumber=0):
        Office.__init__(self, building, name, roomnumber)