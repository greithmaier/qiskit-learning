from qrisp import *
from matplotlib import pyplot as plt

# This example creates a GHZ state, replace it with your own code
qv = QuantumVariable(3)
h(qv[0])
cx(qv[0], qv[1])
cx(qv[0], qv[2])

# Execute it on the quantum computing backend
# Transpilation is taken care of automatically
result = qv.get_measurement(backend = quantum_computer)

# Print and plot the result
print(result)

plt.bar(result.keys(), result.values())
plt.xlabel('Measurement outcomes')
plt.ylabel('Probability')
plt.show()