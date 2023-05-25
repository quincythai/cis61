"""The ants module implements game logic for Ants Vs. SomeBees."""

# Name: Quincy Thai
# Email: quincythai50@icloud.com

import random
import sys
from ucb import main, interact, trace
from collections import OrderedDict


################
# Core Classes #
################


class Place:
    """A Place holds insects and has an exit to another Place."""

    def __init__(self, name, exit=None):
        """Create a Place with the given exit.

        name -- A string; the name of this Place.
        exit -- The Place reached by exiting this Place (may be None).
        """
        self.name = name
        self.exit = exit
        self.bees = []        # A list of Bees
        self.ant = None       # An Ant
        self.entrance = None  # A Place
        # Phase 1: Add an entrance to the exit
        
        # A newly created Place always starts with its entrance as None.
        #   DONE: self.entrance = None (above)

        # If the Place has an exit, then the exit's entrance is set to that Place.
        # NOTE: exit is a place object, and therefore has its own entrance
        if self.exit is not None:
            self.exit.entrance = self # self is the place object

    def add_insect(self, insect):
        """Add an Insect to this Place.

        There can be at most one Ant in a Place, unless exactly one of them is
        a BodyguardAnt (Phase 2), in which case there can be two. If add_insect
        tries to add more Ants than is allowed, an assertion error is raised.

        There can be any number of Bees in a Place.
        """

        # can_contain checks if ant is container, ant does not already contain another ant,
        # or other ant is not a container

        if insect.is_ant():
            other_ant = insect
            # Phase 2: Special handling for BodyguardAnt
            if self.ant: # self.ant refers to ant currently occuping this place
                if self.ant.can_contain(other_ant): # if THIS ant can contain
                    self.ant.contain_ant(other_ant)
                elif other_ant.can_contain(self.ant): # if OTHER ant can contain
                    other_ant.contain_ant(self.ant)
                    self.ant = other_ant # set this place's ant to new ant
                else: # neither Ant can contain the other
                    assert self.ant is None, 'Two ants in {0}'.format(self)
            else: # self.ant is None
                self.ant = other_ant # simply set this place's ant to other ant
        else: # insect is NOT an Ant (Bee)
            self.bees.append(insect)

        insect.place = self # ant or bee occupies the space now

    def remove_insect(self, insect):
        """Remove an Insect from this Place."""

        # Cannot remove True Queen
        if isinstance(insect, QueenAnt) and insect.imposter is False:
            return

        if not insect.is_ant():
            self.bees.remove(insect)
        else:
            assert self.ant == insect, '{0} is not in {1}'.format(insect, self)

            # If THIS ant is a bodyguard
            if hasattr(self.ant, "container") and self.ant.container is True:
                self.ant = self.ant.ant # replace it with the other ant
            else:
                # This ant is not the bodyguard
                self.ant = None

        insect.place = None


    def __str__(self):
        return self.name


class Insect:
    """An Insect, the base class of Ant and Bee, has armor and a Place."""

    # watersafe is attribute for Insects to be deployed in Water places.
    watersafe = False


    def __init__(self, armor, place=None):
        """Create an Insect with an armor amount and a starting Place."""
        self.armor = armor
        self.place = place  # set by Place.add_insect and Place.remove_insect


    def reduce_armor(self, amount):
        """Reduce armor by amount, and remove the insect from its place if it
        has no armor remaining.

        >>> test_insect = Insect(5)
        >>> test_insect.reduce_armor(2)
        >>> test_insect.armor
        3
        """
        self.armor -= amount
        if self.armor <= 0:
            print('{0} ran out of armor and expired'.format(self))
            self.place.remove_insect(self)

    def action(self, colony):
        """Perform the default action that this Insect takes each turn.

        colony -- The AntColony, used to access game state information.
        """

    def is_ant(self):
        """Return whether this Insect is an Ant."""
        return False

    def __repr__(self):
        cname = type(self).__name__
        return '{0}({1}, {2})'.format(cname, self.armor, self.place)


class Bee(Insect):
    """A Bee moves from place to place, following exits and stinging ants."""

    watersafe = True

    name = 'Bee'

    def sting(self, ant):
        """Attack an Ant, reducing the Ant's armor by 1."""
        ant.reduce_armor(1)

    def move_to(self, place):
        """Move from the Bee's current Place to a new Place."""
        self.place.remove_insect(self)
        place.add_insect(self)

    def blocked(self):
        """Return True if this Bee cannot advance to the next Place."""
        # Phase 2: Special handling for NinjaAnt
        if self.place.ant is None or self.place.ant.blocks_path == False:
            return False
        else:
            return True

    def action(self, colony):
        """A Bee's action stings the Ant that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.

        colony -- The AntColony, used to access game state information.
        """
        if self.blocked():
            self.sting(self.place.ant)
        else:
            if self.place.name != 'Hive' and self.armor > 0:
                self.move_to(self.place.exit)


class Ant(Insect):
    """An Ant occupies a place and does work for the colony."""

    implemented = False  # Only implemented Ant classes should be instantiated
    damage = 0
    food_cost = 0

    container = False

    blocks_path = True

    def __init__(self, armor=1):
        """Create an Ant with an armor quantity."""
        Insect.__init__(self, armor)

    def is_ant(self):
        return True

    # Conditions:
    # This ant is a container.
    # This ant does not already contain another ant.
    # The other ant is not a container.
    def can_contain(self, ant): # self.container refers to atribute in Ant class
        # self.ant.container doesn't work bc. Ant class doesn't have ant attribute
        return self.container is True and self.ant is None and ant.container is False


class HarvesterAnt(Ant):
    """HarvesterAnt produces 1 additional food per turn for the colony."""

    name = 'Harvester'
    implemented = True

    food_cost = 2
    # No need to set armor=1 because inherits from parent class's constructor

    def action(self, colony):
        """Produce 1 additional food for the colony.

        colony -- The AntColony, used to access game state information.
        """

        # do not need self.colony because self is automatically passed as argument
        # for instance methods
        colony.food += 1

def random_or_none(l):
    """Return a random element of list l, or return None if l is empty."""
    return random.choice(l) if l else None


class ThrowerAnt(Ant):
    """ThrowerAnt throws a leaf each turn at the nearest Bee in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1

    food_cost = 4

    # Default ranges
    min_range = 0
    max_range = 10
    # No need to set armor=1 because inherits from parent class's constructor

    # Takes into account min and max ranges of the instance of objects
    def nearest_bee(self, hive):
        """Return the nearest Bee in a Place that is not the Hive, connected to
        the ThrowerAnt's Place by following entrances.

        This method returns None if there is no such Bee.

        Problem B5: This method returns None if there is no Bee in range.
        """

        place = self.place  # Bind starting place of ant to a varaible to use in loop
        bees = None          # bees is a list to hold all bees in range
        distance_traveled = 0       # initialize a counter for distance traveled

        # loop continues while bees is empty (None) AND not inside the hive
        while not bees and place != hive:
            # check if the distance_traveled is within the ant's range
            if self.min_range <= distance_traveled <= self.max_range: 
                bees = place.bees   # get all bees at the current Place object
            place = place.entrance  # move to the next Place object
            distance_traveled += 1
        return random_or_none(bees)   # return a random bee within range or None if there are no bees

    def throw_at(self, target):
        """Throw a leaf at the TARGET Bee, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a leaf at the nearest Bee in range."""
        self.throw_at(self.nearest_bee(colony.hive))

    def throw_at(self, target):
        """Throw a leaf at the target Bee, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a leaf at the nearest Bee in range."""
        self.throw_at(self.nearest_bee(colony.hive))


class Hive(Place):
    """The Place from which the Bees launch their assault.

    assault_plan -- An AssaultPlan; when & where bees enter the colony.
    """

    name = 'Hive'

    def __init__(self, assault_plan):
        self.name = 'Hive'
        self.assault_plan = assault_plan
        self.bees = []
        for bee in assault_plan.all_bees:
            self.add_insect(bee)
        # The following attributes are always None for a Hive
        self.entrance = None
        self.ant = None
        self.exit = None

    def strategy(self, colony):
        exits = [p for p in colony.places.values() if p.entrance is self]
        for bee in self.assault_plan.get(colony.time, []):
            bee.move_to(random.choice(exits))


class AntColony:
    """An ant collective that manages global game state and simulates time.

    Attributes:
    time -- elapsed time
    food -- the colony's available food total
    queen -- the place where the queen resides
    places -- A list of all places in the colony (including a Hive)
    bee_entrances -- A list of places that bees can enter
    """
    def __init__(self, strategy, hive, ant_types, create_places, food=2):
        """Create an AntColony for simulating a game.

        Arguments:
        strategy -- a function to deploy ants to places
        hive -- a Hive full of bees
        ant_types -- a list of ant constructors
        create_places -- a function that creates the set of places
        """
        self.time = 0
        self.food = food
        self.strategy = strategy
        self.hive = hive
        self.ant_types = OrderedDict((a.name, a) for a in ant_types)
        self.configure(hive, create_places)

    def configure(self, hive, create_places):
        """Configure the places in the colony."""
        self.queen = Place('AntQueen')
        self.places = OrderedDict()
        self.bee_entrances = []
        def register_place(place, is_bee_entrance):
            self.places[place.name] = place
            if is_bee_entrance:
                place.entrance = hive
                self.bee_entrances.append(place)
        register_place(self.hive, False)
        create_places(self.queen, register_place)

    def simulate(self):
        """Simulate an attack on the ant colony (i.e., play the game)."""
        while len(self.queen.bees) == 0 and len(self.bees) > 0:
            self.hive.strategy(self)    # Bees invade
            self.strategy(self)         # Ants deploy
            for ant in self.ants:       # Ants take actions
                if ant.armor > 0:
                    ant.action(self)
            for bee in self.bees:       # Bees take actions
                if bee.armor > 0:
                    bee.action(self)
            self.time += 1
        if len(self.queen.bees) > 0: # Bee's have killed the queen and you lose
            print('The ant queen has perished. Please try again.')
        else:
            print('All bees are vanquished. You win!')

    def deploy_ant(self, place_name, ant_type_name):
        """Place an ant if enough food is available.

        This method is called by the current strategy to deploy ants.
        """
        constructor = self.ant_types[ant_type_name]
        if self.food < constructor.food_cost:
            print('Not enough food remains to place ' + ant_type_name)
        else:
            self.places[place_name].add_insect(constructor())
            self.food -= constructor.food_cost

    def remove_ant(self, place_name):
        """Remove an Ant from the Colony."""
        place = self.places[place_name]
        if place.ant is not None:
            place.remove_insect(place.ant)

    @property
    def ants(self):
        return [p.ant for p in self.places.values() if p.ant is not None]

    @property
    def bees(self):
        return [b for p in self.places.values() for b in p.bees]

    @property
    def insects(self):
        return self.ants + self.bees

    def __str__(self):
        status = ' (Food: {0}, Time: {1})'.format(self.food, self.time)
        return str([str(i) for i in self.ants + self.bees]) + status

def ant_types():
    """Return a list of all implemented Ant classes."""
    all_ant_types = []
    new_types = [Ant]
    while new_types:
        new_types = [t for c in new_types for t in c.__subclasses__()]
        all_ant_types.extend(new_types)
    return [t for t in all_ant_types if t.implemented]

def interactive_strategy(colony):
    """A strategy that starts an interactive session and lets the user make
    changes to the colony.

    For example, one might deploy a ThrowerAnt to the first tunnel by invoking:
    colony.deploy_ant('tunnel_0_0', 'Thrower')
    """
    print('colony: ' + str(colony))
    msg = '<Control>-D (<Control>-Z <Enter> on Windows) completes a turn.\n'
    interact(msg)

def start_with_strategy(args, strategy):
    """Reads command-line arguments and starts Ants vs. SomeBees with those
    options."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Ants vs. SomeBees")
    parser.add_argument('-t', '--ten', action='store_true',
                        help='start with ten food')
    parser.add_argument('-f', '--full', action='store_true',
                        help='loads a full layout and assault plan')
    parser.add_argument('-w', '--water', action='store_true',
                        help='loads a full layout with water')
    parser.add_argument('-i', '--insane', action='store_true',
                        help='loads a difficult assault plan')
    args = parser.parse_args()

    assault_plan = make_test_assault_plan()
    layout = test_layout
    food = 2
    if args.ten:
        food = 10
    if args.full:
        assault_plan = make_full_assault_plan()
        layout = dry_layout
    if args.water:
        layout = mixed_layout
    if args.insane:
        assault_plan = make_insane_assault_plan()
    hive = Hive(assault_plan)
    AntColony(strategy, hive, ant_types(), layout, food).simulate()


###########
# Layouts #
###########

def mixed_layout(queen, register_place, length=8, tunnels=3, moat_frequency=3):
    """Register Places with the colony."""
    for tunnel in range(tunnels):
        exit = queen
        for step in range(length):
            if moat_frequency != 0 and (step + 1) % moat_frequency == 0:
                exit = Water('water_{0}_{1}'.format(tunnel, step), exit)
            else:
                exit = Place('tunnel_{0}_{1}'.format(tunnel, step), exit)
            register_place(exit, step == length - 1)

def test_layout(queen, register_place, length=8, tunnels=1):
    mixed_layout(queen, register_place, length, tunnels, 0)

def test_layout_multi_tunnels(queen, register_place, length=8, tunnels=2):
    mixed_layout(queen, register_place, length, tunnels, 0)

def dry_layout(queen, register_place, length=8, tunnels=3):
    mixed_layout(queen, register_place, length, tunnels, 0)


#################
# Assault Plans #
#################


class AssaultPlan(dict):
    """The Bees' plan of attack for the Colony.  Attacks come in timed waves.

    An AssaultPlan is a dictionary from times (int) to waves (list of Bees).

    >>> AssaultPlan().add_wave(4, 2)
    {4: [Bee(3, None), Bee(3, None)]}
    """

    def __init__(self, bee_armor=3):
        self.bee_armor = bee_armor

    def add_wave(self, time, count):
        """Add a wave at time with count Bees that have the specified armor."""
        bees = [Bee(self.bee_armor) for _ in range(count)]
        self.setdefault(time, []).extend(bees)
        return self

    @property
    def all_bees(self):
        """Place all Bees in the hive and return the list of Bees."""
        return [bee for wave in self.values() for bee in wave]

def make_test_assault_plan():
    return AssaultPlan().add_wave(2, 1).add_wave(3, 1)

def make_full_assault_plan():
    plan = AssaultPlan().add_wave(2, 1)
    for time in range(3, 15, 2):
        plan.add_wave(time, 1)
    return plan.add_wave(15, 8)

def make_insane_assault_plan():
    plan = AssaultPlan(4).add_wave(1, 2)
    for time in range(3, 15):
        plan.add_wave(time, 1)
    return plan.add_wave(15, 20)



##############
# Extensions #
##############


class Water(Place):
    """Water is a place that can only hold 'watersafe' insects."""

    def add_insect(self, insect):
        """Add insect if it is watersafe, otherwise reduce its armor to 0."""
        print('added', insect, insect.watersafe)

        #First call Place.add_insect to add the insect, regardless of whether it is watersafe. 
        # if the insect not watersafe, reduce the insect's armor to 0 by using reduce_armor.

        # call parent's (Place) class method (add_insect)
        # could also use super().add_insect(insect)

        Place.add_insect(self, insect)
        if insect.watersafe is False:
            insect.reduce_armor(insect.armor) # reduce_armor(self, number of damage)


class FireAnt(Ant):
    """FireAnt cooks any Bee in its Place when it expires."""

    # class level attributes do not use self keyword
    # they apply to all instances of the class
    name = 'Fire'
    damage = 3

    food_cost = 4
    # armor already initialized to 1

    implemented = True

    def reduce_armor(self, amount):
        # use self keyword because want to modify attribute specific to particular instance
        self.armor -= amount
        if self.armor <= 0:
            bee_list = self.place.bees[:] # make a copy to avoid errors while modding
            for bee in bee_list:
                bee.reduce_armor(self.damage)
            self.place.remove_insect(self) # self refers to the FireAnt instance itself




class LongThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at least 4 places away."""

    implemented = True
    name = 'Long'

    food_cost = 3

    # Only throws from 4 to infinity
    # I modified throwing function in ThrowerAnt to account for ranges
    min_range = 4 
    max_range = float('inf') 


class ShortThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees within 3 places."""

    implemented = True
    name = 'Short'

    # Only throws from 0 to 3
    food_cost = 3
    min_range = 0
    max_range = 3



class WallAnt(Ant):
    """WallAnt is an Ant which has a large amount of armor."""

    name = 'Wall'
    food_cost = 4

    implemented = True

    # set armor to 4 by using parent init, passing armor value of 4,
    # which will in turn call THAT parent's init, setting armor to 4.
    def __init__(self):
        Ant.__init__(self, armor=4)



class NinjaAnt(Ant):
    """NinjaAnt is an Ant which does not block the path and does 1 damage to
    all Bees in the exact same Place."""

    name = 'Ninja'
    blocks_path = False
    implemented = True

    food_cost = 6
    damage = 1

    # reduce armor of all Bees in the same place as the NinjaAnt by 1, 
    # Overrides default action method in Ant parent class
    def action(self, colony):
        bee_list = self.place.bees[:]
        for bee in bee_list:
            bee.reduce_armor(self.damage)

class ScubaThrower(ThrowerAnt):
    """ScubaThrower is a ThrowerAnt which is watersafe."""

    name = 'Scuba'

    watersafe = True
    food_cost = 5

    implemented = True


class HungryAnt(Ant):
    """HungryAnt will take three "turns" to eat a Bee in the same space as it.
    While eating, the HungryAnt can't eat another Bee.
    """
    name = 'Hungry'

    time_to_digest = 3 # Constant
    food_cost = 4

    implemented = True

    def __init__(self):
        Ant.__init__(self)
        self.digesting = 0 # Number of turns it has left to digest

    # which will eat a random Bee from its place, instantly killing the Bee.
    # After eating a Bee, it must spend 3 turns digesting before eating again.
    def eat_bee(self, bee):
        if self.digesting == 0 and bee is not None:
            bee.reduce_armor(bee.armor)
            self.digesting = self.time_to_digest

    # check if it's digesting; if so, decrement its digesting counter. 
    # Otherwise, eat a random Bee in its place (killing the Bee and
    # restarting the digesting timer).
    def action(self, colony):
        if self.digesting > 0:
            self.digesting -= 1
        else:
            victim = random_or_none(self.place.bees)
            self.eat_bee(victim)


class BodyguardAnt(Ant):
    """BodyguardAnt provides protection to other Ants."""
    name = 'Bodyguard'

    container = True # indicates an ant can contain another
    food_cost = 4

    implemented = True

    def __init__(self):
        Ant.__init__(self, 2) # initialize with armor 2
        self.ant = None  # The Ant hidden in this bodyguard

    def contain_ant(self, ant):
        self.ant = ant # set instance ant to argument ant

    def action(self, colony): # calls action method of original ant
        self.ant.action(colony)

class QueenPlace:
    """A place that represents both places in which the bees find the queen.

    (1) The original colony queen location at the end of all tunnels, and
    (2) The place in which the QueenAnt resides.
    """

    # intialize these attributes, which represent the original colony queen's
    # location and place where queen ant resides
    def __init__(self, colony_queen, ant_queen):
        self.colony_queen = colony_queen
        self.ant_queen = ant_queen

    @property
    def bees(self): # bees returns a list of all bees in either location
        return self.colony_queen.bees + self.ant_queen.bees

class QueenAnt(ScubaThrower):
    """The Queen of the colony.  The game is over if a bee enters her place."""

    name = 'Queen'

    food_cost = 6
    instances = 0
    imposter = False # instance attribute to check if imposter

    implemented = True

    def __init__(self):
        Ant.__init__(self) # default armor: 1
        # access by QueenAnt.___ means class's attribute
        if QueenAnt.instances == 1:
            self.imposter = True
        QueenAnt.instances += 1
        self.doubled_ants = [] # list to hold

    def action(self, colony):
        """
        A queen ant throws a leaf, but also doubles the damage of ants in her tunnel.
        Impostor queens do only one thing: reduce their own armor to 0.
        """
        
        # If the queen ant is an imposter, reduce its armor to 0 and return
        if self.imposter:
            self.reduce_armor(self.armor)
            return

        # Create a new instance of QueenPlace with the following arguments:
        # 1. original location of queen (colony.queen)
        # 2. location of queen ant (self.place)
        # This allows us to access the queen attribute to see if bees have reached the queen
        colony.queen = QueenPlace(colony.queen, self.place)

        def double_damage(place):
            # If the ant at the current place is not a QueenAnt
            if not isinstance(place.ant, QueenAnt):
                # Check if the ant is not None and not already doubled
                if place.ant is not None and place.ant not in self.doubled_ants:
                    self.doubled_ants.append(place.ant) # Add the ant to the doubled_ants list
                    place.ant.damage *= 2 # Double the ant's damage
                    # If the ant is a bodyguard and the ant it is guarding is not a queen ant
                    if place.ant.container and not isinstance(place.ant.ant, QueenAnt):
                        self.doubled_ants.append(place.ant.ant)
                        place.ant.ant.damage *= 2

        # If the ant at the current place is a bodyguard, double it
        # self refers to instance of QueenAnt
        if isinstance(self.place.ant, BodyguardAnt):
            double_damage(self.place) # call double_damage method on the QueenAnt place

        # call double_damage method on the QueenAnt place

        # Double the damage of all ants in the forward tunnel
        forward = self.place
        while forward.entrance is not None:
            forward = forward.entrance
            double_damage(forward)

        # Double the damage of all ants in the backward tunnel
        backward = self.place
        while backward.exit is not None:
            backward = backward.exit
            double_damage(backward)

        # Call the action method of ScubaThrower
        # Which will call ThrowerAnt's ability to throw at nearest ant in hive
        ScubaThrower.action(self, colony)


class AntRemover(Ant):
    """Allows the player to remove ants from the board in the GUI."""

    name = 'Remover'
    implemented = True

    def __init__(self):
        Ant.__init__(self, 0)


##################
# Status Effects #
##################

def make_slow(action):
    """Return a new action method that calls action every other turn.

    action -- An action method of some Bee
    """
    def new_action(colony):
        if colony.time % 2 == 0: # even time
            action(colony)
        # does nothing on other turns
        return new_action

def make_stun(action):
    """Return a new action method that does nothing.

    action -- An action method of some Bee
    """
    def new_action(colony):
        # does nothing
        return new_action

def apply_effect(effect, bee, duration):
    """Apply a status effect to a BEE that lasts for DURATION turns."""

    old_action = bee.action # store old action
    new_action = effect(bee.action) # new action is a function
    def action(colony):
        nonlocal duration
        if duration > 0:
            new_action(colony)
            duration -= 1
        else:
            old_action(bee.action)
            
    bee.action = action


class SlowThrower(ThrowerAnt):
    """ThrowerAnt that causes Slow on Bees."""

    name = 'Slow'

    food_cost = 4

    # Does not require an __init__ method bc.
    # it does not set any instance attributes to itself
    # i.e: name, food_cost, and implemented are set directly in class
    # TLDR: only need __init__ to initialize instance specific attributes

    implemented = False

    def throw_at(self, target):
        if target:
            apply_effect(make_slow, target, 3)


class StunThrower(ThrowerAnt):
    """ThrowerAnt that causes Stun on Bees."""

    name = 'Stun'

    food_cost = 6

    implemented = False

    def throw_at(self, target):
        if target:
            apply_effect(make_stun, target, 1)

@main
def run(*args):
    start_with_strategy(args, interactive_strategy)
