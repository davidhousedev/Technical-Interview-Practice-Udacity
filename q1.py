# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

import pprint

def question1(s, t):
    # Build initial
    graph = [[] for let in t]
    for letter in t:
        if letter not in s:
            return False
        else:
            graph[0].append(Anagram(letter, t, s))

    for idx, line in enumerate(graph):
        for anagram in line:
            if anagram.check_letters():
                graph[idx + 1].append(anagram)
    print '== RESULTS =='
    for line in graph:
        for obj in line:
            print obj.value,
        print ''
    return bool(len(graph[len(t) - 1]) > 0)



class Anagram:
    """Contains the value of an anagram possibility, and the remaining letters"""
    def __init__(self, first_letter, orig_substr, check_str):
        self.value = first_letter
        self.check_str = check_str
        self.remaining = list(orig_substr.replace(first_letter, ''))

    def check_letters(self):
        for letter in self.remaining:
            if self._test_substr(self.value + letter):
                self.remaining.remove(letter)
                self.value += letter
                return True
        return False

    def _test_substr(self, t):
        ''' Return true if substr t is present in string s, else false '''
        return bool(t in self.check_str)

if __name__ == '__main__':
    print question1('93845093809384509834abcd129832109', 'dcba')


# Notes
# My algorithm weeds out anagram posibilities with dynamic programming to reduce the number of
# computations. First, it checks whether or not any letters in the substr (t) are absent
# from query string s and immediately returns False if any are not found, as an anagram would
# not be possible.
#
# The primary logic of the algorithm uses a series of Anagram objects which keep track of
# a current anagram possibility and any remaining letters that need to be added. Anagrams
# are iterated over multiple times, but only preserving objects that continue to be found
# within the original query string when letters are appended.
#
# Eventually, if an Anagram object survives to the final iteration, it will be complete
# and still present within the original query string. Thus, the algorithm returns True.
#
# The algorithm runs at O((n-x)*(n-(x+1))) where x is the zero-indexed iteration of the
# anagram building loop. However, the first iteration will always run at O(n^2), so
# this is the aproximate runtime.