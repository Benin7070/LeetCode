class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        result = 0
        sign = 1
        
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            
            elif char == '+':
                result += sign * num
                num = 0
                sign = 1
            
            elif char == '-':
                result += sign * num
                num = 0
                sign = -1
            
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            
            elif char == ')':
                result += sign * num
                num = 0
                prev_sign = stack.pop() 
                prev_result = stack.pop()  
                result = prev_result + prev_sign * result
        

        result += sign * num
        
        return result