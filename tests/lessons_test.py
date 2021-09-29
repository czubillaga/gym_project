import unittest 
from models.lesson import Lesson
from models.member import Member
from models.booking import Booking

class TestLesson(unittest.TestCase):

    def setUp(self):
        self.lesson = Lesson('2021-08-28', '14:00:00', 'Yoga Class', 60, 25)

    def test_lesson_has_date(self):
        self.assertEqual('2021-08-28', self.lesson.date)

    def test_lesson_has_time(self):
        self.assertEqual('14:00:00', self.lesson.time)

    def test_lesson_has_description(self):
        self.assertEqual('Yoga Class', self.lesson.description)

    def test_lesson_has_duration(self):
        self.assertEqual(60, self.lesson.duration)

    def test_lesson_has_capacity(self):
        self.assertEqual(25, self.lesson.capacity)

    def test_lesson_start_with_zero_booked(self):
        self.assertEqual(0, self.lesson.booked)