# Question 2
# Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.

def question2(a):
    longest = ''
    for idx in xrange(len(a)):
        current_pal = palindrome_helper(a, idx)
        if len(current_pal) > len(longest):
            longest = current_pal
            #print 'updating longest to {}'.format(longest)
        if idx + 1 != len(a):
            if a[idx] == a[idx + 1]:
                current_pal = palindrome_helper(a, idx, (idx + 1))
            if len(current_pal) > len(longest):
                        longest = current_pal
                        #print 'updating longest to {}'.format(longest)
    return longest

def palindrome_helper(test_str, idx, double_mid=None):
    ''' Creates a palindrome starting from a specified index of a given string
        Returns the text string of any palindrome found '''
    low = idx - 1
    if double_mid:
        high = idx + 2
        pal = test_str[idx:high]
    else:
        high = idx + 1
        pal = test_str[idx]
    while low >= 0 and high < len(test_str):
        if test_str[low] == test_str[high]:
            pal = test_str[low:high + 1]
            low -= 1
            high += 1
        else:
            break
    return pal


if __name__ == '__main__':
    print 'TEST 1: searching "abbaracecar5abcd" for longest palindrome'
    print 'Should return "racecar"'
    print question2('abbaracecar5abcd')
    print 'TEST 2: searching "abbar4cecar5abcd" for longest palindrome'
    print 'Should return "abba"'
    print question2('abbar4cecar5abcd')
    print 'TEST 3: searching "abcdefg" for longest palindrome'
    print 'Should return "a"'
    print question2('abcdefg')

# Notes
# This algorithm discovers the longest palindrome by examining the characters
# to the left and right of each character, and pairs of like characters,
# in the input string `a`. Should the palindrome helper continue to find equal,
# adjacent characters, it will continue to build a palindrom until it reaches
# either end of the string.
#
# This algorithm is only performing its operations once for each character of
# the input string. Thus, it has an aproximate runtime of O(n). The algorithm's
# aproximate worst case space complexity is O(n), in the case that the provided
# string is a complete palindrome. In this case, the program's string splicing
# logic on line 31 will create a new string that is n chars long.