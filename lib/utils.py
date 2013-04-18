import urllib2
from random import choice

ascii_fonts = ['isometric4',
               'starwars',
               'clr8x8',
               'alligator',
               'char3___',
               'tombstone',
               'colossal',
               'shadow',
               'ascii___',
               'drpepper',
               'basic',
               'rounded',
               'nancyj',
               'xhelvi',
               'chunky']

def ascii_print(string):
    # url needs to be sent with '+' as space
    string = string.replace(' ', '+')
    font = choice(ascii_fonts)
    print urllib2.urlopen("http://artii.herokuapp.com/make?text=%s&font=%s" %
                          (string, font)).read()
