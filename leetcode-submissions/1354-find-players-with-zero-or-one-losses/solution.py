class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        player_dict = {}

        for i in range(len(matches)):
            winner = matches[i][0]
            loser = matches[i][1]
            if winner not in player_dict:
                player_dict[winner] = 0
            if loser not in player_dict:
                player_dict[loser] = 1
            else:
                player_dict[loser] = player_dict[loser] + 1

        winner_list = []
        lose_list = []
        for player in player_dict:
            if player_dict[player] == 0:
                winner_list.append(player)
            elif player_dict[player] == 1:
                lose_list.append(player)
        
        winner_list.sort()
        lose_list.sort()
        return [winner_list, lose_list]
            
            
