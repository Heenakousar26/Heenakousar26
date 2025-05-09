import os

class Portfolio: def init(self): self.name = "Your Name" self.skills = ["HTML", "CSS", "JavaScript", "Python"] self.projects = [ {"title": "Project Title 1", "description": "Brief description of the project."}, {"title": "Project Title 2", "description": "Brief description of the project."} ]

def display_about(self):
    return f"Name: {self.name}\nA brief description about yourself, your background, and your career goals."

def display_skills(self):
    return "Skills:\n" + "\n".join(self.skills)

def display_projects(self):
    projects_info = "Projects:\n"
    for project in self.projects:
        projects_info += f"Title: {project['title']}\nDescription: {project['description']}\n\n"
    return projects_info

def display_contact(self):
    return "Contact:\nPlease reach out via email."

def display_portfolio(self):
    os.system('clear' if os.name == 'posix' else 'cls')
    print("Welcome to the Personal Portfolio")
    print("-----------------------------")
    print(self.display_about())
    print("\n" + self.display_skills())
    print("\n" + self.display_projects())
    print("\n" + self.display_contact())

if name == "main": portfolio = Portfolio() portfolio.display_portfolio()
