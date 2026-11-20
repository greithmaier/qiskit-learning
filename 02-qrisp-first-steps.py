from qrisp import QuantumFloat, QuantumVariable

a = QuantumFloat(2)         # create a quantum-number resgister with 2 qubits  
a[:] = 2                    # initialize the register with the value 2
b = a + a                   # b is just a python variable. use it  to add a to itself.
print(b.get_measurement())  # expect 2 + 2 = 4 as output :)
