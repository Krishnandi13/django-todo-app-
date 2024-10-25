from django.test import TestCase
from tasks.models import Task
# Create your tests here.


class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(
            title="Do a 10 push up", 
            description="Thibs  djbcbcj kcb", 
            due_date='2024-08-26', 
            due_time='12:00'
        )
        Task.objects.create(
            title='Go for a walk', 
            description="bcdjc jjkcjdjkj", 
            due_date='2024-08-28', 
            due_time='17:45'
        )
        Task.objects.create(
            title='Read 2 chapters of a good book',
            description='Book markup the new words',
            due_date='2024-08-21',
            due_time='15:00',
            completed='True'
        )
        
    def test_data_consistency(self):
        task = Task.objects.get(title="Do a 10 push up") 
        task2 = Task.objects.get(title='Go for a walk')  
        self.assertEqual(task.description, "Thibs  djbcbcj kcb")
        self.assertEqual(task2.description, "bcdjc jjkcjdjkj")
        
    def test_is_completed(self):
        task3=Task.objects.get(title='Read 2 chapters of a good book')
        self.assertEqual(task3.completed,True)
        