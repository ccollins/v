from planet_wars import Fleet, Planet, Universe
from uuid import UUID
import unittest
        
class TestFleet(unittest.TestCase):
    def test_init_should_not_fail(self):
        fleet = Fleet(1, 10, 2, 3, 50, 10)
        self.assertEqual(fleet.owner, 1)
        self.assertEqual(fleet.num_ships, 10)
        self.assertEqual(fleet.source_planet, 2)
        self.assertEqual(fleet.destination_planet, 3)
        self.assertEqual(fleet.total_trip_length, 50)
        self.assertEqual(fleet.turns_remaining, 10)
    
class TestPlanet(unittest.TestCase):
    def setUp(self):
        self.planet = Planet(0, 1, 10, 5, 10, 10)
        
    def test_init_should_not_fail(self):
        self.assertEqual(self.planet._id, 0)
        self.assertEqual(self.planet.owner, 1)
        self.assertEqual(self.planet.num_ships, 10)
        self.assertEqual(self.planet.growth_rate, 5)
        self.assertEqual(self.planet.x, 10)
        self.assertEqual(self.planet.y, 10)
        
    def test_should_add_ships(self):
        self.planet.add_ships(10)
        self.assertEqual(self.planet.num_ships, 20)
        
    def test_should_remove_ships(self):
        self.planet.remove_ships(5)
        self.assertEqual(self.planet.num_ships, 5)
        
    def test_should_fail_when_removing_too_many_ships(self):
        self.assertRaises(Exception, lambda: self.planet.remove_ships(20))
        
class TestUniverse(unittest.TestCase):
    def setUp(self):
        self.universe = Universe()
        self.neutral_planet = Planet(0, 0, 10, 5, 10, 20)
        self.my_planet = Planet(1, 1, 10, 5, 10, 10)
        self.enemy_planet = Planet(2, 2, 10, 5, 10 , 30)
        self.my_fleet = Fleet(1, 10, 2, 3, 50, 10)
        self.enemy_fleet = Fleet(2, 10, 2, 3, 50, 10)
        
    def test_init_should_not_fail(self):
        self.assertEqual(self.universe.planets, {})
        self.assertEqual(self.universe.fleets, [])
        
    def test_to_string(self):
        self.universe.add_planet(self.my_planet)
        self.universe.add_fleet(self.my_fleet)
        self.assertEqual(str(self.universe), '<Planet x:10.000000 y:10.000000 owner:1 num_ships:10 growth_rate:5>\n<Fleet owner:1 num_ships:10 source_planet:2 destination_planet:3 total_trip_length:50 turns_remaining:10>\n')
        
    def test_num_planets_should_be_zero(self):
        self.assertEqual(self.universe.num_planets, 0)
        
    def test_should_add_planet(self):
        self.universe.add_planet(self.my_planet)
        self.assertEqual(self.universe.num_planets, 1)
        
    def test_should_get_planet(self):
        self.universe.add_planet(self.my_planet)
        planet = self.universe.get_planet(self.my_planet._id)
        self.assertEqual(planet._id, self.my_planet._id)
        
    def test_get_planet_should_raise_key_error(self):
        self.assertRaises(KeyError, lambda:self.universe.get_planet('adsfasdf'))
        
    def test_should_fail_if_adding_planet_more_than_once(self):
        self.universe.add_planet(self.my_planet)
        self.assertRaises(Exception, lambda: self.universe.add_planet(self.my_planet))
    
    def test_my_planets_should_return_planet(self):
        self.universe.add_planet(self.my_planet)
        planets = self.universe.my_planets()
        self.assertEqual(len(planets), 1)
        self.assertEqual(planets[0]._id, self.my_planet._id)
        
    def test_my_planets_should_return_empty_list(self):
        self.universe.add_planet(self.neutral_planet)
        planets = self.universe.my_planets()
        self.assertEqual(len(planets), 0)
        
    def test_neutral_planets_should_return_planet(self):
        self.universe.add_planet(self.neutral_planet)
        planets = self.universe.neutral_planets()
        self.assertEqual(len(planets), 1)
        
    def test_neutral_planets_should_return_empty_list(self):
        self.universe.add_planet(self.my_planet)
        planets = self.universe.neutral_planets()
        self.assertEqual(len(planets), 0)
        
    def test_enemy_planets_should_return_planet(self):
        self.universe.add_planet(self.enemy_planet)
        planets = self.universe.enemy_planets()
        self.assertEqual(len(planets), 1)
        
    def test_enemy_planets_should_return_empty_list(self):
        self.universe.add_planet(self.my_planet)
        planets = self.universe.enemy_planets()
        self.assertEqual(len(planets), 0)
        
    def test_other_planets_should_return_planets(self):
        self.universe.add_planet(self.enemy_planet)
        self.universe.add_planet(self.neutral_planet)
        planets = self.universe.other_planets()
        self.assertEqual(len(planets), 2)
        
    def test_other_planets_should_return_empty_list(self):
        self.universe.add_planet(self.my_planet)
        planets = self.universe.other_planets()
        self.assertEqual(len(planets), 0)
        
    def test_num_fleets_should_be_zero(self):
        self.assertEqual(self.universe.num_fleets, 0)
        
    def test_should_add_fleet(self):
        self.universe.add_fleet(self.my_fleet)
        self.assertEqual(self.universe.num_fleets, 1)
        
    def test_my_fleets_should_return_fleet(self):
        self.universe.add_fleet(self.my_fleet)
        fleets = self.universe.my_fleets()
        self.assertEqual(len(fleets), 1)
        
    def test_my_fleets_should_return_empty_list(self):
        self.universe.add_fleet(self.enemy_fleet)
        fleets = self.universe.my_fleets()
        self.assertEqual(len(fleets), 0)
        
    def test_enemy_fleets_should_return_fleet(self):
        self.universe.add_fleet(self.enemy_fleet)
        fleets = self.universe.enemy_fleets()
        self.assertEqual(len(fleets), 1)
        
    def test_enemy_fleets_should_return_empty_list(self):
        self.universe.add_fleet(self.my_fleet)
        fleets = self.universe.enemy_fleets()
        self.assertEqual(len(fleets), 0)
        
    def test_distance(self):
        p1 = Planet(0, 1, 10, 5, 10, 10)
        p2 = Planet(1, 1, 10, 5, 10, 30)
        self.universe.add_planet(p1)
        self.universe.add_planet(p2)
        self.assertEqual(self.universe.distance(p1._id, p2._id), 20)
            
    def test_is_alive_should_return_true_with_planet(self):
        self.universe.add_planet(self.my_planet)
        self.assertTrue(self.universe.is_alive(1))
        
    def test_is_alive_should_return_true_with_fleet(self):
        self.universe.add_fleet(self.my_fleet)
        self.assertTrue(self.universe.is_alive(1))
        
    def test_is_alive_should_return_false(self):
        self.universe.is_alive(1)