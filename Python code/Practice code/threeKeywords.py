def threeKeywordSuggestions(numReviews, repository, customerQuery):
    # loop over each character of the customerQuery
    # create new subQuery based on that
    # loop over each word in the repo
    # see if it starts with the subQuery
    outputs = []
    loweredRepo = sorted([word.lower() for word in repository])
    for i in range(1, len(customerQuery)):
        subQuery = customerQuery[0:i+1]
        matchedWords = []
        for word in loweredRepo:
            if word.startswith(subQuery):
                matchedWords.append(word)
            if len(matchedWords) == 3:
                break
        if len(matchedWords) > 0:
            outputs.append(matchedWords)
        outputs.append(matchedWords)
    return outputs
