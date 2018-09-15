import numpy as np
import matplotlib.pyplot as plt
# import zAccessCSV
# push the code in
# zAccessCSV

# Create data set
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
print(x1)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

# Create canvas & modify the figures
fig = plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

# plt.show()
# Save the figure.
plt.savefig('foo.png')
plt.savefig('foo.pdf')
