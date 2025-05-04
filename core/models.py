from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='projects/')
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class GladysOro(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()

    def experience(self):
        return [
            {'2024-present': 'Backend Developer | The Benchmarking Network LTD'},
            {'2022-2024': 'Junior Developer | MadKollections'},
        ]

    def skills(self):
        return {
            'frontEnd': ['HTML5/CSS3', 'JavaScript', 'Bootstrap', 'Responsive Design'],
            'backEnd': ['Python', 'Django', 'Flask', 'FastAPI', 'Node.js', 'RESTful APIs', 'PostgreSQL', 'MSSQL'],
            'tools': ['Git', 'Docker', 'AWS', 'VS Code', 'Postman'],
            'softSkills': ['Problem Solving', 'Team Collaboration', 'Agile Methodology', 'Technical Writing', 'Effective Communication']
        }

    def certifications(self):
        return [
            {'name': 'Agile Project Management Foundation (AgilePM)', 'year': '2025'},
            {'name': 'AWS Certified Developer', 'year': '2023'},
            {'name': 'Python Professional Certification', 'year': '2022'}
        ]

    def education(self):
        return [
            {'degree': 'MSc International Business and Management', 'institution': 'University of Bradford'}
        ]

    def interests(self):
        return [ 'Tech Blogging', 'AI/ML Exploration', 'Web Accessibility', 'Cloud Computing']

    motto = "Code is poetry, functionality is art"
#