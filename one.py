import matplotlib.pyplot as plt
import random, math

x=[0,5,10]
y=[0,5*math.sqrt(3),0]

plt.plot(x,y)

#start point

x0=float(1)
y0=float(0)
plt.scatter(x0,y0)

for i in range(2000):
	point = random.randint(0,2)

	x0 = (x0+x[point])/2
	y0 = (y0+y[point])/2

	plt.scatter(x0,y0)
plt.show()
	

