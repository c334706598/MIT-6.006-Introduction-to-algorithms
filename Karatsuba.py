# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:44:54 2018

@author: XIN
"""

### Newton's method: x_i+1 = x_i - f(x_i)/f'(x_i)
### To find the square root of a: x_i+1 = 1/2 * (x_i + a/x_i)
import time
import matplotlib.pyplot as plt

def To_list(a):
    A = []
    while a != 0:
        A.append(a % 10)
        a //= 10
    return A

def To_int(A):
    a = 0
    n = 0
    for digit in A:
        a += digit * 10**n
        n += 1
    return a

#a = 12345601
#print(To_list(a))

def _mul(A, B):      # for list representation
    
    la = len(A)
    lb = len(B)
    n = 1
    
    if len(A) <= 2 and len(B) <= 2:
        return  To_list(To_int(A) * To_int(B))  ### O(1)
    
    while 2**n < len(A) or 2**n < len(B):      ### O(lgn)
        n += 1           
    
    A = A + [0]*(2**n-la)      ### O(n)
    B = B + [0]*(2**n-lb)      ### O(n)

    A0 = _low(A)         # Time complexity O(n)
    A1 = _high(A)        # Time complexity O(n)
    B0 = _low(B)         # Time complexity O(n)
    B1 = _high(B)        # Time complexity O(n)
    C0 = _mul(A0, B0)
    C2 = _mul(A1, B1)
#    print(mul(add(a0, a1), add(b0, b1)))
#    print('c0=',c0)
#    print('c2=',c2)
    C1 = _minus(_minus(_mul(_add(A0, A1), _add(B0, B1)), C0), C2)
    C2 = [0] * 2**n + C2 
    C1 = [0] * 2**(n-1) + C1 
    return _add(_add(C2, C1), C0)

def mul(a, b):
    la = len(a)         ### O(1)
    lb = len(b)         ### O(1)
    n = 1
    
    if len(a) <= 2 and len(b) <= 2:
        return str(int(a)*int(b))   ### O(1)
    
    while 2**n < len(a) or 2**n < len(b):      ### O(lgn)
        n += 1           
    
    a = '0'*(2**n-la) + a        ### O(n)
    b = '0'*(2**n-lb) + b        ### O(n)



    a0 = low(a)         # Time complexity O(n)
    a1 = high(a)        # Time complexity O(n)
    b0 = low(b)         # Time complexity O(n)
    b1 = high(b)        # Time complexity O(n)
    c0 = mul(a0, b0)
    c2 = mul(a1, b1)
#    print(mul(add(a0, a1), add(b0, b1)))
#    print('c0=',c0)
#    print('c2=',c2)
    c1 = minus(minus(mul(add(a0, a1), add(b0, b1)), c0), c2)
    c2 = c2 + '0' * 2**n
    c1 = c1 + '0' * 2**(n-1)
    return add(add(c2, c1), c0)
    
def _high(A):      # for list representation  
    l = len(A)
    return A[l//2:]

def _low(A):
    l = len(A)
    return A[:l//2]

def high(a):   ### Time complexity O(n)
    l = len(a)
    return a[:l//2]

def low(a):    ### Time complexity O(n)
    l = len(a)
    return a[l//2:]

def _trim(List):    ### Time complexity O(n)  ### for list representation
    p = 0
    l = len(List)
    while p < l:
        if List[~p] == 0:
            p += 1
        else:
            break
    if p == l:
        return [0]
    else:
        return List[:~(p-1)] if p > 0 else List

def trim(string):    ### Time complexity O(n)
    p = 0
    l = len(string)
    while p < l:
        if string[p] == '0':
            p += 1
        else:
            break
    if p == l:
        return '0'
    else:
        return string[p:]

def _add(A, B):     ### Time complexity O(n)    ### for list representation
###    return str(int(a)+int(b))  ### This is not linear time !!!    
### the following is linear complexity
    
    A = _trim(A)
    B = _trim(B)    
        
    _sum = []
    la = len(A)
    lb = len(B)
    l = min(la, lb)
    if la < lb:  # switch a and b so that a is always no shorter than b
        A, B = B, A
        la, lb = lb, la
        
    carry = 0
    for i in range(l):
        temp = A[i] + B[i] + carry
        digit = temp % 10
        carry = temp // 10
        _sum.append(digit)
        
    while i < la-1:
        if carry == 0:
            _sum += A[i+1:]
            break
        else:
            i += 1
            temp = A[i] + carry
            digit = temp % 10
            carry = temp // 10
            _sum.append(digit)
    
    if carry == 1:
        _sum.append(1)
        
    return _sum        

def add(a, b):     ### Time complexity O(n)
###    return str(int(a)+int(b))  ### This is not linear time !!!    
### the following is linear complexity
    
    a = trim(a)
    b = trim(b)    
        
    _sum = ''
    la = len(a)
    lb = len(b)
    l = min(la, lb)
    if la < lb:  # switch a and b so that a is always no shorter than b
        a, b = b, a
        la, lb = lb, la
        
    carry = 0
    for i in range(l):
        temp = (int(a[~i]) + int(b[~i]) + carry)
        digit = temp % 10
        carry = temp // 10
        _sum += str(digit)
        
    while i < la-1:
        if carry == 0:
            _sum += a[:~i][::-1]
            break
        else:
            i += 1
            temp = int(a[~i]) + carry
            digit = temp % 10
            carry = temp // 10
            _sum += str(digit)
    
    if carry == 1:
        _sum += '1'
        
    return _sum[::-1]
                
#print(add('1233123'))

def _minus(A, B):     ### Time complexity O(n)          ### for list representation
    ### assuming here a is always larger than b, all the operation is defined on the positive integers
    ### linear time complexity
    A = _trim(A)
    B = _trim(B)    
    
    diff = []
    l = len(B)
    carry = 0
#    print('a=', a)
#    print('b=', b)
#    
    for i in range(l):
        digit_A = A[i]
        digit_B = B[i]
        if digit_A - carry >= digit_B:
            diff.append(digit_A - carry - digit_B)
            carry = 0
        else:
            diff.append(digit_A + 10 - carry - digit_B)
            carry = 1
            
    while carry == 1:
        i += 1
        digit_A = A[i]
        if digit_A == 0:
            diff.append(9)
            carry = 1
        else:
            diff.append(digit_A - carry)
            carry = 0
        
    diff += A[i+1:]
        
    return diff

def minus(a, b):     ### Time complexity O(n)
    ### assuming here a is always larger than b, all the operation is defined on the positive integers
    ### linear time complexity
    a = trim(a)
    b = trim(b)    
    
    diff = ''
    l = len(b)
    carry = 0
#    print('a=', a)
#    print('b=', b)
#    
    for i in range(l):
        digit_a = int(a[~i])
        digit_b = int(b[~i])
        if digit_a - carry >= digit_b:
            diff += str(digit_a - carry - digit_b)
            carry = 0
        else:
            diff += str(digit_a + 10 - carry - digit_b)
            carry = 1
            
    while carry == 1:
        i += 1
        digit_a = int(a[~i])
        if digit_a == 0:
            diff += '9'
            carry = 1
        else:
            diff += str(digit_a - carry)
            carry = 0
        
    diff += a[:~i][::-1]
        
    return diff[::-1]
            
    


#a = '12345567881231231123131333132313888'
#b = '12333456677123123113131131331238888'
#print(Karatsuba_mul(a,b)=='152263526617648095227423243968516371732477105725680661152537128076544')
    
### Newton's Method for computing R/b
### f(x) = 1/x - b/R,   f'(x) = -1/x^2
### x_i+1 = 2x_i - bx_i^2/R

def _divide(A,B):
    l = 2 * max(len(A), len(B))
#    print(l)
    ans = [1]
    while True:
        temp1 = ans
        temp2 = _mul(_mul(ans, ans), B)
        if len(temp2) > l:
            ans = _minus(_mul(ans, [2]), temp2[l:])
        else:
            ans = _mul(ans, [2])
        if temp1 == ans:
            break
    return _mul(A, ans)[l:]

def divide(a,b):
    l = 2 * max(len(a), len(b))
#    print(l)
    ans = '1'
    while True:
        temp1 = ans
        temp2 = mul(mul(ans, ans), b)
        if len(temp2) > l:
            ans = minus(mul(ans,'2'), temp2[:-l])
        else:
            ans = mul(ans,'2')
        if temp1 == ans:
            break
    return mul(a, ans)[:-l]
        
    
#print(divide('1000','25'))
#print(_divide([0,0,0,1], [3,2]))      
    
     
def root(int1, digit):
    d = int(digit)
    int1 = int1 + '0'*(2*d)
    root = '1'
    while True:
        temp1 = root
        root = divide(add(root, divide(int1, root)), '2')
        if root == temp1:
            break
    return root[:-d] + '.' + root[-d:]

def _root(int1, digit):
    d = digit[0]
    int1 = [0]*(2*d) + int1 
    root = [1]
    while True:
        temp1 = root
        root = _divide(_add(root, _divide(int1, root)), [2])
        if root == temp1:
            break
    return root

print(_root([2], [4]))

x = []
t = []

#for i in range(5):
#    t1 = time.time()    
#    print(root('2', str(i+1)))
#    t2 = time.time()
#    x.append(i+1)
#    t.append(t2-t1)

#for i in range(10000,10001):
    
#    int1 = '1'+'0'*i
#    int2 = '2'+'0'*i
#    _int1 = 1*10**i
#    _int2 = 2*10**i
#    _INT1 = [0]*i + [1]
#    _INT2 = [0]*i + [2]

#    t1 = time.time()    
#    ans1 = add(int2, int1)
#    ans2 = _add(_INT2, _INT1)
#    ans1 = minus(int2, int1)
#    ans2 = _minus(_INT2, _INT1)
#    ans1 = mul(int2, int1)
#    ans2 = _mul(_INT2, _INT1)
#    print(ans1==ans2)
#    t2 = time.time()
#    print(i)
#    print(t2-t1)
#    x.append(i)
#    t.append(t2-t1)

#plt.plot(x, t)
#print(t)
    
#print(root('2','5'))    

#print(mul('12345','56789'))
#print(_mul([5,4,3,2,1],[9,8,7,6,5]))
### mul time complexity test result O(n^(1.854)) worse than expected O(n^(1.585))