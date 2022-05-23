#Initialize two pointers ptr1 and ptr2  at the p and  q
#Traverse through the lists,one node at a time.
#When ptr1 reaches the end of a list, then redirect it to q.
#similarly when ptr2 reaches the end of a list, redirect it to p.
#Once both of them go through reassigning, they will be equidistant from the collision point
#If at any node ptr1 meets ptr2, then it is the intersection node.
#After second iteration if there is no intersection node it returns NULL.
#where p and q are heads of the Linked lists 



class Node:
	def __init__(self, data = 0, next = None):
		self.data = data
		self.next = next

def intersectPoint(p, q):
	ptr1 = p
	ptr2 = q
	if (ptr1 == None or ptr2 == None):
		return None
	while (ptr1 != ptr2):
		ptr1 = ptr1.next
		ptr2 = ptr2.next
		if (ptr1 == ptr2):
			return ptr1
		if (ptr1 == None):
			ptr1 = q
		if (ptr2 == None):
			ptr2 = p
	return ptr1

def Print(node):

	if (node == None):
		print("None")
	while (node.next != None):
		print(node.data,end="->")
		node = node.next
	print(node.data)

# 1st Linked list is 3->6->9->15->30
# 2nd Linked list is 10->15->30
p = Node()
p.data = 10
q = Node()
q.data = 3
newNode = Node()
newNode.data = 8
q.next = newNode
newNode = Node()
newNode.data = 9
q.next.next = newNode
newNode = Node()
newNode.data = 12
p.next = newNode
q.next.next.next = newNode
newNode = Node()
newNode.data = 35
p.next.next = newNode
p.next.next.next = None
intersect_node = None

# Find the collision node of two linked lists
intersect_node = intersectPoint(p, q)
print("Collision points:",end="")
Print(intersect_node)
