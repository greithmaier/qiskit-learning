import os
from qrisp import QuantumFloat
from iqm.qrisp_iqm import IQMBackend

if not os.environ.get("IQM_TOKEN"):
    os.environ["IQM_TOKEN"] = input("IQM Resonance token: ")

if not os.environ.get("IQM_SERVER_URL"):
    os.environ["IQM_SERVER_URL"] = "https://resonance.iqm.tech"
iqm_server_url = os.environ["IQM_SERVER_URL"]
backend = IQMBackend(server_url=iqm_server_url, device_instance = "garnet:mock")

a = QuantumFloat(2)
a[:] = 1
b = a + a
b.get_measurement(backend = backend, shots=2000)