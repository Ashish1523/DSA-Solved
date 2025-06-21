class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        cnt = len(word)
        rnd = 1 #nb of mapping layers
        while cnt > 0:
            pushes += rnd*min(8,cnt)
            cnt -= min(8,cnt)
            rnd += 1
        return pushes