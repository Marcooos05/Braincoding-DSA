class Solution(object):
    def isPathCrossing(self, path):
        past = []
        pos = [0,0]
        
        """
        :type path: str
        :rtype: bool
        """
        
        for action in path:
            move_dict = {'N': [pos[0], pos[1]+1], 'S': [pos[0], pos[1]-1], 'E': [pos[0]+1, pos[1]], 'W': [pos[0]-1, pos[1]]}
            past.append((pos))
            pos = move_dict[action]
            if pos in past:
                return True
        return False

        
