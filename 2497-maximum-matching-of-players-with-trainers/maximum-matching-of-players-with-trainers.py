class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        #Avinandan169
        players.sort()
        trainers.sort()

        player=0
        trainer=0
        ans=0

        while player<len(players) and trainer<len(trainers):

            if trainers[trainer]>=players[player]:
                ans+=1
                player+=1
                trainer+=1

            else:
                trainer+=1
        
        return ans

        
            




        