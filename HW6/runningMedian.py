# METCS 526 Fall 2026 - HOMEWORK 6
# Author: Tyler Hunt; Professor: Dr. David Mellor

from binaryMinHeap import BinaryMinHeap, Node

#------------------------------PROBLEM 3----------------------------

class BinaryMaxHeap(BinaryMinHeap):
  '''
  An ADT representing a Binary Max Heap, with the largest value at the root and decreasing values traveling down
  the heap from the root. Inherits from BinaryMinHeap
  '''

  def extract_min(self):
    raise TypeError("Cannot extract min from a max heap")

  def extract_max(self):
    '''
    Removes the maximum value at the top of the heap, then uses the most recently added leaf node to maintain heap order
    via bubbling down.

    PARAMETERS
      None
    RETURN
      Any<Comparable>
        The maximum value of the heap
    '''
    if self.is_empty():
      raise IndexError("Heap is empty")

    max_val = self.root.value
    if self.insertion_pos == 2: # Only one element in the heap
      self.root = None
    else: # More than one element present: move the last leaf to root and bubble down
      leaf = self.find_last_leaf()
      self.root.value = leaf.value

      # Remove the last leaf node's reference from its parent node
      self.remove_child(leaf)

      # Start bubbling down from the root
      self.bubble_down(self.root)
    self.insertion_pos -= 1
    return max_val

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
        if target_node.parent is not None and target_node.value > target_node.parent.value:
          self.bubble_up(target_node)
        else:
          self.bubble_down(target_node)
    self.insertion_pos -= 1
    return True

  def heap_sort(self):
    '''
    Returns a sorted list of all values currently in the heap while leaving the heap itself unaffected.

    PARAMETERS
      None
    RETURN
      LIST<Comparable>
        A sorted list of all elements currently contained in the heap
    '''
    heap_copy = BinaryMaxHeap()

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
      sorted_list.append(heap_copy.extract_max())
    return sorted_list

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
    if parent is not None and node.value > parent.value:
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
      if node.left.value > node.right.value: # Min heap, see if either child is less than this node
        target = node.left
      else:
        target = node.right
    # Bubble down recursively if either child is less than node (prioritize child with lesser value)
    if target is not None and target.value > node.value:
      self.swap(node, target)
      self.bubble_down(target)

#------------------------------------------------------------------------------------------------

def running_median(sales):
  '''
  Populates and returns a list of the running medians given a list of integer sale amounts.

  PARAMETERS
    sales:LIST<INT>
      A list of integers representing the sale amounts for the day
  RETURN
    LIST<FLOAT>
      A list of the running medians, each element representing the median for the subset of the sales 
      list from index 0 to index i
  '''
  lower = BinaryMaxHeap() # Stores smaller (in values) half of all current sales with a max heap
  upper = BinaryMinHeap() # Stores larger half of all current sales with a min heap
  medians = []

  for sale in sales:
    # Start by inserting into lower, or generally insert into lower if the sale is <= lower's max
    if lower.is_empty() or sale <= lower.peek():
      lower.insert(sale)
    else: # Insert values > lower's max into upper
      upper.insert(sale)
    # Check if sizes are imbalanced, then move the max or min to the other heap if needed
    if len(lower) >= len(upper) + 2:
      upper.insert(lower.extract_max())
    elif len(upper) >= len(lower) + 2:
      lower.insert(upper.extract_min())

    median = 0.0
    # Odd length case: Peek from the heap with more values to get the middle value
    if len(lower) > len(upper):
      median = float(lower.peek())
    elif len(upper) > len(lower):
      median = float(upper.peek())
    # Even length case: Average the max/min values from each heap respectively
    else:
      median = (float(lower.peek()) + float(upper.peek())) / 2
    medians.append(median)
  return medians

def main():
    '''
    Reads input for the list of sale integer amounts, then returns the running medians in a list.
    '''
    values = input().strip()
    values = values[1:len(values) - 1].split(", ")
    values = [int(x) for x in values if x != '']

    print(running_median(values))

if __name__ == "__main__":
    main()