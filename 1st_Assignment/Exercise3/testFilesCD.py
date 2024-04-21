#Exercise 3_a)

import os
import math
import matplotlib.pyplot as plt
import zipfile

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

def plotHistogram(hist, filename):
    # Create a histogram based on the fequency(y-axis) of each character(x-axis)
    plt.bar(hist.keys(), hist.values(), color='g')
    plt.title("Histogram for file: " + filename)
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.show()

#Function to open all files in the folder and calculate the entropy and histogram for each
def openAllFiles():
    with zipfile.ZipFile("TestFilesCD.zip", 'r') as zip_ref:
            zip_ref.extractall("TestFilesCDFolder")
    for files in os.listdir('TestFilesCDFolder'):
        text = readfile(os.path.join('TestFilesCDFolder/' + files))
        hist = histogram(text)
        total = sum(hist.values())
        probability = {key : (value / total) for key , value in hist.items()}
        print('Entropy for file ' + files + ' is: ' + str(entropy(probability.values())))
        print('Histogram for file ' + files + ' is: ' + str(hist))
        print('---------------------------------------------')
        plotHistogram(hist, files)

def main():
    openAllFiles()
    # Since the code is running in the terminal, made this to keep the plot open
    # It will show the plot until the user closes it, after that it will show the next file plot
    plt.show()

if __name__ == "__main__":
    main()
