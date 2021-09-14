"""
All current activator functions are here, but more can be added.
"""

#standard class: no inherticance
class ActivationFunctions:
  
  #regularized ReLU activator
  @staticmethod
  def relu(x):
    return nm.maximum(0, x)
  
  #derivative for ReLU
  @staticmethod
  def relu_gradient(x):
    return 1 if (x > 0) else 0

  #regularized sigmoid activator
  @staticmethod
  def sigmoid(x):
    return 1/(1+nm.exp(-x))

  #derivative for sigmoid
  @staticmethod
  def sigmoid_gradient(x):
    return ActivationFunctions.sigmoid(x) * (1 - ActivationFunctions.sigmoid(x))
  
  #swish activation
  @staticmethod
  def swish(x):
    return x*ActivationFunctions.sigmoid(x)
  
  @staticmethod
  def swish_gradient(x):
    return ActivationFunctions.swish(x) + ActivationFunctions.sigmoid(x)*(1 - ActivationFunctions.swish(x))
  
  
