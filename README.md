# From first qubits to useful quantum algorithms

This repo helps to learn the basics of quantum computing with qiskit on a more fundamental quantum level and, subsequently, on qrisp on higher level of abstraction with quantum variables and high level operations. 

We implement a few basic qc single- and two-qubit  gates, some basic algorithms like Grover's search algorithm and Shor's  algorithm. We do this first locally on our machine and, afterwards, execute the actual computation on real-world quantum hardware of IonQ (charged ions) and IQM (superconducting transmon qubits).

Finally, we step  up our QC game, to be able to simulate a few basic QM or quantum chemistry problems using quantum variational algorithms.

## The  repo is  structured in the following way:

### Physics and Math Background:

TBD: create some slides

### Prerequisites: 
- Visual Studio Codewith some useful extensions (always good to  have)
- Python 3.13 (in a venv, if you run the latest python)
- install needed packages with pip. I.e.: matplotlib, qrisp, qiskit, etc.
- Create accounts on IonQ and IQM's cloud access platforms, create API keys &  store in ENV variables.

### The code examples:

#### 01-qubits-and-some-gates.py

#### 02-qrisp-first-steps.py

#### 03-qrisp-GHZ-state.py

#### 04-qrisp-on-iqm.py
