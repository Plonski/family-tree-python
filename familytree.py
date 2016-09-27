"""
Name the project FamilyTree_Kim.py
"""


class Family_tree():

    def __init__(self):
        self.family_tree = {"siblings": [], "parents": [], "half-siblings": [], "cousins": []}

class Family_member():

    def __init__(self, name, relation):
        self.name = name
        self.relation = relation

class Person:

    def __init__(self, name):
        self.name = name
        self.family_tree = Family_tree()

    def add_parents(self, parent_one, parent_two):
        pass

    def add_sibling(self, sibling):
        self.family_tree.family_tree['siblings'].append(sibling)

    def list_relation(self, relation):
        print(self.family_tree.family_tree[relation])

def fileRead():
    filename = input()
    # open file and read all text
    f = open(filename, mode='r')
    text = f.read()
    # tokenize words with " " delimiter
    words = text.split()
    # print words
    for word in words:
        print(word)

def main():

    fileRead()

    x = Person("Thomas")
    Person("Mary")
    Person("Jeff")
    Person("Matt")


    x.add_sibling("Jeff")
    x.add_sibling("Mary")
    x.list_relation("siblings")

if __name__ == '__main__':
    main()
