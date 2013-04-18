import urllib2
from random import choice

ascii_fonts = ['isometric4',
               'starwars',
               'clr8x8',
               'alligator',
               'char3___',
               'ticks',
               'tombstone',
               'p_s_h_m_',
               'colossal',
               'shadow',
               'ascii___',
               'drpepper',
               'basic',
               'rounded',
               'nancyj',
               'xhelvi',
               'e__fist_',
               'chunky']

def ascii_print(string):
    font = choice(ascii_fonts)
    print font
    print urllib2.urlopen("http://artii.herokuapp.com/make?text=%s&font=%s" % (string, font)).read()
