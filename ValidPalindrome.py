class Solution():
    def valid_palindrome(self, s):
        cleaned_text=""
        print(s.lower())
        for char in s.lower():
           if char.isalnum():
               cleaned_text += char
        print(cleaned_text)
        if cleaned_text == cleaned_text[::-1]:
            print("Valid")
        else:
            print("Invalid")
        



if __name__== '__main__':
    solution = Solution()
    solution.valid_palindrome("A man, A plan, a Canal: panama")