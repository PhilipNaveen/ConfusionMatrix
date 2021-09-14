import numpy as nm

class MultilayerPerceptron(object):

  #constructor with *args & **kwargs
  def __init__(self, layers):
    self.layers, self.forward_propagations, self.backward_propagations = list(layers), 0, 0

  #forward
  def forward_propagation(self, input_values):
    #full neural-network forward propagation
    #parse array or whatever value inserted

    #iterate through and propagate
    for j in range(int(len(self.layers))):
      if (j == 0): 
        self.layers[j].forward(input_values)
      else: self.layers[j].forward(self.layers[j-1].get_outputs())
      self.forward_propagations += 1

  #backpropagation - adjust synaptic weights in the network
  def backward_propagation(self, loss):
    #for training with loss
    for layer in self.layers: 
      layer.backward(loss); self.backward_propagations += 1

    #return output values
    return self.layers[-1].get_outputs()

  #total network metrics
  def total_network_metrics(self): 
    for layer in self.layers: layer.metrics()

  #basic getter methods
  def get_forward_propagation_count(self):
    return self.forward_propagations
  
  def get_backward_propagation_count(self):
    return self.backward_propagations
