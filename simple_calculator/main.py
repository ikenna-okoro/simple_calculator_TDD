# -*- coding: utf-8 -*-
from functools import reduce
import operator



class SimpleCalculator:
    def add(self, *args):
        return sum(args)
    
    def subtract(self, a, b):
        return a - b
    
    def mul(self, *args):
        return reduce(operator.mul, args)
    
    

    
