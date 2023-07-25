#!/usr/bin/python3
""" returns a list of available attributes and methods """

def lookup(obj):
    return [method for method in dir(obj)]
