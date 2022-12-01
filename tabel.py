import matplotlib.pyplot as plt
import numpy as np

"""xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints,'o:r')
plt.show()"""

"""x1 = np.array([3, 1, 2, 0])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)

plt.show()"""

"""#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

#plot 3:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

#plot 4:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

#plot 5:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

#plot 6:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()"""
# day one
"""x = np.random.randint(10,size=100)
y = np.random.randint(10,size=100)
colors=np.random.randint(10,size=100)
plt.scatter(x, y, c=colors, cmap='viridis')
# day two
x = np.random.randint(6,size=100)
y = np.random.randint(6,size=100)
colors =np.random.randint(10,size=100)
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.colorbar()
plt.show()"""

"""x = np.array(["A", "B", "C", "D"])
y =np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()"""

"""x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()"""

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode, shadow= True)
plt.show()