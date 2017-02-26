from behave import register_type
from bhive.utilities.parse_functions import parse_bool, parse_integer, parse_nat, parse_nat1, parse_string

from functools import partial
import json
import os

class Typing(object):

    def __init__(self):
        self.types = {}
        self.constant_types = {}
        Typing.register_system_types()
        self.load_types('definitions/custom_types.json')
        self.include_machine = 'CustomTypes'

    def has_custom_types(self):
        return len(self.types.keys()) > 0

    def register_type(self, name, parse_function=(lambda x: x), enumeration=None, is_constant=False):
        register_type(**{name:parse_function})
        if is_constant:
            self.constant_types[name] = enumeration
        else:
            self.types[name] = enumeration


    def load_types(self, json_filename):
        try:
            json_file = open(json_filename, 'r')
        except IOError:
            # failed to find a custom types file
            return

        type_data = json.load(json_file)
        for item in type_data:
            constant_type = 'constant' in item and item['constant']
            self.register_type(name=item['set'], enumeration=item['enumeration'], is_constant=constant_type)
        json_file.close()

    @staticmethod
    def register_system_types():
        """
        Will register all B system types.

        These keeps them from being synthesized.
        """
        register_type(STRING=parse_string)
        register_type(INT=parse_nat)
        register_type(BOOL=parse_bool)
        register_type(NAT=parse_nat)
        register_type(NAT1=parse_nat1)

    @staticmethod
    def string_for_type(allow_declaration_only, type_tuple):
        """
        Generates a string from a type tuple

        :param allow_declaration_only:  boolean flag to allow bare TYPE (without = {}), used for currying in __str__
        :param type_tuple:
        :return:
        """
        (name, enumeration) = type_tuple
        if allow_declaration_only and enumeration is None:
            return name
        else:
            # check if these are strings, or other literals
            return name + ' = {' + ", ".join([str(x) for x in enumeration]) + '}'

    def __str__(self):
        machine_string = "MACHINE\nCustomTypes\n/* synthesized from definitions/custom_types.json*/\nSETS\n\t"
        machine_string += "; ".join(map(partial(Typing.string_for_type, True), self.types.items()))
        if len(self.constant_types):
            machine_string += "\nCONSTANTS\n\t"
            machine_string += ", ".join(self.constant_types.keys())
            machine_string += "\nPROPERTIES\n\t"
            machine_string += " & ".join(map(partial(Typing.string_for_type, False), self.constant_types.items()))
        machine_string += "\nEND"
        return machine_string

    def synthesize(self):
        # this is RIPE for refactor
        if not os.path.exists(os.path.dirname("output/CustomTypes.mch")):
            os.mkdir(os.path.dirname("output"))

        output_file = open("output/CustomTypes.mch", "w")
        output_file.write(str(self))
        output_file.close()

    #todo: "in" to check it type is valid.


    #bhive.integration.load_types('definitions/custom_types.json')