from lxml import etree
from ta_xml import *

class ta_module:
    
    def __init__(self,meta, author, school):
        self.meta = meta
        self.author = author
        self.school = school
        self.question_list = []
        
    def append_question(self, question):
        self.question_list.append(question)
        
    def get_questions(self):
        return self.question_list
    
    def get_num_questions(self):
        return len(self.question_list)
    
    def generate_xml(self):
        # needs to generate the parts part first with question part!
        module = generate_course_module()  
        module.append(self.meta.generate_xml())
        for element in self.question_list:
            module.append(element.generate_xml())
        module.append(self.author.generate_xml())
        module.append(self.school.generate_xml())
        return module