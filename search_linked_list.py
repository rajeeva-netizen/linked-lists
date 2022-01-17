class Node:
  def __init__(self, data=None):
    self.data=data
    self.next=None

class single_linked_list:

  def __init__(self):
    self.Head=None
    self.Tail=None
    self.count=0

  def Iterate_list(self):
    current_data=self.Head
    while current_data:
      val = current_data.data
      current_data = current_data.next
      yield val
  def append_linked_list(self, data):
    node = Node(data)
    if(self.Tail):
      self.Tail.next=node
      self.Tail = node
    else:
      self.Head = node
      self.Tail = node
    self.count+=1

  def search_item(self, val):
      for node in self.Iterate_list():
        if val == node:
            return "Searched value is available", node
        return "Searched value is not available"
    
          

items = single_linked_list()
items.append_linked_list(34)
items.append_linked_list(345)
items.append_linked_list(4)
items.append_linked_list(3445)
val = int(input('enter the value to search:'))
print(items.search_item(val))