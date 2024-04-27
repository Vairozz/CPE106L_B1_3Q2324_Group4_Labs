import statistics

def getAverage(scores):
    return statistics.mean(scores)

def getMedian(scores):
    return statistics.median(scores)

def getMode(scores):
    return statistics.mode(scores)

# Asking for input
input_str = input("Enter a list of numbers separated by spaces: ")
scores = [float(x) for x in input_str.split()]

print("Mean:", getAverage(scores))
print("Median:", getMedian(scores))
print("Mode:", getMode(scores))

