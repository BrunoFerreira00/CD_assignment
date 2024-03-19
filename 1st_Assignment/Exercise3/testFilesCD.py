#Exercise 3_a)

import os
import math

#Function to calculate the entropy = H(X) = -Σ p(x) * log2(p(x))
def entropy(probability):
    return sum(-p * math.log2(p) for p in probability if p > 0)

def readfile(filename):
    try:
        with open(filename, 'r') as file:
            #Just reads the files that are text based
            textExtension = ('.txt', '.c', '.java', '.kt','.htm')
            if filename.endswith(textExtension):
                 return file.read()
            else:
                return ''
    except IOError as e:
        print("Error: {0}".format(e))
        return None
        
   #Simple histogram using dictionary
def histogram(text):
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

#Function to open all files in the folder and calculate the entropy and histogram for each
def openAllFiles():
    for files in os.listdir('TestFilesCD'):
        text = readfile(os.path.join('TestFilesCD/' + files))
        hist = histogram(text)
        total = sum(hist.values())
        probability = {key : (value / total) for key , value in hist.items()}
        print('Entropy for file ' + files + ' is: ' + str(entropy(probability.values())))
        print('Histogram for file ' + files + ' is: ' + str(hist))
        print('---------------------------------------------')

def main():
    openAllFiles()

if __name__ == "__main__":
    main()
