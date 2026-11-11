'''
Estimated: 20 minutes
Actual: 25 minutes

'''

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages =[python, ruby, visual_basic]

print("The langauges that have dynamic typing are: ")
for language in languages:
    if language.is_dynamic():
        print(language.name)
