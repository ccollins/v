from math import ceil, sqrt

NEUTRAL = 0
MINE = 1
ENEMY = 2

class Fleet:
    def __init__(self, owner, num_ships, source_planet, destination_planet, total_trip_length, turns_remaining):
        self.owner = owner
        self.num_ships = num_ships
        self.source_planet = source_planet
        self.destination_planet = destination_planet
        self.total_trip_length = total_trip_length
        self.turns_remaining = turns_remaining

    def __repr__(self):
        return "<Fleet owner:%d num_ships:%d source_planet:%d destination_planet:%d total_trip_length:%d turns_remaining:%d>" % \
                (self.owner, self.num_ships, self.source_planet, self.destination_planet, self.total_trip_length, self.turns_remaining)
        
class Planet:
    def __init__(self, planet_id, owner, num_ships, growth_rate, x, y):
        self._id = planet_id
        self.owner = owner
        self.num_ships = num_ships
        self.growth_rate = growth_rate
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Planet x:%f y:%f owner:%d num_ships:%d growth_rate:%d>" % (self.x, self.y, self.owner, self.num_ships, self.growth_rate)
        
    def add_ships(self, amount):
        self.num_ships += amount

    def remove_ships(self, amount):
        if self.num_ships < amount:
            raise Exception('Cannot remove %i ships, not enough on planet (%i)', amount, self.num_ships)
        self.num_ships -= amount
        
class Universe:
    def __init__(self):
        self.planets = {}
        self.fleets = []

    def __repr__(self):
        return reduce(lambda x,y: "%s%s\n" % (x, y), self.planets.values(), '') + reduce(lambda x,y: "%s%s\n" % (x, y), self.fleets, '')
        
    def update(planets, fleets):
        map(lambda x:self.add_planet(x), planets)
        map(lambda x:self.add_fleet(x), fleets)
        
    def is_alive(self, player_id):
        for p in self.planets.values():
            if p.owner == player_id:
                return True
        for f in self.fleets:
            if f.owner == player_id:
                return True
        return False
        
    @property
    def num_planets(self):
        return len(self.planets)
        
    def add_planet(self, planet):
        if self.planets.has_key(planet._id):
            raise Exception('Planet already exists in the universe')
        self.planets[planet._id] = planet

    def get_planet(self, planet_id):
        return self.planets[planet_id]
        
    def my_planets(self):
        return filter(lambda x: x.owner == MINE, self.planets.values())

    def neutral_planets(self):
        return filter(lambda x: x.owner == NEUTRAL, self.planets.values())
        
    def enemy_planets(self):
        return filter(lambda x: x.owner >= ENEMY, self.planets.values())
        
    def other_planets(self):
        return filter(lambda x: x.owner != MINE, self.planets.values())
                
    @property
    def num_fleets(self):
        return len(self.fleets)
        
    def add_fleet(self, fleet):
        self.fleets.append(fleet)

    def my_fleets(self):
        return filter(lambda x: x.owner == MINE, self.fleets)
        
    def enemy_fleets(self):
        return filter(lambda x: x.owner >= ENEMY, self.fleets)

    def distance(self, p1, p2):
        p1 = self.get_planet(p1)
        p2 = self.get_planet(p2)
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        return int(ceil(sqrt(dx * dx + dy * dy)))