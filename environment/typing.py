from behave import register_type
from bhive.utilities.parse_functions import parse_bool, parse_integer, parse_nat, parse_nat1, parse_string

import json
import os


class Typing(object):

    def __init__(self):
        self.types = {}
        Typing.register_system_types()
        self.load_types('definitions/custom_types.json')
        self.include_machine = 'CustomTypes'

    def has_custom_types(self):
        return len(self.types.keys()) > 0

    def register_type(self, name, parse_function=(lambda x: x), enumeration=None):
        register_type(**{name:parse_function})
        self.types[name] = enumeration

    def load_types(self, json_filename):
        json_file = open(json_filename, 'r')
        type_data = json.load(json_file)
        for item in type_data:
            self.register_type(name=item['set'], enumeration=item['enumeration'])
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
    def string_for_type(type_tuple):
        (name, enumeration) = type_tuple
        if enumeration is None:
            return name
        else:
            # check if these are strings, or other literals
            return name + ' = {' + ", ".join([str(x) for x in enumeration]) + '}'

    def __str__(self):
        machine_string = "MACHINE\nCustomTypes\n/* synthesized from definitions/custom_types.json*/\nSETS\n\t"
        machine_string += "; ".join(map(Typing.string_for_type, self.types.items()))
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