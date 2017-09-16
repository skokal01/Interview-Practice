'''
http://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversal-set-2/
Construct BST from given preorder traversal | Set 2
Given preorder traversal of a binary search tree, construct the BST.

For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output
should be root of following tree.
     10
   /   \
  5     40
 /  \      \
1    7      50
We have discussed O(n^2) and O(n) recursive solutions in the previous post. Following is a stack based iterative solution that works in O(n) time.

1. Create an empty stack.
2. Make the first value as root. Push it to the stack.
3. Keep on popping while the stack is not empty and the
next value is greater than stack's top value. Make this
value as the right child of the last popped node. Push the new node to the stack.
4. If the next value is less than the stack's top value,
make this value as the left child of the stack's top node.
Push the new node to the stack.
5. Repeat steps 2 and 3 until there are items remaining in pre[].
'''
class Node(object):
    def __init__(self,data):
        self.data = int(data)
        self.left,self.right = None,None

class BinarySearchTree(object):
    def constructTree(self,preorder):
        root = Node(preorder[0])

        s = [] # Stack
        s.append(root)

        for i in xrange(1,len(preorder)):
            temp = None

            # Keep on popping while the next value is greater than
            # stack's top value.
            while s and int(preorder[i]) > s[-1].data:
                temp = s.pop()

            if temp:
                temp.right = Node(preorder[i])
                s.append(temp.right)
            else:
                temp = s[-1]
                temp.left = Node(preorder[i])
                s.append(temp.left)

        return root

    def printInorder(self,node):
        if not node:
            return
        self.printInorder(node.left)
        print str(node.data) + " ",
        self.printInorder(node.right)

if __name__ == "__main__":
    tree = BinarySearchTree()
    root = tree.constructTree(['41', '37', '24', '1', '0', '2', '4', '3', '9', '7', '6', '5', '8', '11', '10', '16', '15', '12', '13', '14', '19', '18', '17', '20', '22', '21', '23', '35', '30', '29', '26', '25', '27', '28', '32', '31', '34', '33', '36', '39', '38', '40', '44', '42', '43', '48', '46', '45', '47', '49']
)
    tree.printInorder(root)
