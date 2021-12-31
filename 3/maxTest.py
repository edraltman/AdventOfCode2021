a = [1,1,0]
b = [1,0,0]
c = [1,1,0,0]

# print(max(set(a), key=a.count))

# from collections import Counter

# def Most_Common(lst):
#     data = Counter(lst)
#     return data.most_common(1)[0][0]

# print(Most_Common(a))

from statistics import StatisticsError, multimode

def mostCommon(inputList,tieBreak):
    # modes = multimode(inputList)
    # if len(modes) > 1:
    #     return tieBreak
    # return modes[0]

    if len(multimode(inputList)) == 1:
        return multimode(inputList)[0]
    return tieBreak

print(mostCommon(a,1))
print(mostCommon(b,1))
print(mostCommon(c,1))
print(mostCommon(c,0))