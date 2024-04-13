# Exercise : 4 . a)

# Get numpy for random choice
import numpy as np
import pprint
import math 


# Define the entropy function
def entropy(p):
    return -p * math.log2(p) 

# Generate symbols based on the fmp where the keys will be the symbols and the values the probabilities ex: {'A': 0.5}
def generateSymbols(FMP,N):
    symbols = list(FMP.keys())
    probabilities = list(FMP.values())
    # Generate N symbols based on the probabilities
    return np.random.choice(symbols, N, p=probabilities)

# Calculate the entropy based on the FMP
def calculateEntropy(FMP):
    result = 0
    for p in FMP.values():
        result += entropy(p)
    return result


FMP = {'A': 0.5, 'B': 0.3, 'C': 0.2}

N = 20

def main():
    gen = generateSymbols(FMP,N)
    entropy = calculateEntropy(FMP)
    pprint.pprint(gen)
    print("Entropy:", entropy)


if __name__ == "__main__":
    main()

