class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        #Avinandan169

        free_servers=[(w,i) for i,w in enumerate(servers)]
        heapq.heapify(free_servers)
        busy_servers=[]
        ans=[0]*len(tasks)
        cur_time=0

        for j,t in enumerate(tasks):
            cur_time=max(cur_time,j)
            if not free_servers:
                cur_time=busy_servers[0][0]
            while busy_servers and busy_servers[0][0]<=cur_time:
                ft,w,i=heapq.heappop(busy_servers)
                heapq.heappush(free_servers,(w,i))
            w,i=heapq.heappop(free_servers)
            ans[j]=i
            heapq.heappush(busy_servers,(cur_time+t,w,i))

        return ans
        