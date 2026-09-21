# Binary Search Tree

class TreeNode:
    def __init__(self, value, left, right):
      self.value = value
      self.left = left
      self.right = right

class BinarySearchTree:
    def __init__(self):
      self.head = None
  
    def insert(self, value: int) -> None:
      new = TreeNode(value, None, None)
      
      if self.head is None:
        self.head = new
      else:
        cur = self.head
        while True:
           if cur.value > value:
              if cur.left is None:
                 cur.left = new
                 return
              cur = cur.left
           else:
              if cur.right is None:
                 cur.right = new
                 return
              cur = cur.right

    def search(self, value: int) -> bool:
        cur = self.head
        while True:
           if cur is None:
              return False
           
           if cur.value == value:
              return True
           elif cur.value > value:
              cur = cur.left
           else: 
              cur = cur.right
            
    # 오름차순으로 출력
    def print_in_order(self) -> None:
        cur = self.head
        while True:
           if cur.left is None:
              print(cur.value)
              


if __name__ == "__main__":
    bst = BinarySearchTree()
