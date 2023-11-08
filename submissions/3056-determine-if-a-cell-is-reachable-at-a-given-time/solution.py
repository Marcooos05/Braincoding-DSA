class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        x_dis = abs(sx-fx)
        y_dis = abs(sy-fy)
        minstep = max(x_dis, y_dis)
        
        if minstep == 0:
            return t != 1
        if (minstep <= t):
            return True
        
        return False
