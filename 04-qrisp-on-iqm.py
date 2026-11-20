import os
from qrisp import QuantumFloat

# qrisp with IQM support needs python 3.13 currently => install i.e. in virtual env
# ... and then do 'pip install qrisp[iqm]'
from iqm.qrisp_iqm import IQMBackend

if not os.environ.get("IQM_TOKEN"):
    os.environ["IQM_TOKEN"] = input("IQM Resonance token: ")

if not os.environ.get("IQM_SERVER_URL"):
    os.environ["IQM_SERVER_URL"] = "https://resonance.iqm.tech"
iqm_server_url = os.environ["IQM_SERVER_URL"]
backend = IQMBackend(server_url=iqm_server_url, device_instance = "garnet")

a = QuantumFloat(2)
a[:] = 2
b = a + a

# debug the mock device
# c = QuantumFloat(2)
# c[:] = 1
# print(c.get_measurement(backend = backend, shots=2000))
# this returned {1: 0.9815, 0: 0.011, 3: 0.0065, 2: 0.001} on the real device :)
# it  cost 0.5 credits

# draw the compiled circuit via  qiskit
qc = b.qs.compile(intended_measurements=b.reg)
for qubit in b.reg:
    qc.measure(qubit, qc.add_clbit())
print(qc.to_qiskit().draw(output="text"))

# get the result and display it
result = b.get_measurement(backend = backend, shots=2000)
print(result)

# executed on IQM Garnet mock device, 2000 shots, 1 qubit, 1 measurement
# {10: 0.269, 0: 0.2555, 5: 0.24, 15: 0.2355} --> why is there no "4"? --> debug code on both devices
# this did not cost any credits, since we used the mock device.
# on mock device we seem to  be getting rubbish

# real device (cost: ): 
# {4: 0.705, 6: 0.0615, 0: 0.0425, 2: 0.038, 12: 0.0355, 14: 0.022, 5: 0.02, 8: 0.016, 3: 0.013, 1: 0.0125, 10: 0.011, 9: 0.0065, 13: 0.0055, 7: 0.005, 11: 0.003, 15: 0.003}
# we get the expected "4" with around 70.5% probability which is good enough for a realy device.
# this is raw data (only results > 10%): [ { "0100": 1410 } ] => result is encoded in classic bits :)
