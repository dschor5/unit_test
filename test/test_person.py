import unittest
from source.calculator.person import Person

class TestPerson(unittest.TestCase):
    """Test class for main file."""

    def setUp(self):
        self.p = Person()
        
    def tearDown(self):
        self.p = None

    def test_first_name(self):
        """Test first name functions"""
        self.assertEqual(self.p.first_name, "")
        self.assertEqual(self.p.last_name,  "")
        self.assertEqual(self.p.email,      "")
        self.p.first_name = "John"
        self.assertEqual(self.p.first_name, "John")
        self.assertEqual(self.p.last_name,  "")
        self.assertEqual(self.p.email,      "")
        
    def test_last_name(self):
        """Test last name functions"""
        self.assertEqual(self.p.first_name, "")
        self.assertEqual(self.p.last_name,  "")
        self.assertEqual(self.p.email,      "")
        self.p.last_name = "Smith"
        self.assertEqual(self.p.first_name, "")
        self.assertEqual(self.p.last_name,  "Smith")
        self.assertEqual(self.p.email,      "")
        
    def test_email(self):
        """Test email functions"""
        self.assertEqual(self.p.first_name, "")
        self.assertEqual(self.p.last_name,  "")
        self.assertEqual(self.p.email,      "")
        self.p.first_name = "John"
        self.p.last_name = "Smith"
        self.assertEqual(self.p.first_name, "John")
        self.assertEqual(self.p.last_name,  "Smith")
        self.assertEqual(self.p.email,      "John.Smith@gmail.com")

    def test_str(self):
        """Test __str__ function"""
        self.assertEqual(self.p.__str__() == "")
        self.p.first_name = "John"
        self.p.last_name = "Smith"          
        self.assertEqual(self.p.__str__() == "John Smith")      

    def test_repr(self):
        """Test __repr__ function"""  
        self.assertEqual(self.p.__str__() == "")
        self.p.first_name = "John"
        self.p.last_name = "Smith"          
        self.assertEqual(self.p.__str__() == "Person(John Smith)")      