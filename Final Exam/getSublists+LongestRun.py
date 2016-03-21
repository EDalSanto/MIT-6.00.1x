"""
Write a function called getSublists, which takes as parameters a list of integers named L 
and an integer named n.

assume L is not empty
assume 0 < n <= len(L)
This function returns a list of all possible sublists in L of length n without skipping 
elements in L. The sublists in the returned list should be ordered in the way they appear 
in L, with those sublists starting from a smaller index being at the front of the list.

Example 1, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should 
return the list [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], 
[4, 5, 7, 7], [5, 7, 7, 2]]

Example 2, if L = [1, 1, 1, 1, 4] and n = 2 then your function should return the list 
[[1, 1], [1, 1], [1, 1], [1, 4]]
"""

def getSublists(L, n):
	list_of_sublists = [] 	
	for i in range(len(L)-n+1):
		list_of_sublists.append(L[i:i+n]) 
		#create sublists of length n for every i and adds this sublist to master sublist
	return list_of_sublists

"""
Write a function called longestRun, which takes as a parameter a list of integers named L 
(assume L is not empty). This function returns the length of the longest run of 
monotonically increasing numbers occurring in L. A run of monotonically increasing 
numbers means that a number at position k+1 in the sequence is either greater than or 
equal to the number at position k in the sequence.

For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should return the 
value 5 because the longest run of monotonically increasing integers 
in L is [3, 4, 5, 7, 7].

My function creates a list of sublists for i ranging from the length of the list L 
down to 0.
It then loops through those lists and checks to see if any of those lists are monotonic.
If so, the function returns the current value of i, the Longest Run.
"""

def longestRun(L):
	for i in range(len(L),0,-1): 	
		for list in getSublists(L,i): 
			if all(x<=y for x, y in zip(list, list[1:])) == True: #checks to see if list is monotonic
				return i
		

	
	
