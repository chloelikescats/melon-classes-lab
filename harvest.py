############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller=False):
        """Initialize a melon."""
        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        # Fill in the rest
    def __repr__(self):
        return "< melon called %s >" % (self.name)

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    muskmelon = MelonType('Muskmelon', 'musk', 1998, 'green', True, True)
    muskmelon.add_pairing('mint')

    casaba = MelonType('Casaba', 'cas', 2003, 'orange', False)
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')

    crenshaw = MelonType('Crenshaw', 'cren', 1996, 'green', False)
    crenshaw.add_pairing('proscuitto')

    yellow_watermelon = MelonType('Yellow Watermelon', 'yw', 2013, 'yellow', False, True)
    yellow_watermelon.add_pairing('ice cream')

    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]
    return all_melon_types


def print_melon_pairings(melon_types):
    """Takes in list of melon types and prints their pairings
    """
    for melon in melon_types:
        print "{name} pairs with".format(name=melon.name)

        for pairing in melon.pairings:
            print "- {pairings}".format(pairings=pairing)
        print


def return_melon_code_dict(melon_types):
    """Takes in a list of melon types and returns a dict of their codes and their instance."""

    melon_code_dict = {}

    for melon in melon_types:
        melon_code_dict[melon.code] = melon

    return melon_code_dict


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        self.type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        """Takes melon info and returns if it is sellable"""

        return self.shape_rating > 5 and self.color_rating > 5 and self.field != 3


def make_melons(melon_code_dict):
    """Returns a list of Melon objects."""
    melon1 = Melon(melon_code_dict["yw"], 8, 7, 2, "Sheila")
    melon2 = Melon(melon_code_dict["yw"], 3, 4, 2, "Sheila")
    melon3 = Melon(melon_code_dict["yw"], 9, 8, 3, "Sheila")
    melon4 = Melon(melon_code_dict["cas"], 10, 6, 35, "Sheila")
    melon5 = Melon(melon_code_dict["cren"], 8, 9, 35, "Michael")
    melon6 = Melon(melon_code_dict["cren"], 8, 2, 35, "Michael")
    melon7 = Melon(melon_code_dict["cren"], 2, 3, 4, "Michael")
    melon8 = Melon(melon_code_dict["musk"], 6, 7, 4, "Michael")
    melon9 = Melon(melon_code_dict["yw"], 7, 10, 3, "Sheila")
    melon_list = [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]
    return melon_list


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable() is True:
            print ("Harvested by {harvester} from Field # {field} CAN BE SOLD"
                   .format(harvester=melon.harvester, field=melon.field))
        else:
            print ("Harvested by {harvester} from Field # {field} NOT SELLABLE"
                   .format(harvester=melon.harvester, field=melon.field))

def create_melon_object(melon_file):
    """Takes in file, line by line and creates instance for each melon"""
    pass
    # with open(melon_file) as melon_file:
    #     for line in melon_file:
    #         line = line.rstrip()
    #         melons = line.split(' ')