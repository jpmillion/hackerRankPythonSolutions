def merge_the_tools(string, k):
    # your code goes here
    for substring in zip(*[iter(string)]*k):
        seen = {}
        print(''.join([seen.setdefault(c, c) for c in substring if c not in seen]))