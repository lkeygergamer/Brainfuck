# Exemplo de circuito quântico real usando Qiskit
# Requer: pip install qiskit

from qiskit import QuantumCircuit, Aer, execute

# Cria um circuito com 1 qubit e 1 bit clássico
qc = QuantumCircuit(1, 1)

# Aplica uma porta Hadamard (superposição)
qc.h(0)

# Mede o qubit
qc.measure(0, 0)

# Executa a simulação
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=10).result()
counts = result.get_counts(qc)

print("Resultados da medição (superposição):")
print(counts) 