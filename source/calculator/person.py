"""Module Person docstring"""

class Person:
    """Person object"""

    def __init__(self):
        """Initialization funciton"""
        self._first_name = ""
        self._last_name  = ""

    def _is_defined(self):
        """Check if the first and last name are defined.

        Returns:
            boolean: True if the first and last name are defined.
        """
        return self._first_name == "" and self._last_name == ""

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

    def __str__(self) -> str:
        """String representation"""
        new_str = ""
        if self._is_defined():
            new_str = self._first_name + " " + self.last_name
        return new_str

    def __repr__(self):
        """String representation of Person object"""
        return 'Person({} {})'.format(self._first_name, self._last_name)
