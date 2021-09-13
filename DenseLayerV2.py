"""
So basically this is the same thing as the DenseLayerV1, but this one is compatable with the activation functions.
Right now there are only 2 activation functions available (sigmoid and relu), but more can be added.
The syntax for the forward propagations is the same, except there is an additional kwarg in the constructor's signature.
The activation function automatically defaults towards the sigmoid.
If an activation function that isn't available is entered, then the network assumes there is no activation, but will still function with only weights and biases.
"""

class DenseLayer:
    
    #constructor
    def __init__(self, input_number, neuron_number, activation="sigmoid"): #same signature except additional kwarg for activation
      #instance variables
      self.weights = 0.10 * nm.random.randn(input_number, neuron_number)
      self.biases = nm.zeros((1, neuron_number))
      self.activation = activation
    
    #forward propagation
    def forward(self, inputs):
      #forward propagations
      self.inputs = inputs
      self.outputs = nm.dot(self.inputs, self.weights) + self.biases
      
      #parses the inputs through depending on the activation function kwarg
      if (self.activation == "sigmoid"):
        for point in range(len(self.outputs)): self.outputs[point] = ActivationFunctions.sigmoid(self.outputs[point])
      elif (self.activation == "relu"):
        for point in range(len(self.outputs)): self.outputs[point] = ActivationFunctions.relu(self.outputs[point])
      elif (self.activation == "swish"):
        for point in range(len(self.outputs)): self.outputs[point] = ActivationFunctions.swish(self.outputs[point])
      else:
        pass #when there is no kwarg that works, the network will assume no activation function
    
    #standard getter methods: inputs, weights, biases, outputs
    def get_inputs(self):
      return self.inputs

    def get_weights(self):
      return self.weights
    
    def get_biases(self):
      return self.biases

    def get_outputs(self):
      return self.outputs

    #to string method lol
    def metrics(self):
      print("----- metrics -----")
      print("weights: {}".format(self.weights))
      print("biases: {}".format(self.biases))
      print("inputs: {}".format(self.inputs))
      print("outputs: {}".format(self.outputs))
