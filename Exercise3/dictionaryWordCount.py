#Exercise 3 line b , contains both i) and ii)
#i)

#Simple import just to make the dictionary more readable
import pprint

#Basic function to files
def readfile(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except IOError as e:
        print("Error: {0}".format(e))
        return None
    
#Basic function to read each char and use his value as a key , and his total count as a value in a dictionary
def count_words(text):
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
            combined[key] += count2[key]
        else:
            combined[key] = count2[key]
    return combined

#Function that reads the files , gets the count for each , and then combines them
def getBothCounts():
    portuguese = readfile('ListaPalavrasPT.txt')
    english = readfile('ListaPalavrasEN.txt')
    portuguese_count = count_words(portuguese)
    english_count = count_words(english)
    result = combine_counts(portuguese_count, english_count)
    #returning the combined dictionary
    return result

#Function that gets the most 5 common chars but deletes the special "\n" char
def getMostCommon(dictionary):
    result = {}
    max_count = sum(dictionary.values())
    while len(result) < 5:
        max_value = max(dictionary, key=dictionary.get)
        result[max_value] = dictionary[max_value]
        if max_value == '\n':
            del result[max_value]
        del dictionary[max_value]
        #returning the result with value as percentage
    return {key: (value / max_count) * 100 for key, value in result.items()}

#ii)


def main():
    #i)
    dictionary = getBothCounts()
    #syntax to pretty print a dictionary , using it since the dictionary is too big to be readable
    pprint.pprint(dictionary)
    print("Most common words:", getMostCommon(dictionary))
    #ii)


if __name__ == '__main__':  
    main()
    


