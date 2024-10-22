from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task, TaskStatus
from profiles.models import Profile

class TaskCompletionTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')

        # Спробуй отримати профіль, якщо його немає, то створити
        self.profile, created = Profile.objects.get_or_create(user=self.user)

    def test_task_completion_updates_profile(self):
        # Створюємо завдання
        task = Task.objects.create(title='Test Task', description='This is a test task.')

        # Створюємо статус завдання
        task_status = TaskStatus.objects.create(task=task, user=self.user, completed=False)

        # Позначаємо завдання як завершене
        task_status.completed = True
        task_status.save()

        # Оновлюємо профіль
        self.profile.refresh_from_db()

        # Перевіряємо кількість виконаних завдань і рівень
        self.assertEqual(self.profile.completed_tasks_count, 1)
        self.assertEqual(self.profile.level, 0)  # 1 завдання - рівень не підвищено

        # Виконаємо ще два завдання
        for i in range(2):
            task = Task.objects.create(title=f'Test Task {i+2}', description=f'Test task {i+2}')
            task_status = TaskStatus.objects.create(task=task, user=self.user, completed=False)
            task_status.completed = True
            task_status.save()

        # Оновлюємо профіль
        self.profile.refresh_from_db()

        # Тепер рівень має бути підвищено
        self.assertEqual(self.profile.completed_tasks_count, 3)
        self.assertEqual(self.profile.level, 1)  # Після 3 виконаних завдань рівень має бути 1
