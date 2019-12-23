class TreeNode:

    def __init__(self, value=None):
        self.value = value
        self.leftchild = None
        self.rightchild = None
        self.parent = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def leftchild(self):
        return self.__leftchild

    @leftchild.setter
    def leftchild(self, leftchild):
        self.__leftchild = leftchild

    @property
    def rightchild(self):
        return self.__rightchild

    @rightchild.setter
    def rightchild(self, rightchild):
        self.__rightchild = rightchild

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent
