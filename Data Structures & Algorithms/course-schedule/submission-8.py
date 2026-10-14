from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        from_to = defaultdict(list)
        for a,b in prerequisites:
            indegree[a] += 1
            from_to[b].append(a)

        q = deque()
        count = 0
        for i,val in enumerate(indegree):
            if val == 0:
                q.append(i)

        
        while q:
            node = q.popleft()
            count += 1
            for child in from_to[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
                    
        
        return False if count != numCourses else True
