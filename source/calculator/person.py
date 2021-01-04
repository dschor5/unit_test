"""Person object"""
class Person:
  
   def __init__(self):
      """Initialization funciton"""
      self._first_name = ""
      self._last_name  = ""
   
   @property
   def first_name(self):
      """Get first name
      
      Returns:
         string: first_name
      """
      return self._first_name
      
   @first_name.setter
   def first_name(self, new_first_name):
      """Set first name"""
      self._first_name = new_first_name
      
   @property
   def last_name(self):
      """Get last name
      
      Returns:
         string: last_name
      """
      return self._last_name
      
   @last_name.setter
   def last_name(self, new_last_name):
      """Set last name"""
      self._last_name = new_last_name
      
   @property
   def email(self):
      """Returns email address"""
      if(self._first_name == "" or self._last_name == ""):
         return ""
      return self._first_name + "." + self._last_name + "@gmail.com"
      
   