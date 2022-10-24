import numpy as np
from matplotlib import pyplot as plt

def calc_pi(N):

    number_in_circle=0

    for i in range(N):
        x = np.random.uniform(0,1)
        y = np.random.uniform(0,1)
        skalar = (x**2 + y**2)**0.5
        if  skalar <= 1:
            number_in_circle+=1


    pi_calc=number_in_circle/N*4
    pi_real=3.1415926535
    abweichung=pi_real-pi_calc

    return pi_calc,abweichung


pi_real=3.1415926535

PIs=[]
abweichungen=[]
x_min=10
x_max=1000

for i in range(x_min,x_max):
    pi,abweichung=calc_pi(i)
    PIs.append(pi)
    abweichungen.append(abweichung)

print("Calculating pi with borders {",x_min,";",x_max,"}")
print()
print("Pi real:",pi_real)
print("Pi calc:",PIs[-1])
print()
mittelwert=sum(abweichungen)/len(abweichungen)
print("average deviation:",mittelwert)

plt.plot([x for x in range(len(abweichungen))], PIs)
plt.axhline(pi_real)

#plt.plot(x,y, linewidth=0, marker="o",color="blue")
#plt.plot(x,y,linewidth=0,marker="o", color="red")"
#plt.plot(Xs,Ys, linewidth=0, marker=".",color="blue")
#plt.plot(,Ys_in, linewidth=0, marker=".",color="red")
plt.show() 



