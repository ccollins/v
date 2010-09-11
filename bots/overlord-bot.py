import logging
from v import issue_order, finish_turn, parse_game_state
from planet_wars import Universe

"""
// The do_turn function is where your code goes. The universe object contains
// the state of the game, including information about all planets and fleets
// that currently exist. Inside this function, you issue orders using the
// issue_order function. For example, to send 10 ships from planet 3 to
// planet 8, you would say issue_order(3, 8, 10).
//
// There is already a basic strategy in place here. You can use it as a
// starting point, or you can throw it out entirely and replace it with your
// own. Check out the tutorials and articles on the contest website at
// http://www.ai-contest.com/resources.
"""

def do_turn(universe):
    # (1) If we currently have a fleet in flight, just do nothing.
    if len(universe.my_fleets()) >= 1:
        return
  
    # (2) Find my strongest planet.
    source = -1
    source_score = -999999.0
    source_num_ships = 0
    for p in universe.my_planets():
        score = float(p.num_ships)
    if score > source_score:
        source_score = score
        source = p._id
        source_num_ships = p.num_ships

    # (3) Find the weakest enemy or neutral planet.
    dest = -1
    dest_score = -999999.0
    for p in universe.other_planets():
        score = 1.0 / (1 + p.num_ships)
        if score > dest_score:
            dest_score = score
            dest = p._id

    # (4) Send half the ships from my strongest planet to the weakest
    # planet that I do not own.
    if source >= 0 and dest >= 0:
        num_ships = source_num_ships / 2
        issue_order(source, dest, num_ships)

def main():
    map_data = ''
    universe = Universe()
    while(True):
        current_line = raw_input()
        if len(current_line) >= 2 and current_line.startswith("go"):
            parse_game_state(universe, map_data)
            do_turn(universe)
            finish_turn()
            map_data = ''
        else:
            map_data += current_line + '\n'

if __name__ == '__main__':
  try:
    import psyco
    psyco.full()
  except ImportError:
    pass
    
  try:
    main()
  except KeyboardInterrupt:
    print 'Good-bye.  May the force be with you.'
