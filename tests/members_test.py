import unittest 
from models.lesson import Lesson
from models.member import Member
from models.booking import Booking

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member('Zubillaga', 'Carlos', 'premium')

    def test_member_has_first(self):
        self.assertEqual('Carlos', self.member.first)

    def test_member_has_last(self):
        self.assertEqual('Zubillaga', self.member.last)

    def test_member_has_type(self):
        self.assertEqual('premium', self.member.type)