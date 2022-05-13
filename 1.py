import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.1, 0.01)
plt.plot(x, np.sin(x), x, np.cos(x),)
plt.xlabel(r'$x$')
plt.ylabel(r'f(x)=x')
plt.title(r'$f_1(x)=sin(x), f_2(x)=cox(x)$')
plt.grid()
plt.savefig('graf_cos.pdf')
plt.show()

