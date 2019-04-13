'''
Python Implementation of trie data strucutre

References:
1. persistent trie -- gaurav sen youtube

Todo:
1. Implement an autocomplete system

'''

class TrieNode():
    def __init__(self, char):
        self.char = char
        self.children = []
        self.is_last_node = True

    def add_child(self, char):
        '''
        Add a child to the current node and return the child node.
        '''
        node = TrieNode(char)
        self.children.append(node)
        self.is_last_node = False
        return node
    
    def __str__(self):
        return self.char

class Trie():
    def __init__(self):
        self.root = TrieNode('*')

    def add_string(self, string):
        curr_node = self.root
        
        for char in string:
            is_present = False
            for node in curr_node.children:
                if node.char == char:
                    curr_node = node
                    is_present = True
            if not is_present:
                node = curr_node.add_child(char)
                curr_node = node

        curr_node.is_last_node = True

    def dfs(self, node):
        if node.is_last_node:
            return [node.char]
        else:
            list_words = []
            for child in node.children:
                for word in self.dfs(child):
                    list_words.append(node.char + word)
            
            return list_words

    def find_prefix(self, prefix):
        '''
        Return the list of words beginning with a given prefix
        '''
        list_words = []

        # match prefix in trie and get last node.
        curr_node = self.root
        is_present = False
        for char in prefix:
            for node in curr_node.children:
                if node.char == char:
                    curr_node = node
                    is_present = True
            if not is_present:
                return []
        
        # perform dfs from current node to return all strings with the prefix
        list_child_words = []
        for child in curr_node.children:
            list_child_words += self.dfs(child)

        for word in list_child_words:
            list_words.append(prefix + word)

        return list_words

    def __str__(self):
        pass


if __name__ == '__main__':
    trie = Trie()
    trie.add_string("sea")
    trie.add_string("string")
    trie.add_string("store")
    trie.add_string("stream")
    print(trie.find_prefix('st'))