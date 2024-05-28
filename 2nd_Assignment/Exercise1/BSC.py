import numpy as np

# Read file
def process_file(file_name):
    with open(file_name) as f:
        data = f.read()
    return data

# Convert symbols to binary
def symbol_to_binary(data):
    binary_data = []
    for symbol in data:
        # Format the symbol to 8 bits by the unicode value of each symbol
        binary_data.append(format(ord(symbol), '08b'))
    return ''.join(binary_data)

# Convert binary to symbols
def binary_to_symbol(data):
    symbols = []
    # Convert binary data to symbols , 8 bits at a time
    for i in range(0, len(data), 8):
        # Convert 8 bits to unicode value and then to symbol
        symbols.append(chr(int(data[i:i+8], 2)))
    return ''.join(symbols)
   
# Probability of error
p = [0.1, 0.25, 0.35, 0.75]

def bsc(data, p):
    # Create an array of zeros with the same length as the data
    output_sequence = np.zeros(len(data), dtype=int)
    for i in range(len(data)):
        # If the random number is less than p, flip the bit
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
    # Compare the input and output symbols and count the number of different symbols
    num_different_symbols = sum(1 for a, b in zip(input_symbols, output_symbols) if a != b)
    return num_different_symbols

# Simulation without control
def simulationWithoutControl(file_name):
    input_data = process_file(file_name)
    binary_data = symbol_to_binary(input_data)
    
    for prob in p:
        print("Simulation without control for p =", prob)
        output_sequence = bsc(binary_data, prob)
        output_data = binary_to_symbol(''.join(map(str, output_sequence)))
        
        binary_array = np.array(list(binary_data), dtype=int)  # Convert binary data to array
        output_array = np.array(output_sequence)  # Convert output sequence to array
        
        num_different_symbols = compare_symbols(input_data, output_data)
        print('BER` for p =', prob, 'is', ber(binary_array, output_array))
        print('Different symbols for p =', prob, 'is', num_different_symbols)  
        print('-'*20)  
 

# Repetition code(3, 1) for error correction
def repetitionEncoded(data):
        encoded_data = ''
        # Repeat each bit 3 times, since we are using (3, 1) repetition code
        # With 1 bit we have a message of 3 bits, soo we repeat each bit 3 times
        for i in range(0, len(data)):
            encoded_data += data[i] * 3
        return encoded_data

def repetitionDecoded(data):
    decoded_data = ''
    for i in range(0, len(data), 3):
        # Take 3 bits at a time
        bits = data[i:i+3]
        # If the 3 bits have more 1's than 0's, then the decoded bit is 1 else 0
        # Because of majority voting, the bit with the most occurence is the correct bit
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
        print("Simulation with repetition for p =", prob)
        encoded_data = repetitionEncoded(binary_data)
        output_sequence = bsc(encoded_data, prob)
        decoded_data = repetitionDecoded(''.join(map(str, output_sequence)))  # Corrected decoding function
        output_data = binary_to_symbol(decoded_data)
        
        binary_array = np.array(list(binary_data), dtype=int)  # Convert binary data to array
        output_array = np.array(list(decoded_data), dtype=int)  # Convert decoded data to array
        
        num_different_symbols = compare_symbols(input_data, output_data)
        print('BER for p =', prob, 'is', ber(binary_array, output_array))
        print('Different symbols for p =', prob, 'is', num_different_symbols)  
        print('-'*20)
## For the repetion code, since it goes by majority voting, the error rate is lower than the one without control
# Because this one is able to correct if there's just 1 error in the 3 bits, however, if there are 2 errors, it won't be able to correct it


def hammingEncoded(data):
    # Create a 7 bit Hamming code
    # The first 4 bits are the data bits, the next 3 bits are the parity
    encoded_data = ''
    for i in range(0, len(data), 4):
        # Take 4 bits at a time
        bits = data[i:i+4]
        # Calculate the parity bits (this xors are in the pdf given by the teacher)
        p0 = str(int(bits[1]) ^ int(bits[2]) ^ int(bits[3]))
        p1 = str(int(bits[0]) ^ int(bits[1]) ^ int(bits[3]))
        p2 = str(int(bits[0]) ^ int(bits[2]) ^ int(bits[3]))
        # Append the data bits and parity bits
        encoded_data += bits + p0 + p1 + p2
    return encoded_data

def hammingDecoded(data):
    decoded_data = ''
    for i in range(0, len(data), 7):
        bits = data[i:i+7]
        # Get the parity bits again to check syndrome
        p0 = str(int(bits[1]) ^ int(bits[2]) ^ int(bits[3]))
        p1 = str(int(bits[0]) ^ int(bits[1]) ^ int(bits[3]))
        p2 = str(int(bits[0]) ^ int(bits[2]) ^ int(bits[3]))
        # Get syndrome
        s = p0 + p1 + p2
        # Verify if there is an error, if it's different from 000, then there is an error
        if s != '000':
            error_pos = int(s, 2)
            # Correct the error
            if error_pos < len(bits):
                bits = bits[:error_pos] + str(1 - int(bits[error_pos])) + bits[error_pos+1:]
        decoded_data += bits[0] + bits[1] + bits[2] + bits[3]
    return decoded_data


def simulationWithHamming(file_name):
    input_data = process_file(file_name)
    binary_data = symbol_to_binary(input_data)
    
    for prob in p:
        print("Simulation with Hamming for p =", prob)
        encoded_data = hammingEncoded(binary_data)
        output_sequence = bsc(encoded_data, prob)
        decoded_data = hammingDecoded(''.join(map(str, output_sequence)))  # Corrected decoding function
        output_data = binary_to_symbol(decoded_data)
        
        binary_array = np.array(list(binary_data), dtype=int)  # Convert binary data to array
        output_array = np.array(list(decoded_data), dtype=int)  # Convert decoded data to array
        
        num_different_symbols = compare_symbols(input_data, output_data)
        print('BER for p =', prob, 'is', ber(binary_array, output_array))
        print('Different symbols for p =', prob, 'is', num_different_symbols)  
        print('-'*20)
## The hamming code has a higher BER , because it depends on the syndrome to correct the error
# If there are 2 errors in the 7 bits, it won't be able to correct it, because the syndrome will be the same as if there was just 1 error
# Also to not detect errors, the syndrome needs to be 000, if it's different from that, it will detect an error
# Because of this it has a higher BER than the repetition code , but a lower BER than the one without control

def main():
    file_name = 'test.txt'  
    simulationWithoutControl(file_name)
    simulationWithRepetition(file_name)
    simulationWithHamming(file_name)
if __name__ == "__main__":
    main()
