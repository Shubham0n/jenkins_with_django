from django.test import TestCase
from django.urls import reverse
from .models import EmployProfile

class EmployProfileListViewTest(TestCase):

    def setUp(self):
        """Set up sample employee profiles."""
        EmployProfile.objects.create(
            name="Alice", email="alice@example.com", phone_number="1111111111", total_experience=4
        )
        EmployProfile.objects.create(
            name="Bob", email="bob@example.com", phone_number="2222222222", total_experience=6
        )

    def test_emp_list_view(self):
        """Test if the employee list page loads correctly and displays the employees."""
        response = self.client.get(reverse('emp_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'emp_info_list.html')  # Ensure correct template
        self.assertContains(response, "Alice")
        self.assertContains(response, "Bob")

    def test_emp_list_view_empty(self):
        """Test if the employee list page loads correctly when no employees exist."""
        EmployProfile.objects.all().delete()  # Remove all employees
        response = self.client.get(reverse('emp_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No employees found")  # Modify based on actual message

    def test_emp_list_view_pagination(self):
        """Test if pagination works correctly (assuming 5 per page)."""
        for i in range(10):  # Create 10 employees
            EmployProfile.objects.create(
                name=f"Employee {i}", email=f"employee{i}@example.com", phone_number=f"99999999{i}",
                total_experience=i
            )
        
        response = self.client.get(reverse('emp_list') + "?page=1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Employee 0")
        self.assertContains(response, "Employee 4")  # Check for first 5 entries (if paginated)

        response = self.client.get(reverse('emp_list') + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Employee 5")
        self.assertContains(response, "Employee 9")  # Check next set of entries
