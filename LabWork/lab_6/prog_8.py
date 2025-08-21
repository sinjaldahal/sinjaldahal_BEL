'''
8. Define a class Time with attributes hours, minutes, and seconds. Overload
the == operator to compare two Time objects for equality. Implement the
__eq__() method and test it by comparing two Time instances.
'''

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __eq__(self, other):
        return (self.hours == other.hours and 
                self.minutes == other.minutes and 
                self.seconds == other.seconds)
    
    def __str__(self):
        return f"Time({self.hours}:{self.minutes}:{self.seconds})"


t1 = Time(14, 30, 45)
t2 = Time(14, 30, 45)
t3 = Time(15, 20, 10)

print(f"t1: {t1}")
print(f"t2: {t2}")
print(f"t3: {t3}")
print(f"t1 == t2: {t1 == t2}")
print(f"t1 == t3: {t1 == t3}")