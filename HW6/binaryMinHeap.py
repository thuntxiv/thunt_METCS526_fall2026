# METCS 526 Fall 2026 - HOMEWORK 6
# Author: Tyler Hunt; Professor: Dr. David Mellor

#------------------------------PROBLEM 2----------------------------

class Node:
    '''
    A node intended for binary heaps, holding parent and children references along with a contained value.
    '''
    def __init__(self, parent, value):
      self.parent = parent
      self.value = value
      self.left = None
      self.right = None

class BinaryMinHeap():
  '''
  An ADT representing a Binary Min Heap, with the smallest value at the root and increasing values traveling down
  the heap. 
  '''
  def __init__(self):
    self.insertion_pos = 1 # Size = insertion_pos - 1
    self.root = None

  def insert(self, value):
    '''
    Inserts the given value into the heap at the next insertion position, then bubbles the value up if
    needed to maintain the heap order property.

    PARAMETERS
      value:Any<Comparable>
        The value to be inserted into the heap
    RETURN
      None
    '''
    if self.insertion_pos == 1: # No values yet: set the root
        self.root = Node(None, value)
    else:
      path = f"{self.insertion_pos:b}" # Use a string of the binary insertion position to determine path
      curr_node = self.root # Keep track of the previous node so that its left/right pointer can be updated
      next_node = curr_node
      for i in range(1, len(path)): # Insertion position in binary starts with '1' for the root, so ignore first digit
        # In the binary value: 0 = left subtree, 1 = right subtree
        if path[i] == "0":
          next_node = curr_node.left
        else:
          next_node = curr_node.right
        if next_node is None:
          break
        curr_node = next_node
      # Create the new node and update the parent's left/right pointer accordingly
      next_node = Node(curr_node, value)
      if path[-1] == "0":
        curr_node.left = next_node
      else:
        curr_node.right = next_node
      self.bubble_up(next_node) # Bubble the value up if needed
    self.insertion_pos += 1

  def peek(self):
    '''
    Returns the minimum value held in the heap without removing it.

    PARAMETERS
      None
    RETURN
      Any<Comparable>
        The minimum value of the heap
    '''
    if self.is_empty():
      raise IndexError("Heap is empty")
    return self.root.value
  
  def extract_min(self):
    '''
    Removes the minimum value at the top of the heap, then uses the most recently added leaf node to maintain heap order
    via bubbling down.

    PARAMETERS
      None
    RETURN
      Any<Comparable>
        The minimum value of the heap
    '''
    if self.is_empty():
      raise IndexError("Heap is empty")

    min_val = self.root.value
    if self.insertion_pos == 2: # Only one element in the heap
      self.root = None
    else: # More than one element present: move the last leaf to root and bubble down
      leaf = self.find_last_leaf()
      self.root.value = leaf.value

      # Remove the last leaf node's reference held by its parent node
      self.remove_child(leaf)

      # Start bubbling down from the root to maintain heap order
      self.bubble_down(self.root)
    self.insertion_pos -= 1
    return min_val

  def find_last_leaf(self):
    '''
    Helper function for extract_min() and delete() that returns the most recently inserted leaf node

    PARAMETERS
      None
    RETURN
      NODE
        The most recently inserted node in the heap (i.e. the node at insertion_pos - 1)
    '''
    path = f"{self.insertion_pos - 1:b}" # Use a string of the binary insertion position to determine path
    curr_node = self.root
    for i in range(1, len(path)):
      # In the binary value, 0 = left subtree, 1 = right subtree
      if path[i] == "0":
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right
    return curr_node
  
  def delete(self, value):   
    '''
    Returns a boolean indicating whether a node with the given value was found in the heap and
    successfully deleted.

    PARAMETERS
      value:Any<Comparable>
        The value of the node to be searched for and deleted
    RETURN
      BOOL
        True if a node with the given value was found and deleted from the heap
        False if the node was not found and no deletion was made
    ''' 
    if self.is_empty(): # Can't delete from an empty heap
      return False

    # Search the tree for the first node with the given value
    target_node = self.find(self.root, value)
    if target_node is None:
      return False
    if self.insertion_pos == 2: # Deleting the root
      self.root = None
    else: # Deleting from one of the subtrees
      leaf = self.find_last_leaf()
      if target_node == leaf: # Deleting the most recently added node: No fixing needed for level order
        self.remove_child(leaf)
      else: # Need to patch hole in the level order
        # Move the most recently added leaf in place of the deleted node
        target_node.value = leaf.value
        self.remove_child(leaf)

        # Bubble up or down depending on the node's value to maintain heap order
        if target_node.parent is not None and target_node.value < target_node.parent.value:
          self.bubble_up(target_node)
        else:
          self.bubble_down(target_node)
    self.insertion_pos -= 1
    return True

  def find(self, curr_node:Node, value):
    '''
    Helper function for delete() that recursively searches the heap for the given value and
    returns the first occurrence of the value. If the value appears in both subtrees, the left
    subtree is given priority.

    PARAMETERS
      curr_node:NODE
        The current node that is being searched for the given value
      value:Any<Comparable>
        The value of the desired node
    RETURN
      NODE
        The first node found in the heap with the given value
    '''
    # Base cases: Node is None or value is found
    if curr_node is not None:  
      if curr_node.value == value:
        return curr_node

      # Search left and right subtrees for the value
      left_tree_result = self.find(curr_node.left, value)
      right_tree_result = self.find(curr_node.right, value)

      # If the value is found in both subtrees, prioritize the left
      if left_tree_result is not None and left_tree_result.value == value:
        return left_tree_result
      elif right_tree_result is not None and right_tree_result.value == value:
        return right_tree_result
    return None

  def remove_child(self, child:Node):
    '''
    Helper function for delete() that removes the given child's left/right reference held by its parent node,
    if it exists

    PARAMETERS
      child:NODE
        The child node to be detached from its parent
    RETURN
      None
    '''
    parent = child.parent
    if parent is not None:
      if parent.left == child:
        parent.left = None
      else:
        parent.right = None
  
  def build(self, values:list):
    '''
    Overrides the current contents of the heap and rebuilds it with the given list of values

    PARAMETERS
      values:LIST<comparable>
        A list of elements of the same type that can be compared with < and >
    RETURN
      None
    '''
    self.root = None
    self.insertion_pos = 1

    for value in values:
      self.insert(value)

  def heap_sort(self):
    '''
    Returns a sorted list of all values currently in the heap while leaving the heap itself unaffected.

    PARAMETERS
      None
    RETURN
      LIST<Comparable>
        A sorted list of all elements currently contained in the heap
    '''
    heap_copy = BinaryMinHeap()

    def copy_vals(node):
      '''
      Traverses the heap via the given node recursively and adds all found values into
      the heap copy.
      '''
      nonlocal heap_copy
      if node is not None: # Recursively traverse all tree nodes to copy into new heap
        heap_copy.insert(node.value)

        copy_vals(node.left)
        copy_vals(node.right)

    copy_vals(self.root)

    sorted_list = []

    while not heap_copy.is_empty():
      sorted_list.append(heap_copy.extract_min())
    return sorted_list
  
  def is_empty(self):       
    '''
    Returns a boolean indicating whether the heap is empty or not

    PARAMETERS
      None
    RETURN
      BOOL
        True if there are no elements currently in the heap
        False if there is at least one element in the heap
    '''
    return self.insertion_pos == 1
      
  def __len__(self):
    '''
    Returns the number of elements contained in the heap.

    RETURN
      INT
        An integer indicating the number of elements currently in the heap
    '''
    return self.insertion_pos - 1

  def bubble_up(self, node:Node):
    '''
    Helper function for insert() and delete() that checks if the given node must
    be moved up in the heap to maintain the heap property, and if so, the node is
    moved upward recursively until the heap order is restored.

    PARAMETERS
      node:NODE
        The current node to check if it can be bubbled up or not
    RETURN
      None
    '''
    parent = node.parent
    if parent is not None and node.value < parent.value:
      self.swap(node, parent)
      self.bubble_up(parent)

  def bubble_down(self, node:Node):
    '''
    Helper function for extract_min() and delete() that checks if the given node
    must be moved down in the heap to maintain the min heap property, and if so,
    the node is moved downward recursively until the heap order is restored.

    PARAMETERS
      node:NODE
        The current node to check if it can be bubbled down or not
    RETURN
      None
    '''
    target = None
    if node.right is None:
        target = node.left
    elif node.left is None:
        target = node.right
    else:
      if node.left.value < node.right.value: # Min heap, see if either child is less than this node
        target = node.left
      else:
        target = node.right
    # Bubble down recursively if either child is less than node (prioritize child with lesser value)
    if target is not None and target.value < node.value:
      self.swap(node, target)
      self.bubble_down(target)

  def swap(self, node1:Node, node2:Node):
    '''
    Helper function for bubble_up() and bubble_down() that switches the values of the
    two given nodes.

    PARAMETERS
      node1:NODE
        The first node to swap
      node2:NODE
        The second node to swap
    RETURN
      None
    '''
    node1.value, node2.value = node2.value, node1.value

#-------------------------------------------------------------------------------------------
  def print_heap(self):
    '''
    A printing function that displays the heap to stdout in a vertical tree format. Provided by ChatGPT.

    PARAMETERS
      None
    RETURN
      None
    '''
    if self.root is None:
      print("Empty heap")
      return

    # Determine the height of the tree
    def get_height(node):
      if node is None:
        return 0
      return 1 + max(get_height(node.left), get_height(node.right))

    height = get_height(self.root)

    # Allocate space for the tree
    width = (2 ** height) * 4
    canvas = [[" "] * width for _ in range(height * 2 - 1)]

    # Recursively place nodes and branches
    def draw(node, row, col, offset):
      if node is None:
        return

      value = str(node.value)

      # Place the node value
      start = max(0, col - len(value) // 2)
      for i, char in enumerate(value):
        if start + i < width:
          canvas[row][start + i] = char

      if row + 1 < len(canvas):

        # Left child
        if node.left:
            left_col = col - offset
            branch_col = (col + left_col) // 2

            canvas[row + 1][branch_col] = "/"
            draw(node.left, row + 2, left_col, offset // 2)

        # Right child
        if node.right:
            right_col = col + offset
            branch_col = (col + right_col) // 2

            canvas[row + 1][branch_col] = "\\"
            draw(node.right, row + 2, right_col, offset // 2)

    draw(self.root, 0, width // 2, width // 4)

    # Print the resulting tree
    for row in canvas:
      print("".join(row).rstrip())
#--------------------------------------------------------------------------------------

def hardcoded_testing():
  '''
  Misc. function for hardcoded test cases
  '''
  heap = BinaryMinHeap()
  heap.insert(4)
  heap.insert(5)
  heap.insert(6)
  heap.print_heap()
  heap.insert(2)
  heap.insert(3)
  heap.insert(4)

  heap.print_heap()

  sorted_list = heap.heap_sort()
  print(sorted_list)
  heap.print_heap()

  new_heap = BinaryMinHeap()
  new_heap.build(sorted_list)
  new_heap.print_heap()

def main():
  '''
  Reads stdin for a list of integer values, then creates a binary min heap from those values.
  The heap is printed after every insertion.
  '''
  #hardcoded_testing()
  values = input().strip()
  values = values[1:len(values) - 1].split(", ")
  values = [int(x) for x in values if x != '']
  print(f"Input values: {values}")

  heap = BinaryMinHeap()
  for value in values:
    print()
    print(f"After insert({value}):")
    heap.insert(value)
    heap.print_heap()

if __name__ == "__main__":
  main()