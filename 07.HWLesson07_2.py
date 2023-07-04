print("Enter a string not exceeding 1000 characters")
string = str(input())
if len(string) > 1000:
    print("The entered string is too long. Try again.")
else:
    new_string = ' '.join(string.split())
    if string[0] == ' ':
        new_string = ' ' + new_string
    if string[-1] == ' ':
        new_string = new_string + ' '
    print("Changed string:")
    print(new_string)
