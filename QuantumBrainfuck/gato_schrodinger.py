import random
import os
import sys

from bf_interpreter import run_brainfuck

# Caminhos dos arquivos
vivo_path = os.path.join(os.path.dirname(__file__), 'gato_schrodinger_vivo.bf')
morto_path = os.path.join(os.path.dirname(__file__), 'gato_schrodinger_morto.bf')

# Escolhe aleatoriamente
escolha = random.choice(['vivo', 'morto'])

if escolha == 'vivo':
    with open(vivo_path, 'r', encoding='utf-8') as f:
        code = ''.join([c for c in f.read() if c in '><+-.,[]'])
    print('Resultado do experimento: ', end='')
    run_brainfuck(code)
    print(' (Gato de Schrödinger: VIVO)')
else:
    with open(morto_path, 'r', encoding='utf-8') as f:
        code = ''.join([c for c in f.read() if c in '><+-.,[]'])
    print('Resultado do experimento: ', end='')
    run_brainfuck(code)
    print(' (Gato de Schrödinger: MORTO)') 