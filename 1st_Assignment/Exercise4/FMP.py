# Exercise : 4 . a)

# Get numpy for random choice
import numpy as np
import pprint
import math 


# Define the entropy function
def entropy(probability):
    return -sum([p * math.log2(p) for p in probability if p > 0])

# Generate symbols based on the fmp where the keys will be the symbols and the values the probabilities ex: {'A': 0.5}
def generateSymbols(FMP,N):
    symbols = list(FMP.keys())
    probabilities = list(FMP.values())
    # Generate N symbols based on the probabilities
    return np.random.choice(symbols, N, p=probabilities)

# Calculate the entropy based on the FMP
def calculateEntropy(symbolsDic):
    symbols = list(symbolsDic)
    frequency = {x: symbols.count(x) for x in symbols}
    # Calculate the probability of each symbol
    probability = {x: frequency[x] / len(symbols) for x in frequency}
    # Calculate the entropy based on the probability
    return entropy(probability.values())
    


FMP = {'A': 0.5, 'B': 0.25, 'C': 0.125 , 'D': 0.125}

N = 1000

def main():
    gen = generateSymbols(FMP,N)
    entropyValue = calculateEntropy(gen)
    pprint.pprint(gen)
    print("Entropy:", entropyValue)


if __name__ == "__main__":
    main()

