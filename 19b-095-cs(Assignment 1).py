# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:57:20 2020

@author: Umair Ullah Khan
"""

class SharpSearch:
    def __init__(self, data):
        self.data = data  ### As a List.
    def SearchFrist(self, n):
        for i in range(len(self.data)):
            if self.data[i] == n:
                return i

    def SearchLast(self, n):  ### Print the Second occurrence of the num.
            for i in  reversed(range(len(self.data))):
                if self.data[i] == n:
                    return i
            return -1  ## if the number is not in the list.

    def Search(self, n): ##
        pass

    def SearchAll(self, n): ### Print all the occurrence of the nth value.
        List = []
        for i in range(len(self.data)):

            if self.data[i] == n:
                List.append(i)

        return List
u = SharpSearch([5,4,7,1,4,9])

print(u.SearchFrist(4))
print(u.SearchLast(4))
print(u.SearchLast(5))
print(u.SearchLast(15))
print(u.SearchAll(4))


