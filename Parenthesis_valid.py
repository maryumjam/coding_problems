

class Solution(object):
    def isValid(self, s) -> bool:
        """
        :type s: str
        :rtype: bool
      
        Constraints:

            1 <= s.length <= 104
            s consists of parentheses only '()[]{}'.
        """
        stack=[]
        mapping={')':'(','}':'{',']':'['}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack
    
if __name__ == "__main__":
        solution1= Solution()
        print(solution1.isValid('\\\\\\|||||(hsjkhdjkh)[]'))

