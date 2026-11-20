import numpy as np
from qiskit import QuantumCircuit


# Some qiskit code to keep in mind
#qc.p(np.pi / 2, 0)  # add quantum phase (= S-Gate or 90° z-axis rotatation or T*T)
#qc.cx(0, 2)         # 0th-qubit-Controlled-NOT gate on 2nd qubit


# 1.1 Testing out some gates on a simgle qubit
qc_1 = QuantumCircuit(1)     # initially, the qubits are always in state |0>
qc_1.x(0)                     # apply X gate to the 0th qubit, now the state is |1>
qc_1.h(0)                     # apply H gate to the 0th qubit (generate superposition)
qc_1.t(0)                     # apply T gate to the 0th qubit to add 45-degree phase
qc_1.h(0)                     # apply H gate to the 0th qubit


# 1.2 Testing out some gates on two qubits
qc_2 = QuantumCircuit(2)
qc_2.h(0)
qc_2.cx(0, 1)                 # 0th-qubit-Controlled-NOT gate on 1st qubit. 
                              #   0 & 1 are now entangled.


# 1.3 Testing more entanglement
qc_3 = QuantumCircuit(3)
qc_3.h(0)        # apply H gate to the 0th qubit
qc_3.cx(0, 1)    # apply CNOT gate with 0th qubit as control and 1st qubit as target
qc_3.h(1)        # apply H gate to the 1st qubit
qc_3.cx(1, 2)    # apply CNOT gate with 1st qubit as control and 2nd qubit as target
# the 0th and 1st qubits are now entangled, and the 1st and 2nd qubits are also entangled.
# the 0th and 2nd qubits are indirectly entangled through the 1st qubit.
# TODO: understand output fully... how can i proove entanglement 0 <=> 2?


# 2. Add the classical output in the form of measurement of all qubits
# >>> MAKE SURE TO MEASURE THE QC THAT YOU WANT TO SEE <<<
# qc_X is left intact, qc_measured  is  new circuit description
qc_measured = qc_3.measure_all(inplace=False)   


# 3. Execute using the Sampler primitive
from qiskit.primitives import StatevectorSampler
sampler = StatevectorSampler()
job = sampler.run([qc_measured], shots=10000)
result = job.result()
print(f" > Counts: {result[0].data['meas'].get_counts()}")
print(qc_measured.draw(output="text"))  # >>> Draw Circuit Diagram <<< (this is very nice)


# 4. Graphical output
from qiskit.visualization import plot_histogram
counts = result[0].data["meas"].get_counts()
fig = plot_histogram(counts)
fig.savefig("histogram.png")  # Save the histogram as a PNG file