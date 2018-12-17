# -*- coding: UTF-8 -*-

class Node(object):
	def __init__(self, item):
		self.elem = item
		self.next = None
		
class SingleCycleLinkList(object):
	def __init__(self, node=None):
		self.__head = node
		if node:
			node.next = node
		
	def is_empty(self):	
		return self.__head is None
	
	def length(self):
		cur = self.__head
		if self.is_empty():
			return 0
		count = 1
		while cur.next != self.__head:
			cur = cur.next
			count += 1
		return count
		
	def travel(self):
		if self.is_empty():
			return
		cur = self.__head
		while cur.next != self.__head:  # 当链表中只有一个元素的时候，不进入循环，利用循环外的print输出。
			print(cur.elem, end=' ')	# 当链表中不止一个元素的时候，先输出再前进，会使最后一个元素没有输出，正好由循坏外的print补上
			cur = cur.next
		print(cur.elem)
		
	def add(self, item):
		node = Node(item)
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			node.next = self.__head
			cur = self.__head
			while cur.next != self.__head:
				cur = cur.next
			self.__head = node
			cur.next = node
			
	def append(self, item):
		node = Node(item)
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			cur = self.__head
			while cur.next != self.__head:
				cur = cur.next
			cur.next = node
			node.next = self.__head
			
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
			
	def remove(self, item):
		if self.is_empty():
			return
		cur = self.__head
		pre = None
		while cur.next != self.__head:
			if cur.elem == item:
				if cur == self.__head:
					rear = self.__head
					while rear.next != self.__head:
						rear = rear.next
					self.__head = cur.next
					rear.next = self.__head
				else:
					# 中间节点
					pre.next = cur.next
				return
			else:
				pre = cur
				cur = cur.next
		# 退出循环，cur指向尾节点
		if cur.elem == item:
			if cur == self.__head:
				# 链表只有一个节点
				self.__head = None
			else:
				# pre.next = cur.next
				pre.next = self.__head	

	def search(self, item):
		cur = self.__head
		while cur != self.head:
			if cur.elem == item:
				return True
			cur = cur.next
		return False
			
			

if __name__ == "__main__":
	ll = SingleCycleLinkList()
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
			
			
			
			
			
		
