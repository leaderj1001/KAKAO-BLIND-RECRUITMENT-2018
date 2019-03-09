import sys
# 재귀 최대 깊이를 지정해주는 것. 지정해주지 않으면 런타임 오류가 난다.
sys.setrecursionlimit(10 ** 6)


class Node(object):
    def __init__(self, key, level, index):
        self.key = key
        self.level = level
        self.index = index
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.head = None
        self.preorder_result = []
        self.postorder_result = []

    def insert(self, data):
        current_Node = self.head
        if self.head == None:
            self.head = Node(data[0][0], data[0][1], data[1])
        else:
            while True:
                if current_Node.key < data[0][0]:
                    if current_Node.right is None:
                        current_Node.right = Node(data[0][0], data[0][1], data[1])
                        break
                    else:
                        current_Node = current_Node.right

                elif current_Node.key > data[0][0]:
                    if current_Node.left is None:
                        current_Node.left = Node(data[0][0], data[0][1], data[1])
                        break
                    else:
                        current_Node = current_Node.left

    def preSearch(self, current_Node):
        if current_Node is None:
            return 0
        self.preorder_result.append(current_Node.index)
        self.preSearch(current_Node.left)
        self.preSearch(current_Node.right)

    def postSearch(self, current_Node):
        if current_Node is None:
            return 0
        self.postSearch(current_Node.left)
        self.postSearch(current_Node.right)
        self.postorder_result.append(current_Node.index)


tree = Tree()


def solution(nodeinfo):
    answer = []
    index_sorted_nodeinfo = []
    for idx, info in enumerate(nodeinfo):
        index_sorted_nodeinfo.append([info, idx + 1])
    index_sorted_nodeinfo = sorted(index_sorted_nodeinfo, key=lambda x: (x[0][1], -x[0][0]), reverse=True)

    for info in index_sorted_nodeinfo:
        tree.insert(info)

    tree.preSearch(tree.head)
    answer.append(tree.preorder_result)
    tree.postSearch(tree.head)
    answer.append(tree.postorder_result)
    return answer