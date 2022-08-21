class Document: 
  def display(self): 
   print("Rendering file") 
 
class PDF(Document): 
  def display(self): 
    print("Rendering PDF file") 
 
class MicrosoftWord(Document): 
  def display(self): 
    print("Rendering Microsoft Word file") 
 
doc1 = Document() 
doc2 = PDF() 
doc3 = MicrosoftWord() 
 
doc3.display()