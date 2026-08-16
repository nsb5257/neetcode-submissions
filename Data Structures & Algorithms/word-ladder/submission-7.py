class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        bl,el = len(beginWord),len(endWord)
        if bl != el:
            return 0
        wordSet = set()
        vis = set()
        wordSet.add(beginWord)
        for w in wordList:
            wordSet.add(w)
        if endWord not in wordSet:
            return 0

        q = collections.deque()
        q.append(beginWord)
        vis.add(beginWord)
        counter = 0
        while q:
            ql = len(q)
            counter += 1
            for _ in range(ql):
                word = q.popleft()
                if word == endWord:
                    return counter
                l = len(word)
                for k in range(l):
                    for j in range(97,123):
                        new_word = word[:k]+chr(j)+word[k+1:]
                        new_word="".join(new_word)
                        if new_word in wordSet and new_word not in vis:
                            q.append(new_word)
                            vis.add(new_word)
        
        return 0 