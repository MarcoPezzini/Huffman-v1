class mytree(object):
  def __init__(self, label, value, left=None, right=None):
      self.label = label  # The node label
      self.value = value  # The node value
      self.left = left    # Left child
      self.right = right  # Right child

  def insertLeft(self, child):
    self.left = child
  
  def insertRight(self, child):
    self.right = child

