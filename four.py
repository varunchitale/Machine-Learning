import matplotlib.pyplot as plt
from matplotlib import style
import random,math

#plt.plot([1,2,6],[2,7,8])
#style.use('ggplot') #grid style

plt.title('Demo Title')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

n = input("Size?: ")

x=[random.random()*100 for i in range(n)]
y=[0 for i in range(n)]
for i in range(0,n):
	y[i] = math.sin(x[i])

plt.scatter(x,y)
plt.show()



'''x,y = np.loadtxt('exampleFile.csv',
                 unpack=True,
                 delimiter = ',')'''