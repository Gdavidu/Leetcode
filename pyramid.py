# Given a list of numbers, arrange the elements of the list into a pyramid shaped list
# of lists in a pyramid format. If the number of elements conclude with an unfinished pyramid level, return false
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# number of possible elements necessary for a pyramid: 3 6 10 15 21
# list to contain pyramid: pyramid
# variable needed to track pyramid level: lvl
# while len(nums)>0
# if len(nums)<lvl return false
# else pyramid.append([:lvl])
# del pyramid[:lvl]
# lvl+=1
def pyramidsort(anylist):
    pyramid = []
    lvl = 1
    while len(anylist)>0:
        if len(anylist)<lvl:
            return "Pyramid incomplete"
        else:
            pyramid.append(anylist[:lvl])
            del anylist[:lvl]
            lvl+=1
    return pyramid
print(pyramidsort(nums))
