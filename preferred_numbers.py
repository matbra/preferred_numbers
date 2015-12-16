# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 14:32:28 2015

@author: Matthias Brandt
"""

# TODO: deal with the problem at 8 (should be 8, is 7.95)

import numpy as np

a = 10 # renard's default base

def compute_series(R=10):
    series = a**(np.arange(R+1)/R)
    
    # round to multiple of 0.05 (compare wiki article)
    factor = np.round(series / 0.05)
    series = 0.05 * factor
        
    return series

def preferred_number(x, R=10):
    i = np.round(R * np.log10(x))
    
    # determine the rounding factor
    a_base = 0.05 # default rounding factor for values between 0 ... 10
    a = a_base * 10**(np.floor((np.log10(x))))
    factor = np.round(10**(i/R) / a)
    p = a * factor

    return p, i
    
if __name__ == '__main__':
    # compute the standard ISO series
    print(compute_series(10))
    
    print(preferred_number(3000))