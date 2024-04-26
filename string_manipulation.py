class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dictionary to keep track of how many of each roman numerals are in a string
        # if statement to check all 6 subtraction instances
        # delete each index where each subtraction is found, and the regularly found numerals after
        # counter variable so there is no need to loop thru dict and sole use of dict ... is nothing
        # scrap dict and only use if statements and counter to avoid having to loop thru dict

        # while loop that counts up all subtraction instances (conditional on whether the str
        # contains any of the instances)
        # another while loop looping thru str to count each value into a dict
        # an exp that adds up each value*its value and the prev loops count for the total
        count = 0
        lis = s.split()
        while 'IV' in lis or 'IX' in lis or 'XL' in lis or 'XC' in lis or 'CD' in lis or 'CM' in lis:
            a=lis.find('IV')
            if a:
                del lis[a]
                count+=4
            b=lis.find('IX')
            if b:
                del lis[b]
                count+=9
            c=lis.find('XL')
            if c:
                del lis[c]
                count+=40
            d=lis.find('XC')
            if d:
                del lis[d]
                count+=90
            e=lis.find('CD')
            if e:
                del lis[e]
                count+=400
            f=lis.find('CM')
            if f:
                del lis[f]
                count+=900
        tracker = {}
        while len(lis)>0:
            if lis[0] in tracker:
                tracker[lis[0]]+=1
                del lis[0]
            else:
                tracker[lis[0]] = 1
                del lis[0]
        return count + 1000*tracker['M'] + 500*tracker['D'] + 100*tracker['C'] + 50*tracker['L'] + 10*tracker['X'] + tracker['I']
