# http://www.codewars.com/kata/52adc142b2651f25a8000643/

class Sleigh(object):
    @classmethod
    def authenticate(cls, name, password):
        return name == "Santa Claus" and password == "Ho Ho Ho!"
