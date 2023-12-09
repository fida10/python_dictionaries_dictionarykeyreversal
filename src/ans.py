"""
Practice Question 1: Dictionary Key Reversal

Task:

Create a function reverse_dictionary that takes 
a dictionary and returns a new dictionary 
where the keys and values are swapped. 
If the original dictionary has duplicate values, 
only one of the corresponding keys should be preserved in the new dictionary.
"""

def reverse_dictionary(original_dict):
    ans = {}
    for key, value in original_dict.items():
        ans[value] = key
        
    return ans
