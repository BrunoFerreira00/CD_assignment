import numpy as np

def binarySymmetricChannel(input_sequence, p):
    # Simulates a Binary Symmetric Channel with error probability p
    output_sequence = np.zeros(len(input_sequence))
    for i in range(len(input_sequence)):
        # If the random number is less than p, flip the bit
        if np.random.rand() < p:
            output_sequence[i] = 1 - input_sequence[i]
        else:
            output_sequence[i] = input_sequence[i]
    return output_sequence

def BER(input_sequence, output_sequence):
    # Compares the input and output sequences and returns the Bit Error Rate
    return np.sum(input_sequence != output_sequence) / len(input_sequence)

def inputSize():
        # Test the BER function with different input sizes
        input_sequence = {1024, 10240, 102400, 1024000, 10240000}
        # Set the error probability , 1 = 100% which means that all bits are flipped
        # 0.1 = 10% which means there is a 10% chance that a bit will be flipped
        p = 0.1
        for i in input_sequence:
            # Generate a random input sequence of 0s and 1s
            input_sequence = np.random.randint(0, 2, i)
            output_sequence = binarySymmetricChannel(input_sequence, p)
            print ("Input Sequence:", input_sequence)
            print("BER:", BER(input_sequence, output_sequence))

def compareFile():
    input_file = open("test.txt", "r")
    differentSymbols = 0
    p = 0.1
    for line in input_file:
        # Convert the string to an array of integers
        input_sequence = np.array([int(x) for x in line.strip() if x.isdigit()])
        # Simulate the Binary Symmetric Channel
        output_sequence = binarySymmetricChannel(input_sequence, p)
        # Count the number of different symbols
        differentSymbols += np.sum(input_sequence != output_sequence)
    input_file.close()
    print("Different Symbols:", differentSymbols)
    

def main():
    inputSize()
    compareFile()

if __name__ == "__main__":
    main()
