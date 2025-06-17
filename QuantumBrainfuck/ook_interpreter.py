# Interpretador Ook! em Python
# Uso: python ook_interpreter.py arquivo.ook
# Ook! é uma linguagem esotérica baseada em Brainfuck

import sys
import re
from bf_interpreter import run_brainfuck

OOK_TO_BF = {
    'Ook. Ook?': '>',
    'Ook? Ook.': '<',
    'Ook. Ook.': '+',
    'Ook! Ook!': '-',
    'Ook! Ook.': '.',
    'Ook. Ook!': ',',
    'Ook! Ook?': '[',
    'Ook? Ook!': ']',
}

def ook_to_bf(ook_code):
    # Remove tudo que não seja Ook! Ook? Ook.
    tokens = re.findall(r'(Ook[.!?] Ook[.!?])', ook_code)
    bf_code = ''.join([OOK_TO_BF.get(tok, '') for tok in tokens])
    return bf_code

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python ook_interpreter.py arquivo.ook')
        sys.exit(1)
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        ook_code = f.read()
    bf_code = ook_to_bf(ook_code)
    run_brainfuck(bf_code) 