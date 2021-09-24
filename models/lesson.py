class Lesson:
    
    def __init__(self, date, time, description, duration, level, capacity, id = None):
        self.date = date
        self.time = time
        self.description = description
        self.duration = duration
        self.level = level
        self.capacity = capacity
        self.id = id