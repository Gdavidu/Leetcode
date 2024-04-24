def decode(message_file):
    with open(message_file, 'r') as file:
            txtlist = file.readlines()

    def ele_key(str):
        num, word = str.split()
        num = int(num)
        return num

    sortedlist = sorted(txtlist, key=ele_key)
    

    def pyramidsort(anylist):
        pyramid = []
        lvl = 1
        while len(anylist) > 0:
            if len(anylist) < lvl:
                return "Pyramid incomplete"
            else:
                pyramid.append(anylist[:lvl])
                del anylist[:lvl]
                lvl += 1
        return pyramid

    txtpyramid = pyramidsort(sortedlist)
    codewords = []
    for ele in txtpyramid:
        num, word = ele[-1].split()
        codewords.append(word)
    msg = ' '.join(codewords)
    return msg

print(decode('coding_qual_input.txt'))
