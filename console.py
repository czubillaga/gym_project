import pdb

from models.booking import Booking
from models.lesson import Lesson
from models.member import Member

import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository
import repositories.booking_repository as booking_repository

member_repository.delete_all()
lesson_repository.delete_all()
booking_repository.delete_all()

member1 = Member('Zubillaga', 'Carlos', 'premium')
member2 = Member('Webber', 'Oscar', 'standard')
lesson1 = Lesson('29/08/2021', '14:00', 'Spin Class', 50, 25)
lesson2 = Lesson('29/08/2021', '15:30', 'Yoga Class', 45, 25)
booking1 = Booking(member1, lesson2)
booking2 = Booking(member2, lesson1)

member_repository.save(member1)
member_repository.save(member2)

lesson_repository.save(lesson1)
lesson_repository.save(lesson2)

booking_repository.save(booking1)
booking_repository.save(booking2)

all_bookings = booking_repository.select_all()

for booking in all_bookings:
    print(booking.__dict__)

# lesson_repository.delete(lesson1)

# member_repository.delete(member1)

# all_lessons = lesson_repository.select_all()

# for lesson in all_lessons:
#     print(lesson.__dict__)

lesson = lesson_repository.select(lesson2.id)
print(lesson.__dict__)

member2.type = 'premium'
member_repository.update(member2)

member = member_repository.select(member2.id)
print(member.__dict__)