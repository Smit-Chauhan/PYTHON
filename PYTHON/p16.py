class Slideshow: 
  def _init_(self, slides): 
    self.slides = slides 
    self.current = 1 
  
  def viewNextSlide(self): 
    self.current += 1 
  
  def play(self): 
    while self.current <= self.slides: 
      print('Slide', self.current) 
      self.viewNextSlide() 
 
slideshow = Slideshow(5) 
slideshow.play()

