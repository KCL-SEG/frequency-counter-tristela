"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        itemstr = str(item)
        if itemstr in frequencies:
            frequencies[itemstr]=frequencies[itemstr]+1
        else:
            frequencies[itemstr]=1
    return frequencies
