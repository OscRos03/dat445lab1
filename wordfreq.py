def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            if line[start].isalpha():
                end = start
                while end < len(line) and line[end].isalpha():
                    end = end+1
                words.append(line[start:end])
                start = end
            elif line[start].isdigit():
                end = start
                while end < len(line) and line[end].isdigit():
                    end = end+1
                words.append(line[start:end])
                start = end
            elif not line[start].isalpha() and not line[start].isdigit() and not line[start].isspace():
<<<<<<< HEAD
                words.append(line[start])
                start = start + 1
=======
                end = start
                while end < len(line) and not line[end].isalpha() and not line[end].isdigit() and not line[end].isspace():
                    end = end + 1
                words.append(line[start:end])
                start = end
>>>>>>> refs/remotes/origin/master
            else:
                start = start+1
    return [word.lower() for word in words]

def countWords(words, stopWords):
    wordsDict = {}
    for word in words:
        if word not in stopWords:
            if word not in wordsDict:
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1
    return wordsDict

<<<<<<< HEAD

=======
>>>>>>> refs/remotes/origin/master
def printTopMost(frequencies, n):
    if len(frequencies) > 1:
        frequencies = sorted(frequencies.items(), key=lambda x: -x[1])
    for key, value in frequencies:
        if n > 0:
            print(key.ljust(20) + str(value).rjust(5))
<<<<<<< HEAD
            n -= 1
            
=======
            n -= 1
>>>>>>> refs/remotes/origin/master
