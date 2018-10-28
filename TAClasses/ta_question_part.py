from interfaces.XML_interface import *

class ta_question_part:
    
    def __init__(self, mode,text, answer, possible_answers , name='  responseNaN  ', editing='useHTML', num_attempts=1,numberOfAttemptsLeft=1, numberOfTryAnother=0, numberOfTryAnotherLeft=0, allowRepublish='false',attributeAuthor='false', difficulty='0.0',  display='vertical', fixed='    ',  width='0.0'):
        self.mode = mode
        self.text = text
        self.answer = answer
        self.possible_answers = possible_answers
        self.name = name
        self.editing = editing
        self.num_attempts = num_attempts
        self.numberOfAttemptsLeft = numberOfAttemptsLeft
        self.numberOfTryAnother = numberOfTryAnother
        self.numberOfTryAnotherLeft = numberOfTryAnotherLeft
        self.allowRepublish = allowRepublish
        self.attributeAuthor = attributeAuthor
        self.difficulty = difficulty
        self.display = display
        self.fixed = fixed
        self.width = width
        
    def get_mode(self):
        return self.mode
    
    def get_answer(self):
        return self.answer
    
    def get_possible_answers(self):
        return self.possible_answers
    
    def generate_xml(self):
        return generate_part(self.mode,self.text, self.answer, self.possible_answers , self.name, self.editing, self.num_attempts, self.numberOfAttemptsLeft, self.numberOfTryAnother, self.numberOfTryAnotherLeft, self.allowRepublish, self.attributeAuthor, self.difficulty,  self.display, self.fixed,  self.width)