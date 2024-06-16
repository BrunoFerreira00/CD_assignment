import numpy as np
import os

# Read file
def process_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read()
    return data

# Convert symbols to binary
def symbol_to_binary(data):
    binary_data = []
    for symbol in data:
        binary_data.append(format(ord(symbol), '08b'))
    return ''.join(binary_data)

# Convert binary to symbols
def binary_to_symbol(data):
    symbols = []
    for i in range(0, len(data), 8):
        symbols.append(chr(int(data[i:i+8], 2)))
    return ''.join(symbols)

# Probability of error
p = [0.05, 0.15, 0.35, 0.8]

def bsc(data, p):
    output_sequence = np.zeros(len(data), dtype=int)
    for i in range(len(data)):
        if np.random.rand() < p:
            output_sequence[i] = 1 - int(data[i])
        else:
            output_sequence[i] = int(data[i])
    return output_sequence

# Bit error rate
def ber(input, output):
    return np.sum(input != output) / len(input)

# Compare symbols
def compare_symbols(input_symbols, output_symbols):
    num_different_symbols = sum(1 for a, b in zip(input_symbols, output_symbols) if a != b)
    return num_different_symbols

# Simulation without control
def simulationWithoutControl(file_name):
    input_data = process_file(file_name)
    binary_data = symbol_to_binary(input_data)
    
    for prob in p:
        print("Without control for p =", prob)
        output_sequence = bsc(binary_data, prob)
        output_data = binary_to_symbol(''.join(map(str, output_sequence)))
        
        binary_array = np.array(list(binary_data), dtype=int)
        output_array = np.array(output_sequence)
        
        num_different_symbols = compare_symbols(input_data, output_data)
        print('BER for p =', prob, 'is', ber(binary_array, output_array))
        print('Different symbols for p =', prob, 'is', num_different_symbols)  
        print('-'*20)
        
        # Create directory if not exists
        os.makedirs('output_without_control', exist_ok=True)
        
        # Write the output data to a file
        with open(f'output_without_control/output_without_control_p_{prob}.txt', 'w', encoding='utf-8') as f:
            f.write(output_data)

# Repetition code(3, 1) for error correction
def repetitionEncoded(data):
    encoded_data = ''
    for i in range(0, len(data)):
        encoded_data += data[i] * 3
    return encoded_data

def repetitionDecoded(data):
    decoded_data = ''
    for i in range(0, len(data), 3):
        bits = data[i:i+3]
        if bits.count('1') > 1:
            decoded_data += '1'
        else:
            decoded_data += '0'
    return decoded_data

# Simulation with repetition
def simulationWithRepetition(file_name):
    input_data = process_file(file_name)
    binary_data = symbol_to_binary(input_data)
    
    for prob in p:
        print("Repetition for p =", prob)
        encoded_data = repetitionEncoded(binary_data)
        output_sequence = bsc(encoded_data, prob)
        decoded_data = repetitionDecoded(''.join(map(str, output_sequence)))
        output_data = binary_to_symbol(decoded_data)
        
        binary_array = np.array(list(binary_data), dtype=int)
        output_array = np.array(list(decoded_data), dtype=int)
        
        num_different_symbols = compare_symbols(input_data, output_data)
        print('BER for p =', prob, 'is', ber(binary_array, output_array))
        print('Different symbols for p =', prob, 'is', num_different_symbols)  
        print('-'*20)
        
        # Create directory if not exists
        os.makedirs('output_with_repetition', exist_ok=True)
        
        # Write the output data to a file
        with open(f'output_with_repetition/output_with_repetition_p_{prob}.txt', 'w', encoding='utf-8') as f:
            f.write(output_data)

def hammingEncoded(data):
    encoded_data = ''
    for i in range(0, len(data), 4):
        bits = data[i:i+4]
        p0 = str(int(bits[1]) ^ int(bits[2]) ^ int(bits[3]))
        p1 = str(int(bits[0]) ^ int(bits[1]) ^ int(bits[3]))
        p2 = str(int(bits[0]) ^ int(bits[2]) ^ int(bits[3]))
        encoded_data += bits + p0 + p1 + p2
    return encoded_data

def hammingDecoded(data):
    decoded_data = ''
    for i in range(0, len(data), 7):
        bits = list(data[i:i+7])
        p0 = bits[4]
        p1 = bits[5]
        p2 = bits[6]
        s0 = str(int(bits[1]) ^ int(bits[2]) ^ int(bits[3]) ^ int(p0))
        s1 = str(int(bits[0]) ^ int(bits[1]) ^ int(bits[3]) ^ int(p1))
        s2 = str(int(bits[0]) ^ int(bits[2]) ^ int(bits[3]) ^ int(p2))
        s = s0 + s1 + s2

        syndrome = {
            '011': 0,
            '110': 1,
            '101': 2,
            '111': 3,
            '100': 4,
            '010': 5,
            '001': 6,
            '000': -1
        }
        
        if s != '000':
            error_position = syndrome[s]
            bits[error_position] = str(1 - int(bits[error_position]))
        
        decoded_data += ''.join(bits[:4])
    return decoded_data

def simulationWithHamming(file_name):
    input_data = process_file(file_name)
    binary_data = symbol_to_binary(input_data)
    
    for prob in p:
        print("Hamming for p =", prob)
        encoded_data = hammingEncoded(binary_data)
        output_sequence = bsc(encoded_data, prob)
        decoded_data = hammingDecoded(''.join(map(str, output_sequence)))
        output_data = binary_to_symbol(decoded_data)
        
        binary_array = np.array(list(binary_data), dtype=int)
        output_array = np.array(list(decoded_data), dtype=int)
        
        num_different_symbols = compare_symbols(input_data, output_data)
        print('BER for p =', prob, 'is', ber(binary_array, output_array))
        print('Different symbols for p =', prob, 'is', num_different_symbols)  
        print('-'*20)
        
        # Create directory if not exists
        os.makedirs('output_with_hamming', exist_ok=True)
        
        # Write the output data to a file
        with open(f'output_with_hamming/output_with_hamming_p_{prob}.txt', 'w', encoding='utf-8') as f:
            f.write(output_data)

def main():
    file_name = 'test.txt'  
    simulationWithoutControl(file_name)
    simulationWithRepetition(file_name)
    simulationWithHamming(file_name)

if __name__ == "__main__":
    main()
