class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        part1 = self.get_value(l1)
        print(part1)
        part2 = self.get_value(l2)
        print(part2)
        result = part1 + part2
        return result

    def get_value(self, node):
        count = 0
        part = 0
        while node != None:
            print(node.val)
            part = part + node.val * (10 ** count)
            node = node.next
            count = count + 1
        return part


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)
    s = Solution()
    print(s.addTwoNumbers(l1, l2))
