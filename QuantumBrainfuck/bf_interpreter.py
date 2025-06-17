# Interpretador Brainfuck simples em Python 3
# Uso: python bf_interpreter.py arquivo.bf

import sys

MEM_SIZE = 30000

def run_brainfuck(code, input_stream=None):
    tape = [0] * MEM_SIZE
    ptr = 0
    pc = 0
    output = ''
    loop_stack = []
    code_len = len(code)
    input_buffer = list(input_stream) if input_stream else []

    # Pré-processa os loops para saltos rápidos
    loop_map = {}
    temp_stack = []
    for i, c in enumerate(code):
        if c == '[':
            temp_stack.append(i)
        elif c == ']':
            start = temp_stack.pop()
            loop_map[start] = i
            loop_map[i] = start

    while pc < code_len:
        cmd = code[pc]
        if cmd == '>':
            ptr = (ptr + 1) % MEM_SIZE
        elif cmd == '<':
            ptr = (ptr - 1) % MEM_SIZE
        elif cmd == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '.':
            print(chr(tape[ptr]), end='')
            output += chr(tape[ptr])
        elif cmd == ',':
            if input_buffer:
                tape[ptr] = ord(input_buffer.pop(0))
            else:
                tape[ptr] = 0
        elif cmd == '[':
            if tape[ptr] == 0:
                pc = loop_map[pc]
        elif cmd == ']':
            if tape[ptr] != 0:
                pc = loop_map[pc]
        pc += 1
    return output

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python bf_interpreter.py arquivo.bf')
        sys.exit(1)
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        code = ''.join([c for c in f.read() if c in '><+-.,[]'])
    run_brainfuck(code) 