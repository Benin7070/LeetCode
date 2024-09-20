class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        cur_num = x/2.0
        while True:
            next_num=(cur_num+x/cur_num)/2
            if abs(next_num-cur_num)<0.0001:
                return int(next_num)
            cur_num=next_num