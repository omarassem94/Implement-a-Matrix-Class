#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Run this cell but don't modify it.

get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
from matrix import Matrix, zeroes, identity


# In[12]:


# some functionality already exists... here's a demo

m1 = Matrix([
    [1, 2],
    [3, 4]
])

m2 = Matrix([
    [2, 5],
    [6, 1]
])

print("m1 is")
print(m1)

print("m2 is")
print(m2)

print("we've also provided you with a function called zeros")
print("here's what happens when you call zeros(4,2)")
print(zeroes(4,2))

print("we've also provided you with a function called identity")
print("here's identity(3)")
print(identity(3))

print("Determinant function should be working now")
print(m1.determinant())

print("but not everything works yet!")
print("for example, matrix addition...")
print("run the cell below to see what happens when we try...")


# In[15]:


m1 = Matrix([
    [1, 2],
    [3, 4]
])

m2 = Matrix([
    [2, 5],
    [6, 1]
])

m3 = m1 + m2
print("m1 + m2 is")
print(m3)


# In[17]:


# Try running this code. You should get an assertion error. 
# You will continue to get assertion errors until all the 
# methods in matrix.py are correctly implemented.

# You can open matrix.py by selecting File > Open... 
# and then selecting matrix.py

import test


# In[18]:


# open matrix.py (File > Open...) and start
# implementing matrix methods! 

# when your code passes all the tests you can submit by 
# pressing the SUBMIT button in the lower right corner 
# of this page.


# In[19]:


import matrix as m

def test():
    I2 = m.Matrix([
        [1, 0],
        [0, 1]
        ])
    I2_neg = m.Matrix([
        [-1, 0],
        [0, -1]
        ])

    zero = m.Matrix([
        [0,0],
        [0,0]
        ])

    m1 = m.Matrix([
        [1,2,3],
        [4,5,6]
        ])

    m2 = m.Matrix([
        [7,-2],
        [-3,-5],
        [4,1]
        ])
    
    m3 = m.Matrix([
        [8]
        ])
    
    m3_inv = m.Matrix([
        [0.125]
        ])

    m1_x_m2 = m.Matrix([
        [ 13,  -9],
        [ 37, -27]])

    m2_x_m1 = m.Matrix([
        [ -1,   4,   9],
        [-23, -31, -39],
        [  8,  13,  18]])

    m1_m2_inv = m.Matrix([
        [1.5, -0.5],
        [2.0555556, -0.722222222]
        ])

    top_ones = m.Matrix([
        [1,1],
        [0,0],
        ])

    left_ones = m.Matrix([
        [1,0],
        [1,0]
        ])


    assert equal(-I2, I2_neg), "Error in your __neg__ function"
    assert equal(I2 + I2_neg, zero), "Error in your __add__ function"
    assert equal(m1 * m2, m1_x_m2), "Error in your __mul__ function"
    assert equal(m2 * m1, m2_x_m1), "Error in your __mul__ function"
    assert equal(m3.inverse(), m3_inv), """Error in your inverse function for the 1 x 1 case"""
    assert equal(m1_x_m2.inverse(), m1_m2_inv), """Error in your inverse function for the first 2 x 2 case"""
    assert equal(I2.inverse(), I2), """Error in your inverse function for the second 2 x 2 case"""
    assert equal(top_ones.T(), left_ones), "Error in your T function (transpose)"
    assert equal(left_ones.T(), top_ones), "Error in your T function (transpose)"
    assert equal(top_ones - left_ones.T(), m.zeroes(2,2)), "Error in your __sub__ function"
    assert (4*m.identity(5))[0][0] == 4, "Error in your __rmul__ function"
    assert (4*m.identity(5)).trace() == 20 , "Error in your trace function"

    assert type(-I2) == type(I2_neg), "Error: Your __neg__ function does not return a Matrix does not return a Matrix"
    assert type(I2 + I2_neg) == type(zero), "Error: Your __add__ function does not return a Matrix"
    assert type(m1 * m2) == type(m1_x_m2), "Error: Your __mul__ function does not return a Matrix"
    assert type(m2 * m1) == type(m2_x_m1), "Error: Your __mul__ function does not return a Matrix"
    assert type(m3.inverse()) == type(m3_inv), """Error: Your inverse function for the 1 x 1 case does not return a Matrix"""
    assert type(I2.inverse()) == type(I2), """Error: Your inverse function for the 2 x 2 case does not return a Matrix"""
    assert type(top_ones.T()) == type(left_ones), "Error: Your T function (transpose) does not return a Matrix"
    assert type(left_ones.T()) == type(top_ones), "Error: Your T function (transpose) does not return a Matrix"
    assert type(top_ones - left_ones.T()) == type(m.zeroes(2,2)), "Error: Your __sub__ function does not return a Matrix"
    print("Congratulations! All tests pass. Your Matrix class is working as expected.")

def equal(m1, m2):
    if len(m1.g) != len(m2.g): return False
    if len(m1.g[0]) != len(m2.g[0]): return False
    for r1, r2 in zip(m1.g, m2.g):
        for v1, v2 in zip(r1, r2):
            if abs(v1 - v2) > 0.0001:
                return False
    return True

test()


# In[4]:


import matrix as m

print(4*m.identity(5))
print(4*m.identity(5).trace())

