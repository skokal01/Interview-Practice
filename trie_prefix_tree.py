# Prefi Tree or Trie Data Structure
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.endOfWord = True

    def search(self,word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]

        return node.endOfWord

    def startsWith(self,prefix):
        node = self.root
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        return True

if __name__ == "__main__":
    trie = Trie()
    import pdb
    pdb.set_trace()
    trie.insert("apple")
    trie.insert("apples")
    trie.insert("bat")
    trie.insert("bate")
    trie.insert("zebra")

    print trie.search("apple")
    print trie.search("dog")
    print trie.startsWith("app")
    print trie.startsWith("zzz")
