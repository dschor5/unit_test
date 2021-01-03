"""My calculator object"""
class Calculator:
   """My constant #1"""
   CONSTANT_VAR = 4
   
   """My constant #2"""
   CONSTANT_VAR_2 = 5

   def __init__(self):
      """Initialization funciton"""
      self.public_var = 1
      self._protected_var = 2
      self.__private_var = 3
   

   
   def _protected_function(self):
      """Some protected function"""
      pass
      
   def __private_function(self):
      """Some private function"""
      pass

   def addition(self, a, b):
      """Adds the list of arguments
      
      Args:
        a (float): First value
        b (float): Second value
      
      Returns:
        float: Sum
        
      Raises:
         TypeError: If something other than float or int is used.
      """
      if((isinstance(a, int) or isinstance(a, float)) and
         (isinstance(b, int) or isinstance(b, float))):
         r = a + b
      else:
         raise ValueError
      return r
      
      
   def subtraction(self, a, b):
      """Subtracts second value from first value.
      
      Args:
        a (float): First value
        b (float): Second value
      
      Returns:
        float: Subtraction
      """
      return a - b
      
   def multiplication(self, a, b):
      """Multiply two numbers.
      
      Args:
        a (float): First value
        b (float): Second value
      
      Returns:
        float: Multiplication
      """
      return a * b
      
   def division(self, a, b):
      """Divide first value by second value
      
      Args:
        a (float): First value
        b (float): Second value
      
      Returns:
        float: Division
      """
      r = a / b