
def getPrefix(number, k):
    
    if len(number) >= k:
        prefix = int(number[:k])
    else:
        prefix = int(number)
    return prefix

