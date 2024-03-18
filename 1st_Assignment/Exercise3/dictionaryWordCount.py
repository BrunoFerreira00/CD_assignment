#Exercise 3 line b) , contains both i) and ii)
#i)

#Simple import just to make the dictionary more readable in the console
import pprint

#Basic function to read files
def readfile(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
        #Error handling
    except IOError as e:
        print("Error: {0}".format(e))
        return None
    
#Basic function to read each char and use him as a key , and his total count as a value in a dictionary
def count_chars(text):
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


#Function to combine the two dictionaries
def combine_counts(count1, count2):
    combined = count1.copy()
    for key in count2:
        if key in combined:
            #If the key is already in the dictionary , add the value to the existing one
            combined[key] += count2[key]
        else:
            #If the key is not in the dictionary , add it
            combined[key] = count2[key]
    return combined

#Function that reads the files , get the count for each , and then combines them into a singular dictionary
def getBothCounts():
    portuguese = readfile('ListaPalavrasPT.txt')
    english = readfile('ListaPalavrasEN.txt')
    portuguese_count = count_chars(portuguese)
    english_count = count_chars(english)
    result = combine_counts(portuguese_count, english_count)
    total = sum(result.values())
    #returning the combined dictionary with values as percentage
    return {key : (value / total * 100) for key , value in result.items()}

#Function that gets the most 5 common chars but deletes the special "\n" char
def getMostCommon(dictionary):
    result = {}
    #While dictionary doesn't have 5 elements ,get the max value and add it to the result after delete it from original
    while len(result) < 5:
        max_value = max(dictionary, key=dictionary.get)
        #If the max value is a '\n' char , delete it , and continue searching
        if (max_value == '\n'):
            del dictionary[max_value]
            continue
        #Add the max value to the result and delete it from the dictionary
        result[max_value] = dictionary[max_value]
        del dictionary[max_value]
    return result

#ii)

def countPairsOfChars(text):
    result = {}
    for i in range(len(text) - 1):
        #i represents the start of the pair , i+2 the end of the pair (substring of length 2)
        pair = text[i:i + 2]
        if pair in result:
            result[pair] += 1
        else:
            result[pair] = 1
    return result

def getBothPairs():
    portuguese = readfile('ListaPalavrasPT.txt')
    english = readfile('ListaPalavrasEN.txt')
    portuguese_count = countPairsOfChars(portuguese)
    english_count = countPairsOfChars(english)
    result = combine_counts(portuguese_count, english_count)
    total = sum(result.values())
    return {key : (value / total * 100) for key , value in result.items()}

def getMostCommonPairs(dictionary):
    result = {}
    while len(result) < 5:
        max_value = max(dictionary, key=dictionary.get)
        #This line verifies if the first or the second char is the '\n' char , if it is , delete it and continue searching
        if (max_value[0] == '\n' or max_value[1] == '\n'):
            del dictionary[max_value]
            continue
        result[max_value] = dictionary[max_value]
        del dictionary[max_value]
    return result


def main():
    #i)
    dictionary = getBothCounts()
    #syntax to pretty print a dictionary , using it since the dictionary is too big to be readable
    pprint.pprint(dictionary)
    print("Most common chars:", getMostCommon(dictionary))

    #ii)
    '''
    This line is commented since the dictionary is too big to be readable
    Since there are about 84 singular chars present, which means there's beetween 84^2 and 84*83 pairs
    Because of this , it also could take a while until it finishes
    So just the 5 most common pairs are printed
    '''
    dictionary = getBothPairs()
    #pprint.pprint(dictionary)
    print("Most common pairs:", getMostCommonPairs(dictionary))




if __name__ == '__main__':  
    main()
    