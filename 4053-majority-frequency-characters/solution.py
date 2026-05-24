from collections import Counter, defaultdict

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counts = Counter(s)
        freq_map = defaultdict(list)
        for char, freq in counts.items():
            freq_map[freq].append(char)
            
        best_freq = max(freq_map.keys(), key=lambda k: (len(freq_map[k]), k))
        return "".join(freq_map[best_freq])

