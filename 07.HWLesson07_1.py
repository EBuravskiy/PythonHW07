print("Enter a word or string without spaces")
string = str(input())
string.lower()
mid = (len(string))//2
for index in range(mid):
    if string[index] != string[-1-index]:
        print ("No. The entered word or string is not a palindrome")
        quit()
print ("Yes. The entered word or string is a palindrome")
