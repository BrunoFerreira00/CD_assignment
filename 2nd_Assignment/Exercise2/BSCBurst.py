import numpy as np

# Length of the error burst
L = [32]

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

def xor_division(dividend, divisor):
    # Make copies of the dividend and divisor for processing
    dividend = dividend.copy()
    divisor = divisor.copy()
    
    # Get the lengths of the dividend and divisor
    len_dividend = len(dividend)
    len_divisor = len(divisor)
    
    # Loop over the dividend and perform XOR division
    for i in range(len_dividend - len_divisor + 1):
        if dividend[i] == 1:
            for j in range(len_divisor):
                dividend[i + j] ^= divisor[j]
    
    # The remainder is the CRC
    remainder = dividend[-(len_divisor-1):]
    return remainder

def append_crc(sequence, polynomial):
    # Append zeros to the sequence to make space for the CRC bits
    padded_sequence = np.concatenate([sequence, np.zeros(len(polynomial) - 1, dtype=int)])
    # Get the CRC bits
    crc = xor_division(padded_sequence, polynomial)
    # Append the CRC to the original sequence
    return np.concatenate([sequence, crc])

def crc_check(sequence, polynomial):
    # Perform XOR division on the received sequence
    remainder = xor_division(sequence, polynomial)
    # Check if the remainder is all zeros
    # If it's all zeros it means that the CRC check is successful and that there are no errors, otherwise there are errors
    return np.all(remainder == 0)

def simulateBurstError(sequence, p):
    for bit in L:
        print("Simulation with burst error for p =", p, "and Length of burst =", bit)
        output_sequence = bsc(sequence, p, bit)
        print("input: ", sequence)
        print("output: ", output_sequence)
        different_bits = np.sum(sequence != output_sequence)
        print("Number of different bits: ", different_bits)
        print("-"*50)   

def simulateCRC(sequence, p, polynomial):
    for bit in L:
        print("Simulation with CRC for p =", p, "and Length of burst =", bit)
        output_sequence = bsc(sequence, p, bit)
        print("input: ", sequence)
        print("output: ", output_sequence)
        different_bits = np.sum(sequence != output_sequence)
        print("Number of different bits: ", different_bits)
        print("CRC Check: ", crc_check(output_sequence, polynomial))
        print("-"*50)

def main():
    # CRC32 polynomial
    polynomial = np.array([1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1], dtype=int)
    
    # Get a random sequence of 64 bits
    # sequence = np.random.randint(0, 2, 64)
    sequence = [0,0,0,0,0,0,0,1]
    
    # Append CRC to the sequence
    sequence_with_crc = append_crc(sequence, polynomial)
    
    # Simulate burst errors and CRC checking
    #simulateBurstError(sequence_with_crc, 0.1)
    # Since CRC is extremely reliable to detect errors, the probability needs to be around 0.01 to get examples of errors and no errors
    # Anything from above from 0.05 CRC always detects errors (from my tests)
    simulateCRC(sequence_with_crc, 0.1, polynomial)

if __name__ == "__main__":
    main()
