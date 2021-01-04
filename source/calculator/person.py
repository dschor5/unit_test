"""Module Person docstring"""

class Person:
    """Person object"""

    def __init__(self):
        """Initialization funciton"""
        self._first_name = None
        self._last_name  = None

    def _is_defined(self):
        """Check if the first and last name are defined.

        Returns:
            boolean: True if the first and last name are defined.
        """
        return self._first_name is not None and self._last_name is not None

    @property
    def first_name(self):
        """Get first name

        Returns:
            string: first_name
        """
        f_name = ""
        if self._first_name is not None:
            f_name = self._first_name
        return f_name

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
        l_name = ""
        if self._last_name is not None:
            l_name = self._last_name
        return l_name

    @last_name.setter
    def last_name(self, new_last_name):
        """Set last name"""
        self._last_name = new_last_name

    @property
    def email(self):
        """Returns email address"""
        e_str = ""
        if self._is_defined():
            e_str = self._first_name + "." + self._last_name + "@gmail.com"
        return e_str

    def __str__(self) -> str:
        """String representation"""
        new_str = ""
        if self._is_defined():
            new_str = self._first_name + " " + self.last_name
        return new_str

    def __repr__(self):
        """String representation of Person object"""
        new_str = "Person()"
        if self._is_defined():
            new_str = 'Person({} {})'.format(self._first_name, self._last_name)
        return new_str
