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
        while 'IV' in s or 'IX' in s or 'XL' in s or 'XC' in s or 'CD' in s or 'CM' in s:
            a=s.find('IV')
            if a!=-1:
                s = s.replace(s[a:a+1], '')
                count+=4
            b=s.find('IX')
            if b!=-1:
                s = s.replace(s[b:b+1], '')
                count+=9
            c=s.find('XL')
            if c!=-1:
                s = s.replace(s[c:c+1], '')
                count+=40
            d=s.find('XC')
            if d!=-1:
                s = s.replace(s[d:d+1], '')
                count+=90
            e=s.find('CD')
            if e!=-1:
                s = s.replace(s[e:e+1], '')
                count+=400
            f=s.find('CM')
            print(f)
            if f!=-1:
                s = s.replace(s[f:f+1], '')
                count+=900
        print('count: ', count, 'current s: ', s)
        count2 = 0
        while len(s)>0:
            if s[0] == 'M':
                count2+=1000
            if s[0] == 'D':
                count2+=500
            if s[0] == 'C':
                count2+=100
            if s[0] == 'L':
                count2+=50
            if s[0] == 'X':
                count2+=10
            if s[0] == 'V':
                count2+=5
            if s[0] == 'I':
                count2+=1
            s = s[1:]
            # print('count2: ', count2, 's: ', s)
        return count + count2
        #     if s[0] in tracker:
        #         tracker[s[0]]+=1
        #         del s[0]
        #     else:
        #         tracker[s[0]] = 1
        #         del s[0]
        # return count + 1000*tracker['M'] + 500*tracker['D'] + 100*tracker['C'] + 50*tracker['L'] + 10*tracker['X'] + tracker['I']
