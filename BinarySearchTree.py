from TreeNode import TreeNode


class BinarySearchTree:

    def __init__(self):
        self.root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        self.__root = root

    def add(self, value):
        newnode = TreeNode(value)
        if self.root is None:
            self.root = newnode
            return
        temp = self.root
        while True:
            if temp.value > value:
                if temp.leftchild is None:
                    temp.leftchild = newnode
                    newnode.parent = temp
                    break
                else:
                    temp = temp.leftchild
            else:
                if temp.rightchild is None:
                    temp.rightchild = newnode
                    newnode.parent = temp
                    break
                else:
                    temp = temp.rightchild

    def find(self, value):
        temp = self.root
        while value != temp.value:
            if value < temp.value:
                temp = temp.leftchild
            elif value > temp.value:
                temp = temp.rightchild
        return temp

    def remove(self, value):
        nodetoremove = self.find(value)
        parent = nodetoremove.parent
        if nodetoremove.leftchild is None and nodetoremove.rightchild is None:
            self.removeLeaf(nodetoremove, parent)
        elif nodetoremove.leftchild is None or nodetoremove.rightchild is None:
            self.removeIfHasOneChild(nodetoremove, parent)
        else:
            self.removeIfHasTwoChildren(nodetoremove, parent)
        return nodetoremove.value

    def removeLeaf(self, nodetoremove, parent):
        if nodetoremove.value < parent.value:
            parent.leftchild = None
        else:
            parent.rightchild = None

    def removeIfHasOneChild(self, nodetoremove, parent):
        if nodetoremove.rightchild is None:
            leftchild = nodetoremove.leftchild
            if nodetoremove == parent.leftchild:
                parent.leftchild = leftchild
            else:
                parent.rightchild = leftchild
            leftchild.parent = parent
        else:
            rightchild = nodetoremove.rightchild
            if nodetoremove == parent.leftchild:
                parent.leftchild = rightchild
            else:
                parent.rightchild = rightchild
            rightchild.parent = parent

    def removeIfHasTwoChildren(self, nodetoremove, parent):
        rightchild = nodetoremove.rightchild
        rightchildsLeftchild = rightchild.leftchild
        if rightchild.leftchild is not None and rightchildsLeftchild.leftchild is None and rightchildsLeftchild.rightchild is None:
            if nodetoremove == parent.leftchild:
                parent.leftchild = rightchildsLeftchild
            else:
                parent.rightchild = rightchildsLeftchild
            rightchildsLeftchild.parent = parent
            rightchild.leftchild = None

        else:
            temp = rightchildsLeftchild
            while temp.leftchild is not None:
                temp = temp.leftchild
            if nodetoremove == parent.leftchild:
                parent.leftchild = temp
            else:
                parent.rightchild = temp
            tempParent = temp.parent
            tempParent.leftchild = temp.rightchild
            temp.rightchild.parent = tempParent
            temp.parent = parent







