class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return None
        visited=[]
        ttl_rooms=len(rooms)
        
        def visit(room):
            visited.append(room)

            for key in rooms[room]:
                if key not in visited:
                    visit(key)

        visit(0)

        print(visited)
        
        print(ttl_rooms)
        return ttl_rooms==len(visited)