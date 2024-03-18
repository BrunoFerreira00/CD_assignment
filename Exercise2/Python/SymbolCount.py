def readfile(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except IOError as e:
        print("Error: {0}".format(e))
        return None

def count_symbols(text):
    result = {}
    for symbol in text:
        if symbol in result:
            result[symbol] += 1
        else:
            result[symbol] = 1
    return result

def main():
    text = readfile("example.txt")
    if text:
        result = count_symbols(text)
        total_count = sum(result.values())
        for symbol, count in result.items():
            percentage = (count / total_count) * 100
            print("{0}: {1}%".format(symbol, percentage))

if __name__ == "__main__":
    main()