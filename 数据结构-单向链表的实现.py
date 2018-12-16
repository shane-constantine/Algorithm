# -*- coding: UTF-8 -*-

class Node(object):
	def __init__(self, item):
		self.elem = item
		self.next = None
		
class SingleLinklist(object):
	def __init__(self, node=None):
		self.__head = node
		
	def is_empty(self):
		return self.__head is None
	
	def length(self):
		cur = self.__head
		'''
		count = 1
		if not self.is_empty():
			return count
		while cur.next != None:
			cur = cur.next
			count += 1
		'''
		count = 0
		while cur != None:
			cur = cur.next
			count += 1
		return count 
		
	def travel(self):
		cur = self.__head
		while cur != None:
			print(cur.elem, end=' ')
			cur = cur.next
		print('')
		
	def add(self, item):
		node = Node(item)
		'''
		cur = self.__head
		if cur is None:
			self.__head = node
		else:
			self.__head = node
			node.next = cur
		'''
		node.next = self.__head
		self.__head = node
		
	def append(self, item):
		node = Node(item)
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node
			
	def insert(self, pos, item):
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			node = Node(item)
			count = 1
			pre = self.__head
			while count < (pos):
				count += 1
				pre = pre.next
			node.next = pre.next
			pre.next = node
			
	def remove(self,item):
		if self.is_empty():
            return
		cur = self.__head
		pre = None
		while cur != None:
			if cur.elem == item:
				if not pre:
					self.__head = cur.next
				else:
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next	

	def search(self, item):
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			cur = cur.next
		return False
			
			
if __name__ == "__main__":
	ll = SingleLinklist()
	ll.append(1)
	ll.append(2)
	ll.append(3)
	ll.insert(3, 4)
	print("length:",ll.length())
	ll.insert(0, 1)
	ll.insert(2, 2)
	ll.insert(4, 3)
	ll.insert(6, 4)
	ll.travel()
	print(ll.search(3))
	print(ll.search(5))
	ll.remove(1)
	print("length:",ll.length())
	ll.travel()			
			
			
			
			
			
		