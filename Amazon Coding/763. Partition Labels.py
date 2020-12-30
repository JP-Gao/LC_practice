class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_index = {} # set a dictionary to store the index for each unique letter's last occurence
        for idx, char in enumerate(S):
            last_index[char] = idx # fill the dict
        ans = []
        start = end = 0
        for idx, char in enumerate(S):
            if last_index[char] > end: # if the last index is larger than end, we need to expand end with the last index in the dict
                end = last_index[char]
            if idx == end: # if our idx reaches the end, we find the first split.
                ans.append(end-start+1) # store the length.
                start = end + 1 # set the new start as the end's next one
        return ans
