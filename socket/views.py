def index():
    with open('templates/index.html', 'r') as template:
        return template.read()
    
def blog():
    with open('templates/blog.html', 'r') as template:
        return template.read()

def about():
    with open('templates/about.html', 'r') as template:
        return template.read()

def contact():
    with open('templates/contact.html', 'r') as template:
        return template.read()

def not_found():
    with open('templates/404.html', 'r') as template:
        return template.read()

def method_not_allowed():
    with open('templates/405.html', 'r') as template:
        return template.read()
