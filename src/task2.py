from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings or not all(isinstance(s, str) for s in strings):
            return ""
        
        for string in strings:
            self.put(string, 0)

        result = ""
        node = self.root
        while len(node.children) == 1 and node.value is None:
            char = next(iter(node.children))
            result += char
            node = node.children[char]
        
        return result

def run_task2():
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    print('Тести пройдено успішно!')

if __name__ == "__main__":
    run_task2()