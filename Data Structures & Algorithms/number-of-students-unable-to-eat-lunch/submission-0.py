from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        que_students = deque(students)
        que_sandwich = deque(sandwiches)
        sandwiches_left = len(sandwiches)
        unable_to_eat = 0

        while unable_to_eat < sandwiches_left:
            if que_students[0] == que_sandwich[0]:
                que_students.popleft()
                que_sandwich.popleft()
                sandwiches_left -= 1
                unable_to_eat = 0
            else:
                que_students.rotate(-1)
                unable_to_eat += 1
        
        return sandwiches_left

