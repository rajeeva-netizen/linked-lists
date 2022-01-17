class Node:
  def __init__(self, data=None):
    self.data=data
    self.next=None

class single_linked_list:
  def __init__(self):
    self.Head=None
    self.Tail=None
    self.count=0

  
  def append_linked_list(self, data):
    node = Node(data)
    if(self.Tail):
      self.Tail.next=node
      self.Tail = node
    else:
      self.Head = node
      self.Tail = node
    self.count+=1

  def del_item(self, data):
        # Delete an item from the list
        current = self.Head
        prev = self.Head
        while current:
            if current.data == data:
                if current == self.Head:
                    self.Head = current.next
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next


  def Iterate_list(self):
    current_data=self.Head
    while current_data:
      val = current_data.data
      current_data = current_data.next
      yield val

items = single_linked_list()
items.append_linked_list(34)
items.append_linked_list(345)
items.append_linked_list(4)
items.append_linked_list(3445)
val = int(input('enter the value to search:'))
items.del_item(val)
for i in items.Iterate_list():
  print(i)