# GRAPHS - Medium

# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
# Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. 
# Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
# return true if you can visit all the rooms, or false otherwise.

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = rooms[0]
        keys_got = {0,}

        while keys:
            key = keys.pop()
            
            if key not in keys_got:
                keys_got.add(key)
                keys += rooms[key]
        
        return len(keys_got) == len(rooms)
