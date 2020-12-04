# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon: 
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

# class inherits from a parent class as an parameter

class Waypoint(LatLon): 
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
        
    # must add __str__ method in order to print a class unless
    # inheriting from a class that already implements it

    def __str__(self):
        return f'{self.name}, { self.lat}, {self.lon}'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

        # adding str to a child class with override the inheritied str 

    def __str__(self):
        return f"{super().__str__()} has difficulty {self.difficulty} and size {self.size}"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
# this is an instance of a class
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(geocache)


class Animal:
    name = ""
    kind = ""
    color = ""

    def description(self):
        return "%s is a %s %s." % (self.name, self.color, self.kind)

# Create instances of Animal here and modify the instance attributes
# as described above.


# YOUR CODE HERE
cat = Animal()
dog = Animal()
# Should print Purrfect is a brown cat.
print(cat.description())
# Should print Fido is a black dog.
print(dog.description())
