import numpy as np
input_data = np.array([2,3])
weights={'node_0':np.array([1,1]),
         'node_1':np.array([-1,1]),
         'output':np.array([2,-1])
         }
node_0_input= (input_data * weights['node_0']).sum()
node_0_output= np.tanh(node_0_input)
node_1_input=(input_data * weights['node_1']).sum()
node_1_output=np.tanh(node_1_input)
hidden_later_values = np.array([node_0_output,node_1_output])
print(f"The hidden layer values are ",hidden_later_values)
output = (hidden_later_values * weights['output']).sum()
print (f"The output is ",output)
input("Press any key to continue...")