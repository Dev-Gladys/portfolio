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


class GladysOro:
    """
    Passionate about turning ideas into code
    Building digital experiences one line at a time
    """

    def __init__(self):
        self.name = 'Gladys Oro'
        self.role = 'Software Developer'
        self.email = 'ziglad.dev@gmail.com'

    def journey(self):
        return [
            {'2024-present': 'Backend Developer at The Benchmarking Network LTD'},
            {'2022-2023': 'Junior Developer at MadKollection'},
        
        ]

    def expertise(self):
        return {
            'frontEnd': [
                'HTML5/CSS3',
                'JavaScript',
                'Bootstrap',
                'Responsive Design'
            ],
            'backEnd': [
                'Python',
                'Django',
                'flask',
                'FastAPI',
                'Node.js',
                'RESTful APIs',
                'PostgreSQL',
                'MSSQL',
            ],
            'tools': [
                'Git',
                'Docker',
                'AWS',
                'VS Code',
                'Postman'
            ],
            'softSkills': [
                'Problem Solving',
                'Team Collaboration',
                'Agile Methodology',
                'Technical Writing',
                'Project Management'
            ]
        }

    def certifications(self):
        return [
            {
                'name': 'AWS Certified Developer',
                'year': '2023'
            },
            {
                'name': 'Python Professional Certification',
                'year': '2022'
            }
        ]

    def education(self):
        return [
            {
                'degree': 'MSc International Business and Management', 
                'institution': 'University of Bradford',
                
            }
        ]

    def interests(self):
        return [
            'Open Source Contributing',
            'Tech Blogging',
            'AI/ML Exploration',
            'Web Accessibility',
            'Cloud Computing'
        ]

       

    def get_current_project(self):
        return {
            'name': 'Portfolio Website',
            'tech': ['Django', 'JavaScript', 'Bootstrap'],
            'status': 'In Progress',
            'description': 'A personal portfolio showcasing my journey and projects'
        }

    # Life motto
    motto = "Code is poetry, functionality is art"
