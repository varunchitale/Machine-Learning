from numpy import exp, array, random, dot
import matplotlib.pyplot as plt

class NeuralNetwork():
	#something goes here
	def __init__(self):
		random.seed(1)
		self.synaptic_weights = 2 * random.random((9,1)) -1

		self.trainingSetIP = array([[random.choice([0,1]) for i in range (9)] for j in range (700)])
		self.trainingSetOP = array([[random.choice([0,1]) for i in range (700)] for j in range (1)]).T

	def func_sigmoid(self, x):
		return 1 / (1 + exp(-x))

	def func_sigmoid_derivative(self,x):
		return x * (1-x)

	def think(self, trainingSetIP):
		return self.func_sigmoid(dot(trainingSetIP, self.synaptic_weights))


	def train_network(self, trainingSetIP, trainingSetOP, iterations):
		for i in xrange(iterations):
			output = self.think(trainingSetIP)
			
			error = trainingSetOP - output


			#self.scatter_mean_error(error,i)
						
			adjustment = dot(trainingSetIP.T , (error * self.func_sigmoid_derivative(output)) )
			
			self.synaptic_weights += adjustment

	def scatter_mean_error(self,error,xvalue):
		mean_error = 0
		for i in range(10):
			mean_error += error[i]
		mean_error /= 10

		plt.scatter(xvalue,abs(mean_error), s=4)
			

if __name__ == "__main__":
	nn = NeuralNetwork()
	print "Generating initial synaptic weights:"
	print nn.synaptic_weights

	print "\nTraining data-set: Input:"
	print nn.trainingSetIP
	print "Output:"
	print nn.trainingSetOP
	
	nn.train_network(nn.trainingSetIP, nn.trainingSetOP, 1000)

	print "Final synaptic weights:"
	print nn.synaptic_weights

	print "Test input [1,0,0,1,0,1,1,1,1,0]:"
	print nn.think(array([1,0,0,1,0,1,1,1,1]))

	plt.show()
