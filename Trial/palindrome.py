# identify palindromes
# if not a palindrome output should read "not palindrome"
# if palindrome output should read "this is a palindrome

count = 0
while count < 5:
    word_input = input('enter a word')
    if word_input == word_input[:: -1]:
        print ('is a palindrome')
    else:
        print('is not a palindrome')
    count += 1
