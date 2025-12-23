class Solution:
    def decodeString(self, s: str) -> str:
        num_stack=[]
        str_stack=[]
        curr_num=0
        curr_str=""
        for i in s:
            if i.isdigit():
                curr_num=curr_num*10+int(i)
            elif i=="[":
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_num=0
                curr_str=""
            elif i=="]":
                rep=num_stack.pop()
                str_s=str_stack.pop()
                curr_str=str_s+curr_str*rep
            else:
                curr_str+=i
        return curr_str
