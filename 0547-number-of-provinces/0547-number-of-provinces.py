class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        provinces=0
        n=len(isConnected)


        def dfs(city):
            visited.add(city)

            for i in range(n):
                if isConnected[city][i]==1 and i not in visited:
                    dfs(i)
        for city in range(n):
            
            if city not in visited:
                provinces+=1
                dfs(city)

        return provinces