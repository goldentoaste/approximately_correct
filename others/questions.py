from operator import index


class Solution:
    index = 0
    expected = {"(" : ")", "[": "]", "{": "}"}
    def isValid(self, s: str) -> bool:
        val =  self.helper(s)
        if Solution.index < len(s):
            return False
        return val

    def helper(self, s:str, ):
        
        if Solution.index == len(s):
            return True        
        
        current = s[Solution.index]
        Solution.index +=1
        
        if s[Solution.index] != Solution.expected[current]:
            return self.helper(s)
        
        temp = s[Solution.index] == Solution.expected[current] 
        Solution.index +=1
        return temp and  self.helper(s)
    
print(Solution().isValid("([)]"))