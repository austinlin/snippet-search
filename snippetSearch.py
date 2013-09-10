#!/usr/bin/env python

import string, sys

def snippetSearch(query, corpus):
    """Given a page of content with alphanumeric words, and a search phrase of N words, 
    return the shortest snippet of content that contains all N words in any order.
    """
    #generate an inverted index
    corpusSplit = corpus.split(" ")
    #normalize text, remove punctuation
    removePunc = corpus.translate(None, string.punctuation)
    corpusSplitRemovePunc = removePunc.lower().split(" ")
    corpusIndex = {}
    #add all words into a hashtable with the key being the word and the value being it's index, chaining for multiple indices 
    for idx, val in enumerate(corpusSplitRemovePunc):
        if val in corpusIndex:
            corpusIndex[val].append(idx)
        else:
            corpusIndex[val] = [idx]    
    #for each word in search query see if there is a match in index
    #if there is a match save the corpus index to an array to a bucket matching corpus index and the value equaling the search term 
    wordIndex = []
    query = query.lower().split(" ")
    for word in query:
        if word in corpusIndex:
            wordIndex.append([word, corpusIndex[word]])
    #perform search function and return joined result
    snippetIndices = findSmallestRange(wordIndex)
    snippet = []
    for item in range(snippetIndices[0], snippetIndices[1]+1):
        snippet += [corpusSplit[item]]
    return " ".join(snippet)

def findSmallestRange(wordIndex):
    """Finds the smallest range that contains all search terms, core logic for search function
    input:  [['landmark', [32]], 
            ['city', [7, 27]], 
            ['bridge', [3, 23, 33]]]
    output: 27, 33
    """
    #initialize data structures with variable length depending on occurrences of each query term
    wordPositions = [] #indicies of the query terms in corpus
    doneTracker = [] #booleans that are false if there are more positions within a term that haven't been iterated
    currentPos = [] #current position within wordPositions
    for index, value in enumerate(wordIndex):
        wordPositions += [wordIndex[index][1]]
        doneTracker += [False]
        currentPos += [0]
    minRange = sys.maxint
    while(True):
        #exit loop if all positions have been compared for a query term
        if not False in doneTracker:
            break
        #retrieve the current set of indicies to compare, one for each query term
        currentValues = getIndexValues(wordPositions, currentPos)
        minValue = sys.maxint
        #find lowest of the index values within the current set
        for idx, elem in enumerate(doneTracker):
            if not doneTracker[idx]:
                if currentValues[idx] < minValue:
                    minValue = currentValues[idx]
        listWithMinValue = currentValues.index(minValue)
        #increment the pointer to the term with the lowest value or mark as done if all values for a term have been compared
        if currentPos[listWithMinValue] + 1 < len(wordPositions[listWithMinValue]):
            currentPos[listWithMinValue] += 1
        else:
            doneTracker[listWithMinValue] = True
        #keep track of the minimum range for each set compared and return lowest when all are done
        curRange = getListRange(getIndexValues(wordPositions, currentPos))
        if curRange < minRange:
            minRange = curRange
            resPos = getIndexValues(wordPositions, currentPos)
            resRange = getListRange(resPos)    
    return (min(resPos), max(resPos))
    
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
    query = "Landmark City Bridge"
    print "query: " + str(query)
    print "result snippet: " + snippetSearch(query, corpus * int(sys.argv[1]))