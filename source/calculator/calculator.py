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

    def __private_function(self):
        """Some private function"""

    @staticmethod
    def addition(var_a, var_b):
        """Adds the list of arguments

        Args:
          var_a (float): First value
          var_b (float): Second value

        Returns:
          float: Sum

        Raises:
            TypeError: If something other than float or int is used.
        """
        if((isinstance(var_a, (int, float)) and isinstance(var_b, (int, float)))):
            var_r = var_a + var_b
        else:
            raise ValueError
        return var_r

    @staticmethod
    def subtraction(var_a, var_b):
        """Subtracts second value from first value.

        Args:
          var_a (float): First value
          var_b (float): Second value

        Returns:
          float: Subtraction
        """
        return var_a - var_b

    @staticmethod
    def multiplication(var_a, var_b):
        """Multiply two numbers.

        Args:
          var_a (float): First value
          var_b (float): Second value

        Returns:
          float: Multiplication
        """
        return var_a * var_b

    @staticmethod
    def division(var_a, var_b):
        """Divide first value by second value

        Args:
          var_a (float): First value
          var_b (float): Second value

        Returns:
          float: Division
        """
        return var_a / var_b
