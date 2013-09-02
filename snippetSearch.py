import string, sys

def snippetSearch(query, corpus):
    """Returns the occurance of a search query

    Given a page of content with alphanumeric words, and a search phrase of N words, write an algorithm that will return the shortest snippet of content that contains all N words in any order.
    Example: The George Washington Bridge in New York City is one of the oldest bridges ever constructed. It is now being remodeled because the bridge is a landmark. City officials say that the landmark bridge effort will create a lot of new jobs in the city.
    Search Terms: Landmark City Bridge
    Result: bridge is a landmark. City"""

    #generate an inverted index
    #add all words into a hashtable with the key being the word and the value being it's index, chaining for multiple indices 
    corpusSplit = corpus.split(" ")
    removePunc = corpus.translate(None, string.punctuation)
    corpusSplitRemovePunc = removePunc.lower().split(" ")
    corpusIndex = {}
    for idx, val in enumerate(corpusSplitRemovePunc):
        if val in corpusIndex:
            corpusIndex[val] = corpusIndex[val] + [idx]
        else:
            corpusIndex[val] = [idx]    
    #for each word in search query see if there is a match in index
    #if there is a match save the corpus index to an array to a bucket matching corpus index and the value equaling the search term 
    wordIndex = []
    query = query.lower().split(" ")
    for word in query:
        if word in corpusIndex:
    #snippetIndices = findSmallestRange(tempWordIndex)
            wordIndex.append([word, corpusIndex[word]])
    #print "Word Index: " + str(wordIndex)
    
    snippetIndices = findSmallestRange(wordIndex)
    snippet = []
    for item in range(snippetIndices[0], snippetIndices[1]+1):
        snippet += [corpusSplit[item]]
    return " ".join(snippet)

def findSmallestRange(wordIndex):
    """Finds the smallest range that contains all search terms
    input:  [['landmark', [32]], 
            ['city', [7, 27]], 
            ['bridge', [3, 23, 33]]]
    output: 27, 33
    """
    wordPositions = []
    doneTracker = []
    currentPos = []
    for index, value in enumerate(wordIndex):
        wordPositions += [wordIndex[index][1]]
        doneTracker += [False]
        currentPos += [0]
    
    minRange = sys.maxint

    while(True):
        if not False in doneTracker:
            break
        currentValues = getIndexValues(wordPositions, currentPos) #0,95,70
        minValue = sys.maxint 
        for idx, elem in enumerate(doneTracker):
            if not doneTracker[idx]:
                if currentValues[idx] < minValue:
                    minValue = currentValues[idx]
        listWithMinValue = currentValues.index(minValue) # 0
        if currentPos[listWithMinValue] + 1 < len(wordPositions[listWithMinValue]):
            currentPos[listWithMinValue] += 1
        else:
            doneTracker[listWithMinValue] = True
        curRange = getListRange(getIndexValues(wordPositions, currentPos))
        if curRange < minRange:
            minRange = curRange
            resPos = getIndexValues(wordPositions, currentPos)
            resRange = getListRange(resPos)    
    return (min(resPos), max(resPos))

def newCounterPos(positionLists, currentPos):
    '''returns the new counterPosition given a set of positions and a list of current positions
    uses logic in increment the index of the list with the min value
    allows iteration through multiple lists of different length
    input: [[0, 89, 130], [95, 123, 177, 199], [70, 105, 117]], [0,0,0] 0, 95, 70
    output: 1 -> you know to increment the first list
    input: [[0, 89, 130], [95, 123, 177, 199], [70, 105, 117]], [2,2,0]
    output: 3 -> you know to increment the first list
    returns None when all values have been checked
    '''
    if len(positionLists) == 0:
        return None
    newPos = currentPos
    currentValues = getIndexValues(positionLists, currentPos) #0,95,70
    minValue = min(currentValues) #0
    listWithMinValue = currentValues.index(minValue) # 0
    if currentPos[listWithMinValue] + 1 < len(positionLists[listWithMinValue]):
        newPos[listWithMinValue] += 1
    else:
       del positionLists[listWithMinValue]
       print positionLists
       newCounterPos(positionLists, currentPos)
    return newPos
    
def getListRangeIndices(l):
    '''returns the upper and lower bound of indices given a list'''
    return (max(l), min(l))

def getListRange(l):
    '''returns the range given a list'''
    return max(l) - min(l)

def getIndexValues(positions, indices):
    """return the values from a list of positions given a list of lists and list of indices 
    input: [[0, 89, 130], [95, 123, 177, 199], [70, 105, 117]], [0,0,0]
    output: [0, 95, 70]
    """
    solution = []
    for listCount, index in zip(positions, indices):
        solution += [listCount[index]]
    return solution

if __name__ == '__main__':
    corpus = "The George Washington Bridge in New York City is one of the oldest bridges ever constructed. It is now being remodeled because the bridge is a landmark. City officials say that the landmark bridge effort will create a lot of new jobs in the city."
    query = "Landmark City Bridge jobs in"
    print "query: " + str(query)
    print "result snippet: " + snippetSearch(query, corpus)

    
    
