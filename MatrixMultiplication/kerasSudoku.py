from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.optimizers import Adam
from keras.callbacks import History 
import time
import numpy
import sudokureader as sr

'''
kerasSudoku.py
Keras neural network which trains on and classifies / solves Sudokus
Justin Kahr
'''


class KerasAgent(object):
	
	# Saves specifications of model, model will be actually created in train_net
	def __init__(self, num_in_nodes, num_hid_nodes, num_hid_layers, num_out_nodes, learning_rate = 0.2, max_epoch=1000, momentum=0.1):
		assert num_in_nodes > 0 and num_hid_layers > 0 and num_hid_nodes and num_out_nodes > 0, "Illegal number of input, hidden, or output layers!"
		# Assign variables
		self.num_in_nodes = num_in_nodes
		self.num_hid_nodes = num_in_nodes
		self.num_hid_layers = num_hid_layers
		self.num_out_nodes = num_out_nodes
		self.learning_rate = learning_rate
		self.max_epoch = max_epoch
		self.momentum = momentum

	# Trains the model on given input and output data
	def train_net(self, in_vals, out_vals):
		# Keep track of training time
		trainTime = time.time()
		
		# Init model
		self.model = Sequential()
		
		# Add layers
		self.model.add(Dense(self.num_hid_nodes, input_dim=self.num_in_nodes))
		self.model.add(Activation('tanh'))
		i = 1
		while(i < self.num_hid_layers):
			print("Hidden Layer Made")
			self.model.add(Dense(self.num_hid_nodes))
			self.model.add(Activation('tanh'))
			i += 1
		self.model.add(Dense(self.num_out_nodes))
		self.model.add(Activation('sigmoid'))

		# Compile model
		adam = Adam(0.001, 0.9, 0.999)
		self.model.compile(loss='mean_squared_error', optimizer=adam)

		# Dictionary to hold error over time
		history = History()

		# Train the model
		self.model.fit(in_vals, out_vals, batch_size=1, nb_epoch=self.max_epoch, callbacks=[history])
		# Classify one more time once the model is trained
		self.classify(in_vals)

		# Print the training time
		trainTime = time.time() - trainTime
		print("Training Time: "+str(trainTime)+" seconds.")

	# Runs input through the model and prints values from output node
	def classify(self, in_vals):
		print(self.model.predict_proba(in_vals))

# Sudoku input values
NUM_SUDOKU=10000
in_vals = numpy.array(sr.get_sudoku_n(NUM_SUDOKU))
out_vals = numpy.array(sr.get_solution_n(NUM_SUDOKU))

#Agent initialization parameter list
#	num_in_nodes
#	num_hid_nodes
#	num_hid_layer
#	num_out_nodes
#	learning_rate
#	max_epoch
#	momentum
test_agent = KerasAgent(81, 729, 18, 81, max_epoch=10)
test_agent.train_net(in_vals, out_vals)
#test_agent.classify(in_vals)
