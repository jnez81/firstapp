def retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude):
    # split literatureText, loop over each word, maintain a dict about how often used
    # not going to count any word in wordsToExclude
    outputs = []
    countMap = {}
    words = literatureText.split()
    for word in words:
        if word in wordsToExclude:
            continue
        if word not in countMap:
            countMap[word] = 0
        countMap[word] += 1
    if len(countMap) == 0:
        return outputs
    maxCount = max(countMap.values())
    for word, count in countMap.items():
        if count == maxCount:
            outputs.append(word)
    return outputs