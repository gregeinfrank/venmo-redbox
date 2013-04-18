import urllib2
from random import choice

def ascii_print(string):
    ascii_fonts = urllib2.urlopen("http://artii.herokuapp.com/fonts_list").read().split('\n')
    font = choice(ascii_fonts)
    print font
    print urllib2.urlopen("http://artii.herokuapp.com/make?text=%s&font=%s" % (string, font)).read()
