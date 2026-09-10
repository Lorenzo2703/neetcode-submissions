class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        l, r = 0, len(people) - 1

        while l <= r:
            if people[r] + people[l] <= limit:
                l += 1  # Lightest person shares the boat
            
            # Heaviest person always gets on a boat (alone or with the lightest)
            r -= 1
            boat += 1

        return boat