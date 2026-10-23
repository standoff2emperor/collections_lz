import matplotlib.pyplot as plt
import numpy as np
a=np.linspace(1, 10)
#иксы
plt.plot(a, np.log(a), color='grey', marker='+', markevery=5)
#график логарифма
plt.plot(a, a**2, color='blue', marker='o', markevery=5)
#график степени
plt.plot(a, a**3, color='pink', marker='^', markevery=5)
#график степени
plt.plot(a, np.exp(a), color='purple', marker='x', markevery=5)
#експонента
plt.yscale('log')
plt.show()
#вывод