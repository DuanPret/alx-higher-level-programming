#!/usr/bin/python3
""" Module that defines a JSON-to-object function """
import json


def from_json_string(my_str):
    """ Returns the Python object representation of a json string """
    return json.loads(my_str)
