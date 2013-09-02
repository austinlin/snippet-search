import string

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
        print corpusSplit[item]
        snippet += [corpusSplit[item]]
    return "Result snippet: " + " ".join(snippet)

def findSmallestRange(wordIndex):
    """Finds the smallest range that contains all search terms
    input:  [['landmark', [32]], 
            ['city', [7, 27]], 
            ['bridge', [3, 23, 33]]]
    output: 27, 33
    """
    # found = {}
    
    # lengthOfIndices = []
    # print wordIndex
    # for word, index in wordIndex:
    #     lengthOfIndices += [len(index)]
    # print "length of indices: " + str(lengthOfIndices)
    # solutionRange = []
    # solutionPos = []
    # counterPositions = [0, 0, 0]
    # smallestRange = 99999999
    # wordPositions = []
    # #massage input to be just word positions
    # for index, value in enumerate(wordIndex):
    #     wordPositions += [wordIndex[index][1]]
    # print wordPositions
    
    # currentWordPositions = getIndexValues(wordPositions, counterPositions)
    # print currentWordPositions
    # currentRange = getListRange(getIndexValues(wordPositions, counterPositions))
    # smallestRange = currentRange
    # solutionPos = currentWordPositions
    # solutionRange = getListRange(solutionPos)
    # print solutionRange
    # while(True):
    #     indexOfSmallest = currentWordPositions.index(min(currentWordPositions))
    #     if counterPositions[indexOfSmallest]+1 < len(wordIndex[0][1]):
    #         counterPositions[indexOfSmallest] += 1
    #         currentWordPositions = getIndexValues(wordPositions, counterPositions)
    #         currentRange = getListRange(getIndexValues(wordPositions, counterPositions))
    #         print currentWordPositions
    #         if currentRange < smallestRange:
    #             #update solutions
    #             smallestRange = currentRange
    #             solutionPos = currentWordPositions
    #             solutionRange = getListRange(solutionPos)
    #             print solutionRange
    #     else:
    #         #return solutionRange
    #         print (min(currentWordPositions), max(currentWordPositions))
    #         break

    print "------------"
    #positionLists = [[0, 89, 130], [95, 123, 177, 199], [70, 105, 117]]
    print wordIndex
    wordPositions = []
    doneTracker = []
    currentPos = []
    for index, value in enumerate(wordIndex):
        wordPositions += [wordIndex[index][1]]
        doneTracker += [False]
        currentPos += [0]
    
    minRange = 9999999

    while(True):
        if not False in doneTracker:
            print "done" 
            break
        currentValues = getIndexValues(wordPositions, currentPos) #0,95,70
        print doneTracker
        minValue = 999999
        for idx, elem in enumerate(doneTracker):
            if not doneTracker[idx]:
                if currentValues[idx] < minValue:
                    minValue = currentValues[idx]
        #print currentValues
        listWithMinValue = currentValues.index(minValue) # 0
        #print listWithMinValue
        if currentPos[listWithMinValue] + 1 < len(wordPositions[listWithMinValue]):
            currentPos[listWithMinValue] += 1
        else:
            doneTracker[listWithMinValue] = True
            print "finished with list " + str(listWithMinValue)          
            #print positionLists
        curRange = getListRange(getIndexValues(wordPositions, currentPos))
        if curRange < minRange:
            minRange = curRange
            resPos = getIndexValues(wordPositions, currentPos)
            resRange = getListRange(resPos)
        print currentPos
        print getIndexValues(wordPositions, currentPos)
    print resPos
    print resRange

    #     if currentRange < smallestRange:
    #         #update solutions
    #         smallestRange = currentRange
    #         solutionPos = currentWordPositions
    #         solutionRange = getListRange(solutionPos)
    #         print solutionRange
    #     else:
    #         #increment position of lowest index 0,95,70 -> 89, 95,70
    #         indexOfSmallest = currentWordPositions.index(min(currentWordPositions))
    #         if counterPositions[indexOfSmallest]+1 < len(wordIndex[0][1]):
    #             counterPositions[indexOfSmallest] += 1
    #             currentWordPositions = getIndexValues(wordPositions, counterPositions)
    #             print currentWordPositions
    #         currentRange = getListRange(getIndexValues(wordPositions, counterPositions))

    # print solutionRange


    #iterate through all of the queryterms and pull the first value
    #for queryTerm, numberOfOccurances in enumerate(lengthOfIndices):
        #pointer to first numbers in all three
        #resultIndexSet += [wordIndex[queryTerm][1][0]]
    #smallestRange = max(resultIndexSet) - min(resultIndexSet)
    #print "resultIndexSet: " + str(resultIndexSet) + " - range: " + str(smallestRange)

    #print "resultIndexSet: " + str(resultIndexSet) + " - range: " + str(smallestRange)




    #     for word, index in wordIndex:
    #         if(len(index) > i):
    #             a.append(index[i])
    #     smallestRange = max(a) - min(a)
    #     if max(a) - min (a) < smallestRange:
    #         smallestRange = max(a) - min(a)
    #         print smallestRange
    #     break

    # print "final smallest Range: " + str(smallestRange)
    # print a
    
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
        print "done"
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
    print newPos
    return newPos
    

#     #isolate each list
#     currentValues = []
#     solution = indices
#     for elem in indices:
#         #find smallest position in positions
#         currentValues = getIndexValues(positions, indices) #0,95,70
#     #if item is able to be incremented
#     minValue = min(currentValues)
#     lindices.index(minValue) #the list in position which contains the minValue
#     for elem in positions:
#         indexOfMinValue = positions[elem].index(minValue)
#     #indices[currentValues[minValue]] value of current index on current position list
#     if indices[currentValues[minValue]] + 1 < len(currentValues[minValue]):
#         solution[] =
#         return solution


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
    query = "Landmark City Bridge effort"
    print snippetSearch(query, corpus)

    
    
