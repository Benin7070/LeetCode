class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        bal={}
        for bill in bills:
            if bill>5:
                if bill==10 and bal.get(5,0)>0:
                    bal[5]=bal.get(5)-1
                elif bill==20:
                    if (bal.get(10,0)>0 and bal.get(5,0)>0):
                        bal[10]=bal.get(10)-1
                        bal[5]=bal.get(5)-1
                    elif (bal.get(5,0)>2):
                        bal[5]=bal.get(5)-3
                    else:
                        return False
                else:
                    return False

            bal[bill]=bal.get(bill,0)+1


        return True