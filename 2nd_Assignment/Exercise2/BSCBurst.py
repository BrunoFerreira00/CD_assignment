
import numpy as np
# Length of the error burst
L = [2,4,6,8]

def bsc(data, p, burst_length):
    # Create a copy of the data to produce the output sequence
    output_sequence = np.array(data)
    
    # Initial bit index
    i = 0
    while i < len(data):
        if np.random.rand() < p:
            for j in range(burst_length):
                # If the index of the bit plus the size of the burst is less than the length of the data, flip the bits
                if i + j < len(data):
                    output_sequence[i + j] = 1 - output_sequence[i + j]
            # Move the index to the next bit after the burst
            i += burst_length  
        else:
            # Move the index to the next bit in case of no error
            i += 1  
    return output_sequence

def ber(input, output):
    return np.sum(input != output) / len(input)


def simulateBurstError(sequence, p):
    for bit in L:
        print("Simulation with burst error for p =", p, "and Length of burst =", bit)
        output_sequence = bsc(sequence, p, bit)
        print("input: ", sequence)
        print("output: ", output_sequence)
        different_bits = np.sum(sequence != output_sequence)
        print("Number of different bits: ", different_bits)
        print("Bit error rate: ", ber(sequence, output_sequence))
        print("-"*50)   

def crc_encode(data, gx):
    # Get the length of the data
    data_len = len(data)
    # Get the length of the generator polynomial
    polinomy_len = len(gx)
    # Append zeros to the data to be able to perform the polynomial division
    data = np.append(data, np.zeros(polinomy_len-1, dtype=int))
    # Create a copy of the data to produce the output sequence
    output_sequence = np.array(data)
    # Initial bit index
    i = 0
    while i < data_len:
        # If the bit is 1, perform the polynomial division
        if output_sequence[i] == 1:
            for j in range(polinomy_len):
                # XOR the data with the generator polynomial
                output_sequence[i+j] = output_sequence[i+j] ^ gx[j]
        # Move the index to the next bit
        i += 1
    return output_sequence

def crc_check(data, gx):
    polinomy_len = len(gx)
    # Perform polynomial division
    for i in range(len(data) - polinomy_len + 1):
        if data[i] == 1:
            for j in range(polinomy_len):
                data[i + j] ^= gx[j]
    # If the remainder is all zeros, the data is correct
    # If this returns True, the data is correct , if it returns false it means that errors were detected
    # This checks if the last polinomy_len - 1 bits are zeros
    return np.all(data[-(polinomy_len - 1):] == 0)    

def simulateCRC(sequence, p, gx):
    for bit in L:
        print("Simulation with CRC for p =", p, "and Length of burst =", bit)
        output_sequence = bsc(sequence, p, bit)
        print("input: ", sequence)
        print("output: ", output_sequence)
        different_bits = np.sum(sequence != output_sequence)
        print("Number of different bits: ", different_bits)
        print("Bit error rate: ", ber(sequence, output_sequence))
        print("CRC Check: ", crc_check(output_sequence, gx))
        print("-"*50)



def main():
    # Get a random sequence of 100 bits
    sequence = np.random.randint(0, 2, 100)
    simulateBurstError(sequence, 0.1)
    # the array of the generator polynomial means that the generator polynomial is x^7 p x^6 + x^4 + 1
    simulateCRC(sequence, 0.1, [1,1,0,1,0,0,0,1])

if __name__ == "__main__":
    main()