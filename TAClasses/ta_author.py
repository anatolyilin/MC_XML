from ta_xml import *

class ta_author:
    def __init__(self, displayName, author_uid="02037092-3d70-4051-8447-b7cd2beef048", instanceUid="899d2f9c-1ea7-4c10-9e5b-805f88434028",defaultSchool="4d371c02-0aef-47ff-a091-c676055f80fc"):
        self.displayName= displayName
        self.author_uid = author_uid
        self.instanceUid = instanceUid
        self.defaultSchool = defaultSchool
    
    def get_author(self):
        return self.displayName
        
    def generate_xml(self):
        return generate_author(self.author_uid, self.instanceUid, self.defaultSchool, self.displayName)