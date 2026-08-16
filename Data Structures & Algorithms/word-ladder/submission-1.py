class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        bl,el = len(beginWord),len(endWord)
        if bl != el:
            return 0
        wordSet = set()
        vis = set()
        adj_list = collections.defaultdict(list)
        for w in wordList:
            wordSet.add(w)
        if endWord not in wordSet:
            return 0
        wordList.append(beginWord)
        for word in wordList:
            l = len(word)
            if l != bl:
                continue
            for i in range(l):
                for j in range(97,123):
                    new_word = word[:i]+chr(j)+word[i+1:]
                    new_word="".join(new_word)
                    if new_word in wordSet:
                        adj_list[word].append(new_word)
                        adj_list[new_word].append(word)

        q = collections.deque()
        if endWord not in wordSet:
            return 0
        vis.add(beginWord)
        for i in adj_list[beginWord]:
            q.append(i)
            vis.add(i)
        counter = 1
        while q:
            ql = len(q)
            counter += 1
            for i in range(ql):
                curr = q.popleft()
                if curr == endWord:
                    return counter
                for neigh in adj_list[curr]:
                    if neigh not in vis:
                        vis.add(neigh)
                        q.append(neigh)
        
        return 0 