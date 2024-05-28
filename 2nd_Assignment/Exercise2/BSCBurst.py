
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
                # If the index of the bit plus the size of the burst is less than the length of the data, flip the bit
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

def CRC(data, generator):
    



def main():
    # Get a random sequence of 100 bits
    sequence = np.random.randint(0, 2, 100)
    simulateBurstError(sequence, 0.1)


if __name__ == "__main__":
    main()