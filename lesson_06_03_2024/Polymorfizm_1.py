class Tree:
    def draw(self):
        pass

class SlashTree(Tree):
    def draw(self):
        print(" / \\")
        print("// \\\\")

class StarTree(Tree):
    def draw(self):
        print(" / \\")
        print("/ ** \\")

class PlusTree(Tree):
    def draw(self):
        print(" / \\")
        print("/ ++ \\")

trees = [SlashTree(), StarTree(), PlusTree()]


for tree in trees:
    tree.draw()
    print()
