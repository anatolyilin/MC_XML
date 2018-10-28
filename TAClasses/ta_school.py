from ta_xml import *

class ta_school:
    def __init__(self, name,  school_uid="4d371c02-0aef-47ff-a091-c676055f80fc"):
        self.school_uid = school_uid
        self.name = name
        
    def get_school_name(self):
        return self.name
        
    def generate_xml(self):
        return generate_school(self.school_uid, self.name)