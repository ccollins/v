from sys import stdout

def issue_order(source_planet, destination_planet, num_ships):
    stdout.write("%d %d %d\n" % (source_planet, destination_planet, num_ships))
    stdout.flush()
   
def parse_game_state(universe, game_data):
    planets = []
    fleets = []
    planet_id = 0
    for line in s.split("\n"):
        line = line.split("#")[0] # remove comments
        tokens = line.split(" ")
        if len(tokens) == 1:
            continue
        elif tokens[0] == "P":
            if len(tokens) != 6:
                raise ParsingException("Invalid format in gamestate: '%s'" % line)
            #[1]x [2]y [3]owner [4]num-ships [5]growth-rate
            planets.append(Planet(planet_id, int(tokens[3]), int(tokens[4]), int(tokens[5]), float(tokens[1]), float(tokens[2])))
            planet_id += 1
        elif tokens[0] == "F":
            if len(tokens) != 7:
                raise ParsingException("Invalid format in gamestate: '%s'" % line)
            #[1]owner [2]num-ships [3]source [4]destination [5]total-trip-length [6]turns-remaining
            fleets.append(Fleet(int(tokens[1]), int(tokens[2]), int(tokens[3]), int(tokens[4]), int(tokens[5]), int(tokens[6])))
        else:
            raise ParsingException("Invalid format in gamestate: '%s'" % line)
    
    universe.update(planets, fleets)
    return 1
 
def finish_turn():
    stdout.write("go\n")
    stdout.flush()