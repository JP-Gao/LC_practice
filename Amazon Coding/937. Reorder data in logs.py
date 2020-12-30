class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            identifier, rest = log.split(' ', maxsplit = 1) # split the log with space and do only 1 split. default is -1.
            if rest[0].isalpha():
                return (0, rest, identifier)
            else:
                return (1, )
        return sorted(logs, key = get_key)
        # n is the number of logs, m is the max length of a single log
        # time: O(nlogn * m)
        # space: O(n*m)
        
        
class Solution:
    def reorderLogFiles(self, logs):

        letter = []
        digit = []

        for each in logs:

            # split and check the element after 0th position to decide whether its a digit or alphabet
            if each.split(' ')[1].isdigit():
                digit.append(each)
            else:
                letter.append(each)

        # sort letter elements first, if tie sort identifier
        letter.sort(key = lambda x: (x.split()[1:], x.split()[0]))

     
        return letter + digit
