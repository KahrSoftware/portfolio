import time
import tensorflow.compat.v1 as tf

'''
tensorflowXOR.py
Tensorflow neural network which trains on and classifies the XOR function
Justin Kahr
'''


tf.disable_v2_behavior()
print(tf.__version__)


XORin = [[0,0], [0,1], [1,0], [1,1]]
XORout = [[0], [1], [1], [0]]

x = tf.placeholder(tf.float32, shape=[4,2])
y = tf.placeholder(tf.float32, shape=[4,1])

# weights
w1 = tf.Variable([[1.0, 0.0],[1.0, 0.0]], shape=[2,2])
w2 = tf.Variable([[0.0], [1.0]], shape=[2,1])

# biases
b1 = tf.Variable([0.0, 0.0], shape=[2])
b2 = tf.Variable([0.0], shape=1)

# forward and back propigation
classification = tf.sigmoid(tf.matmul(tf.sigmoid(tf.matmul(x, w1) + b1), w2) + b2)

# error
e = tf.reduce_mean(tf.squared_difference(y, classification))
train = tf.train.GradientDescentOptimizer(0.1).minimize(e)
 
trainTime = time.time()

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range (1000001):
    error = sess.run(train, feed_dict={x: XORin, y: XORout})
    # Training debug print statements
    #print('\nEpoch: ' + str(i))
    #print('\nError: ' + str(sess.run(e, feed_dict={x: XORin, y: XORout})))
    #for el in sess.run(classification, feed_dict={x: XORin, y: XORout}):
        #print('    ',el)
sess.close()
 
# Print the training time
trainTime = time.time() - trainTime
print("Training Time: "+str(trainTime)+" seconds.")
