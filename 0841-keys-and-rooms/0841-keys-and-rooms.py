class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return None
        visited=set()
        ttl_rooms=len(rooms)
        
        def visit(room):
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    visit(key)

        visit(0)
        return ttl_rooms==len(visited)