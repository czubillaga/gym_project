import unittest 
from models.lesson import Lesson
from models.member import Member
from models.booking import Booking

class TestBooking(unittest.TestCase):

    def setUp(self):
        member = Member('Zubillaga', 'Carlos', 'premium')
        lesson = Lesson('2021-08-28', '14:00:00', 'Yoga Class', 60, 25)
        self.booking = Booking(member, lesson)

    def test_booking_has_member_object(self):
        self.assertEqual('Carlos', self.booking.member.first)

    def test_booking_has_lesson_object(self):
        self.assertEqual('Yoga Class', self.booking.lesson.description)