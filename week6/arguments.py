#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="This is Bryan Duncanson's script")


parser.add_argument('-m', dest='BASIC', help='Enter some text'),
parser.add_argument('-i', '--integer', dest='varInteger', metavar='[an integer]', default=17, type=int, required=False, help='<required> Enter a simple Integer')
parser.add_argument('-d', '--float', dest='varFloat', metavar='[a float]', default=17.0, type=float, required=False, help='Enter a simple Float')
parser.add_argument('-s', '--string', dest='varString', metavar='[a string]', default='arg parse seems useful', type=str, required=False, help='Enter a simple String')
parser.add_argument('-l', dest='varList', metavar='[strings]', default=[], nargs='+', required=False, help='Enter a list of strings (space delimited)')
parser.add_argument('-t', '--set-true', dest='bool_t', default=False, action='store_true', required=False, help='Toggle from default False to True')
parser.add_argument('-f', '--setfalse', dest='bool_f', default=True, action='store_false', required=False, help='Toggle from default True to False')
parser.add_argument('-v','--version', action='version', version='1.2')


args = parser.parse_args()

print(args.varInteger)
print(args.varString)
print(args.varFloat)