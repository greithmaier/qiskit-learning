from qrisp import QuantumFloat, QuantumVariable

a = QuantumFloat(2)   # create a quantum-number resgister with 2 qubits  
a[:] = 2
b = a + a
b.get_measurement()
