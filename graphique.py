from ctypes.wintypes import RGB
from math import cos, pi
from matplotlib.colors import rgb2hex

import matplotlib.pyplot as plt
import numpy as np

# supprime toutes les figures précédentes
plt.clf()
# acces des abcisses

# pour avoir les points

x=np.linspace(0,20,100)
y=[cos(t) for t in x] 
# Dans mon projet x= valeur y=date)

plt.plot(x,y, label="cos(x)",color="green")
plt.title('Courbe du cosinus')
plt.xlabel("abscisses")
plt.ylabel('ordonnees')
plt.legend()
plt.show()

