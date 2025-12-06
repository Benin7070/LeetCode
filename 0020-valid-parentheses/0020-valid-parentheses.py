class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch in '({[':
                st.append(ch)
            else:
                if not st:
                    return False
                top=st.pop()
                if (top=='(' and ch!=")") or (top=='{' and ch!='}') or (top=="[" and ch!=']') :
                    return False
        if st:      
            return False
        else:
            return True