class DenseLayer:
    
    #constructor
    def __init__(self, input_number, neuron_number):
      self.weights = 0.10 * nm.random.randn(input_number, neuron_number) #generates randomized weights in the input shapes
      self.biases = nm.zeros((1, neuron_number)) #regularizes the bias per neuron
    
    def forward(self, inputs):
      self.inputs = inputs #self explanatory
      """
      generates the outputs: the forward propagation takes the inputs from this layer (which could also be the outputs
      from a previous layer) multiplies them by the sum of the weights and adds the bias
      """
      self.outputs = nm.dot(self.inputs, self.weights) + self.biases 
    
    #getter methods: inputs, weights, biases, outputs
    def get_inputs(self):
      return self.inputs

    def get_weights(self):
      return self.weights
    
    def get_biases(self):
      return self.biases

    def get_outputs(self):
      return self.outputs

    #regular to-string method here for the metrics of the layer
    def metrics(self):
      print("----- metrics -----")
      print("weights: {}".format(self.weights))
      print("biases: {}".format(self.biases))
      print("inputs: {}".format(self.inputs))
      print("outputs: {}".format(self.outputs))
