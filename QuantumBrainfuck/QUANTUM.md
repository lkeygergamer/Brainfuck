# QUANTUM.md

## Como simular um universo quântico em Brainfuck (ou pelo menos fingir)

### 1. Qubits
Cada célula da fita é um qubit. O valor 0 representa |0⟩, o valor 1 representa |1⟩. Se for outro valor, é bug quântico (ou superposição, depende do ponto de vista).

### 2. Superposição
Loops como `[->+++<]` "espalham" o valor de uma célula para outras, simulando a incerteza e a multiplicidade de estados.

### 3. Portas Quânticas
- **Hadamard**: Sequências como `>++>++>++>++<<<<` e `[->>+>+<<<]` embaralham valores, fingindo criar superposição.
- **CNOT/Entrelaçamento**: `[->+<]` e variantes copiam valores entre células, simulando o entrelaçamento quântico.

### 4. Medição
O comando `.` imprime o valor da célula, colapsando o "estado quântico" para um valor clássico (ou um caractere aleatório).

### 5. Decoerência
Sequências como `[-]++++++++++.[-]` zeram tudo e imprimem um valor, simulando o colapso do universo (ou só um reset).

### 6. Observador Quântico
Qualquer comando que mexe na fita pode ser visto como o "ato de observar", mudando o estado do sistema.

---

**Nota:** Nada aqui é quântico de verdade, mas tudo é diversão garantida!

