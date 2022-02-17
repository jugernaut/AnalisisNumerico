from math import trunc
import numpy as np
from math import log10, floor

def truncar(x,t):
    if x==0:
        fl=0
    else:
        e=trunc(np.log10(abs(x)))
        if np.log10(abs(x))>0:
            e=e+1
        fl=trunc(x*10**(t-e))*10**(e-t)    
    return fl

def rdnd(x, t):

	return round(x, t-int(floor(log10(abs(x))))-1)


# Python3 program to convert fractional
# decimal to binary number
 
# Function to convert decimal to binary
# upto k-precision after decimal point
def decimalToBinary(num, k_prec) :
 
    binary = ""
 
    # Fetch the integral part of
    # decimal number
    Integral = int(num)
 
    # Fetch the fractional part
    # decimal number
    fractional = num - Integral
 
    # Conversion of integral part to
    # binary equivalent
    while (Integral) :
         
        rem = Integral % 2
 
        # Append 0 in binary
        binary += str(rem);
 
        Integral //= 2
     
    # Reverse string to get original
    # binary equivalent
    binary = binary[ : : -1]
 
    # Append point before conversion
    # of fractional part
    binary += '.'
 
    # Conversion of fractional part
    # to binary equivalent
    while (k_prec) :
         
        # Find next bit in fraction
        fractional *= 2
        fract_bit = int(fractional)
 
        if (fract_bit == 1) :
             
            fractional -= fract_bit
            binary += '1'
             
        else :
            binary += '0'
          
 
        k_prec -= 1
 
    return binary
    

