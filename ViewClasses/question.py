from TAClasses.ta_question import *
from interfaces.mta_interface import *

class question:
    
    def __init__(self, name, text="", comment="", correct_ans=0):
        self.name = name
        self.text = text
        self.comment = comment
        self.correct_ans = correct_ans
        
    def get_name(self):
        return self.name
    
    def get_text(self):
        return self.text
    
    def set_name(self, name):
        self.name = name
    
    def set_text(self, text):
        self.text = text
    
    def get_comment(self):
        return self.comment
    
    def set_comment(self, comment):
        self.comment = comment
        
    def get_correct_ans(self):
        return self.correct_ans
    
    def set_correct_ans(self, correct_ans):
        self.correct_ans = correct_ans

class mc_question(question):
    def __init__(self, name, text="",type="MC", shuffle=True, choices=[], correct=0, comment=""):
        if type not in ["MC", "MS"]:
            raise ValueError("Value must be either MC [multiplechoice] or MS [Multiple Selection]")
        question.__init__(self,  name=name, text=text,  comment=comment, correct_ans=correct )
        self.type = type
        self.shuffle = shuffle
        self.choices = choices
        
    def get_shuffle(self):
        return self.shuffle
    
    def get_choices(self):
        return self.choices
    
    def set_shuffle(self, shuffle):
        self.shuffle = shuffle

    def set_choices(self, choices):
        self.choices = choices
        
    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type=types
        
    def generate_ta_question(self):
        question = ta_question_generation(self)
        return question        