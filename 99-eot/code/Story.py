import Print, get

class Create:
  def __init__(self):
    self.pages = {}  # create a dictionary of story pages
  
  def display(self, page):
    while page != 'end':
      Print.clear()
      print()
      Print.yellow(self.pages[page][0])
      choices = len(self.pages[page][1])
      for choice in range(choices):
        Print.green("\n\t" + str(choice+1) + " - " + self.pages[page][1][choice])
      page = self.pages[page][2][get.number(choices)]
  
  def start(self):
    self.display("start")