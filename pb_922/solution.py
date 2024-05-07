class Treenode:
	def __init__(self, parent=None, value=1):
		self.left = None
		self.rigth = None
		self.parent = parent
		self.islock = False
		self.value = value
	def add_tree(self, direction):
		if direction == "l":
			self.left = Treenode(self, self.value * 2)
		elif direction == "r":
			self.right = Treenode(self, self.value * 2 + 1)
	def is_locked(self):
		while self != None:
			if self.islock == True:
				return True
			self = self.parent
		return False
	def lock(self):
		if self.is_locked():
			return False
		while self != None:
			self.islock = True
			self = self.parent
		return True
	def unlock(self):
		if self.islock == False:
			return False
		if self.left != None and self.left.islock == True:
			return False
		if self.right != None and self.right.islock == True:
			return False
		while self != None:
			self.islock = False
			self = self.parent
		return True

treenode = Treenode()
treenode.add_tree("l")
treenode.left.add_tree("r")
print(treenode.value)
print(treenode.left.value)
print(treenode.left.right.value)
print(treenode.left.right.is_locked())
print(treenode.islock)
print(treenode.left.islock)
print(treenode.left.right.islock)
print(treenode.left.lock())
print(treenode.islock)
print(treenode.left.islock)
print(treenode.left.right.islock)
print(treenode.lock())
print(treenode.islock)
print(treenode.left.islock)
print(treenode.left.right.islock)
print("................")
print(treenode.left.unlock())
print(treenode.islock)
print(treenode.left.islock)
print(treenode.left.right.islock)

# another solution
# class TreeNode:
#     def __init__(self, value, parent=None):
#         self.value = value
#         self.parent = parent
#         self.left = None
#         self.right = None
#         self.is_locked = False
#         self.locked_descendants_count = 0

#     def is_locked(self):
#         return self.is_locked

#     def lock(self):
#         if self._can_lock_or_unlock():
#             self.is_locked = True
#             self._update_ancestors_locked_descendants_count(1)
#             return True
#         return False

#     def unlock(self):
#         if self._can_lock_or_unlock():
#             self.is_locked = False
#             self._update_ancestors_locked_descendants_count(-1)
#             return True
#         return False

#     def _can_lock_or_unlock(self):
#         if self.locked_descendants_count > 0:
#             return False
#         current = self.parent
#         while current:
#             if current.is_locked:
#                 return False
#             current = current.parent
#         return True

#     def _update_ancestors_locked_descendants_count(self, delta):
#         current = self.parent
#         while current:
#             current.locked_descendants_count += delta
#             current = current.parent


# # Example usage:
# root = TreeNode(1)
# root.left = TreeNode(2, parent=root)
# root.right = TreeNode(3, parent=root)
# root.left.left = TreeNode(4, parent=root.left)

# # Locking node 4
# print(root.left.left.lock())  # Output: True

# # Attempting to lock node 2 (parent of node 4)
# print(root.left.lock())  # Output: False, because one of its descendants is locked

# # Unlocking node 4
# print(root.left.left.unlock())  # Output: True

# # Now locking node 2 should succeed
# print(root.left.lock())  # Output: True
