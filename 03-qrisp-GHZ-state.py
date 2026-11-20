import os
from qrisp import *
from matplotlib import pyplot as plt

# This example creates a GHZ state, replace it with your own code
qv = QuantumVariable(5)
h(qv[0])
cx(qv[0], qv[1])
cx(qv[0], qv[2])
cx(qv[0], qv[3])
cx(qv[0], qv[4])

# Print and plot the result
result = qv.get_measurement()
print(result)

plt.bar(result.keys(), result.values())
plt.xlabel('Measurement outcomes')
plt.ylabel('Probability')
plt.show()