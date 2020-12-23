import random
import numpy
import math
import time
import matrixmath as mm
from scipy.special import expit

'''
pythonXOR.py
Justin Kahr
Neural net using my matrix math operations, trains on and classifies the XOR function
'''

class NeuralMMAgent(object):

    def __init__(self, num_in_nodes, num_hid_nodes, num_hid_layers, num_out_nodes, learning_rate = 0.2, max_epoch=10000, max_sse=.01, momentum=0.2, activation_function=None, random_seed=1):
        '''
          Arguments:
    num_in_nodes -- total # of input nodes for Neural Net
    num_hid_nodes -- total # of hidden nodes for each hidden layer
        in the Neural Net
    num_hid_layers -- total # of hidden layers for Neural Net
    num_out_nodes -- total # of output nodes for Neural Net
    learning_rate -- learning rate to be used when propagating error
    activation_function -- list of two functions:
        1st function will be used by network to determine activation given a weighted summed input
        2nd function will be the derivative of the 1st function
    random_seed -- used to seed object random attribute.
        This ensures that we can reproduce results if wanted
        '''
        assert num_in_nodes > 0 and num_hid_layers > 0 and num_hid_nodes and num_out_nodes > 0, "Illegal number of input, hidden, or output layers!"

        # Assign model's variables
        self.num_in = num_in_nodes
        self.num_hid = num_hid_nodes
        self.num_hid_layers = num_hid_layers
        self.num_out = num_out_nodes
        self.rand_obj = random_seed
        self.learning_rate = learning_rate
        self.max_sse = max_sse
        self.max_epoch = max_epoch
        self.momentum = momentum

        self.create_neural_structure(self.num_in, self.num_hid, self.num_hid_layers, self.num_out, self.rand_obj)


    def train_net(self, input_list, output_list, max_num_epoch=100000, max_sse=0.1):
        ''' Trains neural net using incremental learning
    (update once set of input-outputs)
    Arguments:
        input_list -- 2D list of inputs
        output_list -- 2D list of outputs matching inputs
                            max_num_epoch -- max number of trainings we can run
                            max_sse -- error beyond which training stops
    '''
        
        # Keep track of traning time
        trainTime = time.time()

        # Keep track of error
        all_err = []
        
        # Keep track of epoch number
        epoch = 0

        #vars for momentum
        deltaWih = [[0] * self.num_hid] * self.num_in
        deltaWho = [[0] * self.num_out] * self.num_hid
        deltaWhh = [0] * self.num_hid_layers

        while(True):

            # Put input values into a matrix
            #input_vals = numpy.matrix(input_list)
            input_vals = input_list

            # Initialize arrays to store hidden value matricies
            toHid = [None] * self.num_hid_layers
            hidden_vals = [None] * self.num_hid_layers

            # Hidden = g( in dot Wih + Bih )
            #toHid[0] = numpy.dot(input_list, self.Wih) + self.Bih
            #print(self.Bih)
            toHid[0] = mm.matrix_basis_add(mm.matrix_mult(input_list, self.Wih) , self.Bih)
            hidden_vals[0] = self.tanh_af(toHid[0]).tolist()

            # Hidden for "middle" hidden layers is:
            # = g (hidden-1 dot Whh[i] + Bhh[i])
            # range from 1 to num_hid_layers
            hid_layer = 1
            while(hid_layer < self.num_hid_layers):
                toHid[hid_layer] = numpy.dot(hidden_vals[hid_layer-1], self.Whh[hid_layer-1] + self.Bhh[hid_layer-1])
                hidden_vals[hid_layer] = self.tanh_af(toHid[hid_layer])
                hid_layer += 1

            # Output = g( hid dot Who + Bho )
            # Use hidden_vals[num_hid_layers - 1]
            #toOut = numpy.dot(hidden_vals[self.num_hid_layers-1], self.Who) + self.Bho
            toOut = mm.matrix_basis_add(mm.matrix_mult(hidden_vals[self.num_hid_layers-1], self.Who) , self.Bho)
            output_vals = self.sigmoid_af(toOut).tolist()

            # Output error
            #error = (output_list - output_vals)
            error = mm.matrix_add(output_list, mm.matrix_scalar_mult(-1, output_vals))
            # Matrix of deltas for output layer
            #deltaO = (error) * self.sigmoid_af_deriv(output_vals)
            deltaO = mm.matrix_elem_mult((error) , self.sigmoid_af_deriv(output_vals))

            # Initrialize array to store deltaH matricies
            deltaH = [None] * self.num_hid_layers
            # Matrix of deltas for input layer
            # Highest hidden to hidden connection needs to use deltaO
            #deltaH[self.num_hid_layers - 1] = (deltaO @ self.Who.transpose()) * self.tanh_af_deriv(hidden_vals[self.num_hid_layers - 1])
            deltaH[self.num_hid_layers - 1] = mm.matrix_elem_mult(mm.matrix_mult(deltaO , mm.matrix_transpose(self.Who)) , self.tanh_af_deriv(hidden_vals[self.num_hid_layers - 1]))

            # Range num_hid_layers - 1 to 1
            hid_layer = self.num_hid_layers - 1
            while(hid_layer > 0):
                # Calculate deltaH[n] using deltaH[n+1]
                #deltaH[hid_layer-1] = (deltaH[hid_layer] @ self.Whh[hid_layer-1].transpose()) * self.tanh_af_deriv(hidden_vals[hid_layer - 1])
                deltaH[hid_layer-1] = mm.matrix_elem_mult(mm.matrix_mult(deltaH[hid_layer] , mm.matrix_transpose(self.Whh[hid_layer-1])) * self.tanh_af_deriv(hidden_vals[hid_layer - 1]))
                hid_layer -= 1

            # Update the weights from input to first hidden layer, using momentum
            #self.Wih += self.learning_rate * (input_vals.transpose() @ deltaH)
            #deltaWih = (self.learning_rate * (input_vals.transpose() @ deltaH[0])) + (self.momentum * deltaWih)
            deltaWih = mm.matrix_add(mm.matrix_scalar_mult(self.learning_rate , mm.matrix_mult(mm.matrix_transpose(input_vals) , deltaH[0])) , mm.matrix_scalar_mult(self.momentum  , deltaWih))
            #self.Wih += deltaWih
            self.Wih = mm.matrix_add(self.Wih, deltaWih)

            # loop through weights which connect a pair of hidden layers
            hid_layer = 1
            while(hid_layer < self.num_hid_layers):
                # Update the weights between all hidden layers using momentum
                deltaWhh[hid_layer] = (self.learning_rate * hidden_vals[hid_layer].transpose() @ deltaH[hid_layer]) + (self.momentum * deltaWhh[hid_layer-1])
                self.Whh[hid_layer-1] += deltaWhh[hid_layer]
                hid_layer += 1

            # Update the weights from last hidden layer to output, using momentum
            #self.Who += self.learning_rate * (hidden_vals.transpose() @ deltaO)
            #deltaWho = (self.learning_rate * (hidden_vals[self.num_hid_layers-1].transpose() @ deltaO)) + (self.momentum * deltaWho)
            deltaWho = mm.matrix_add(mm.matrix_scalar_mult(self.learning_rate , mm.matrix_mult(mm.matrix_transpose(hidden_vals[self.num_hid_layers-1]) , deltaO)) , mm.matrix_scalar_mult(self.momentum , deltaWho))
            #self.Who += deltaWho
            self.Who = mm.matrix_add(self.Who, deltaWho)

            # Compile all error for storage
            sse = numpy.mean(numpy.asarray(error)**2)
            all_err.append(sse)
            # Print status each epoch
            print("Epoch: "+str(epoch)+" | sse: "+str(sse))
            epoch += 1
            # If below error threshold or done with all epochs break
            if (sse < max_sse or epoch >= max_num_epoch):
                break
        # Print our last output vals for comparison to given outputs
        for i in range(len(output_list)):
            print(str(output_list[i])+" | "+str(output_vals[i]))
        
        # Print the training time
        trainTime = time.time() - trainTime
        print("Training Time: "+str(trainTime)+" seconds.")


    #@staticmethod
    def create_neural_structure(self, num_in, num_hid, num_hid_layers, num_out, rand_obj):
        ''' Creates the structures needed for a simple backprop neural net
    This method creates random weights [-0.5, 0.5]
    Arguments:
        num_in -- total # of input nodes for Neural Net
        num_hid -- total # of hidden nodes for each hidden layer
in the Neural Net
        num_hid_layers -- total # of hidden layers for Neural Net
        num_out -- total # of output nodes for Neural Net
        rand_obj -- the random object that will be used to selecting
random weights
        Saves all parts of the network as object variables
    '''
        numpy.random.seed(rand_obj)
        RAND_ADJUST = 0.1667

        #Wih is Weights input to hidden, (input size, hidden size)
        #self.Wih = RAND_ADJUST*numpy.random.randn(num_in, num_hid)
        self.Wih = []
        for i in range(num_in):
            self.Wih.append([RAND_ADJUST*random.gauss(0,1)]*num_hid)
        #Bih is Bias input to hidden
        #self.Bih = numpy.full((1, num_hid), 0.1)
        self.Bih = [[0.1]*num_hid]

        #Whh is an array of matricies with weights between hidden layers
        self.Whh = [num_hid_layers-1]
        #Bhh is biases of hidden layer connections
        self.Bhh = [num_hid_layers-1]
        for i in range(num_hid_layers - 1):
            self.Whh[i] = RAND_ADJUST*numpy.random.randn(num_hid, num_hid)
            self.Bhh[i] = numpy.full((1, num_hid), 0.1)

        #Who is Weights hidden to output, (hidden size, output size)
        #self.Who = 0.1667*numpy.random.randn(num_hid, num_out)
        self.Who = []
        for i in range(num_hid):
            self.Who.append([RAND_ADJUST*random.gauss(0,1)]*num_out)
        #Bho is Bias hidden to output
        #self.Bho = numpy.full((1, num_out), 0.1)
        self.Bho = [[0.1]*num_out]

    @staticmethod
    def sigmoid_af(summed_input):
    #Sigmoid function
        return expit(summed_input)

    @staticmethod
    def sigmoid_af_deriv(sig_output):
    #The derivative of the sigmoid function
        return numpy.asarray(sig_output)*(1-numpy.asarray(sig_output))

    @staticmethod
    def relu_af(summed_input):
        #Relu function
        return numpy.maximum(0, summed_input)

    @staticmethod
    def relu_af_deriv(sig_output):
        #Derivative of the relu function
        return (numpy.asarray(sig_output) > 0) * 1

    @staticmethod
    def tanh_af(summed_input):
        #Tanh function
        return numpy.tanh(summed_input)

    @staticmethod
    def tanh_af_deriv(sig_output):
        #Derivative of the tanh function
        return 1 - (numpy.asarray(sig_output))**2


#Agent initialization parameter list
#   num_in_nodes
#   num_hid_nodes
#   num_hid_layer
#   num_out_nodes
#   learning_rate
#   max_epoch
#   max_sse
#   momentum
#   random_seed
test_agent = NeuralMMAgent(2, 4, 1, 1, max_epoch=1000000)
# XOR function
test_in = [[1,0],[0,0],[1,1],[0,1]]
test_out = [[1],[0],[0],[1]]
# Train the agent
test_agent.train_net(test_in, test_out, max_sse = 0, max_num_epoch=test_agent.max_epoch)
