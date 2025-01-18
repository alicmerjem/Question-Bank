"""
combine two lists in a dict
"""

def combine_lst(l1, l2):
    return {l1[i]:l2[i] for i in range(len(l1))}
