class Trie:
    is_end : bool = False
    children: dict[str, object]
    def __int__(self):
        self.children = {}

    def insert(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()

            node = node.children[ch]
        node.is_end = True


    def confirm_search(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return True if node.is_end else False

    def search(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                return {}
            node = node.children[ch]

        return node if node.is_end else {}

    def get_words(self, word):
        node = self
        def find_strings(node, word: list, words: list):
            if node.is_end:
                words.append(''.join(word))
            for child in node.children:
                word.append(child)
                find_strings(node.children[child], word, words)
                word.pop()
        words = []
        node = self.search(word)
        find_strings(node, [], words)

        return words

    def delete(self, word):
        node = self
        is_found = self.confirm_search(word)
        def recurse(node, word: str, index: int):
            if index >= len(word):
                node.is_end = False
                return len(node.children) == 0
            node = node.children[word[index]]
            is_delete = recurse(node, word, index + 1)
            if is_delete:
                del node.children[word[index]]

            return is_delete and not node.is_end and len(node.children) == 0

        recurse(node, word, 0)








