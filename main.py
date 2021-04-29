import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def Graph(array):
    X, Y = np.meshgrid(x, t)
    plotT = plt.axes(projection='3d')
    plotT.plot_surface(X, Y, array, rstride=1, cstride=1, cmap=cm.coolwarm)
    plotT.set_title("Wykres zmiany temperatury, poszczególnych części szklanej rurki w czasie")
    plotT.set_xlabel("Długość [m]")
    plotT.set_ylabel("Czas [s]")
    plotT.set_zlabel("Temperatura [$^o C$]")
    plt.show()


L = 1                   #długość szklanej rurki
D = 10**(-5)            #współczynnik dyfuzji
h = 0.1                 #odległość pomiędzy punktami węzłowymi
TEMP_0 = 58             #temperatura szklanej rurki w punkcie x0
TEMP_10 = 181           #temperatura szklanej rurki w punkcie x10
end_time = 50000        #czas końcowy

c = (h**2)/(2*D)        #krok czasowy
a = (D*c)/(h**2)
b = 1-2*a
x = np.arange(0, L + h, h)
t = np.arange(0, end_time + c, c)
Temp_array = np.full((len(t), len(x)), 25)

for i in range(0, len(t)-1):
    for n in range(0, len(x)-1):
        Temp_array[:, 0] = TEMP_0
        Temp_array[:, 10] = TEMP_10
        q=Temp_array[i][n+1]+Temp_array[i][n-1]
        Temp_array[i+1, n] = a*q+b*Temp_array[i][n]



np.savetxt("wyniki.txt", Temp_array, fmt="%4d", delimiter='\t')
Graph(Temp_array)
