class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        lookup = set()
        for u, v in similarPairs:
            lookup.add((u, v))
            lookup.add((v, u))

        if len(sentence1) != len(sentence2):
            return False

        return all(w1 == w2 or (w1, w2) in lookup
            for w1, w2 in zip(sentence1, sentence2))