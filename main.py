# this function takes a string message as a parameter,
# performs Run Length Encoding on the string,
# and returns a new string representing the compressed message.
def RLE_compress(message):
    charlist = list(message)
    counts = 1
    finished = ""

    for i in range (1,len(charlist)):
        if charlist[i - 1] == charlist[i]:
            counts += 1
        else:
            finished = finished + charlist[i-1] + str(counts)
            counts = 1
    finished = finished + charlist[len(charlist)-1] + str(counts)
    return finished


    











    

# TEST CODE:
print(RLE_compress("AABBBAAAABBBBBAAAAAABBBBBBB"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFF"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFD"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFDD"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFDDD"))
print(RLE_compress("ABCDEF"))
print(RLE_compress("FFFFFFFFFFFFFFFFFFF"))
print(RLE_compress("F"))
print(RLE_compress("F????"))
print(RLE_compress("Mmmmmmmmmm sooooo goooooood!"))
print(RLE_compress("Booooooooooooo, hisssssssss"))
