class Lesson:
    
    def __init__(self, date, time, description, duration, capacity, booked = 0, id = None):
        self.date = date
        self.time = time
        self.description = description
        self.duration = duration
        self.capacity = capacity
        self.booked = booked
        self.id = id