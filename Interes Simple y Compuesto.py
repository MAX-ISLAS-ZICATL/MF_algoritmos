import numpy as np

def Interes_simple (VP,i_p,t):
    i = i_p/100
    VF = VP*(1+(t*i))
    return VF

def Interes_Compuesto(VP,i_p,t,m=1):
    i = i_p/100
    VF = VP * ((1+(i/m))**(m*t))
    return VF
def Vi_a_la_m(i_p,m):
    i = i_p/100
    k = (1+i)**m
    v = 1/k
    return v

def A_vencida(n,i_p):
    i = i_p/100
    V = 1/(1+i)
    alfa = (1-(V**n))/i
    return alfa
def A_anticipada(n,i_p):
    i = i_p/100
    V = 1/(1+i)
    d = i * V
    alfa = (1-(V**n))/d
    return alfa

def S_vencida(n,i_p):
    i = i_p/100
    w = ((1+(i))**(n))
    Sss = (w-1)/i
    return Sss
def S_anticipada(n,i_p):
    i = i_p/100
    d = i/(1+i)
    w = ((1+(i))**(n))
    Sss = (w-1)/d
    return Sss

def W(k, f):
    w= f / A_anticipada(11-k,3)
    return w

if __name__ == "__main__":

    f0 = 1000*A_vencida(10,3)
    print(f0)
    f1 = Interes_Compuesto(f0,4,1)

    w1 = W(1,f1)

    f2 = Interes_Compuesto(f1-w1,4,1)
    w2 = W(2,f2)
    f3 = Interes_Compuesto(f2-w2,4,1)
    w3 = W(3,f3)
    f4 = Interes_Compuesto(f3-w3,4,1)
    w4 = W(4,f4)
    f5 = Interes_Compuesto(f4-w4,5,1)
    w5 = W(5,f5)
    f6 = Interes_Compuesto(f5-w5,5,1)
    w6 = W(6,f6)
    f7 = Interes_Compuesto(f6-w6,5,1)
    w7 = W(7,f7)
    f8 = Interes_Compuesto(f7-w7,5,1)
    w8 = W(8,f8)
    f9 = Interes_Compuesto(f8-w8,5,1)
    w9 = W(9,f9)
    f10 = Interes_Compuesto(f9-w9,5,1)
    w10 = W(10,f10)


    print(f1)
    print(w1)

    print(f2)
    print(w2)
    print(f3)
    print(w3)

    print(f4)
    print(w4)
    print(f5)
    print(w5)

    print(f6)
    print(w6)


    print(f7)
    print(w7)

    print(f8)
    print(w8)

    print(f9)
    print(w9)

    print(f10)
    print(w10)
