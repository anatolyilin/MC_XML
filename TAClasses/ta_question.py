from ta_xml import *
from lxml import etree

class ta_question:
    
    def __init__(self, uid, name, cmAttributed="true", cmWeight="0.0", modifiedBy="02037092-3d70-4051-8447-b7cd2beef048", school="4d371c02-0aef-47ff-a091-c676055f80fc" , mode="Inline",  chainId=0 , comment='',  editing='useHTML', numberOfAttempts=1,numberOfAttemptsLeft=1, numberOfTryAnother=0, numberOfTryAnotherLeft=0, privacy=10, allowRepublish='false',attributeAuthor='false', difficulty='0.0', text='',width=0.0, weighting=1, numbering='alpha', part=None, modifiedIn=13.0):
        # fields apply to the question, not the question part(s)
        self.uid = uid
        self.name=name
        self.cmAttributed = cmAttributed
        self.cmWeight = cmWeight
        self.modifiedBy = modifiedBy
        self.school=school
        self.mode=mode
        self.chainId=chainId
        self.comment=comment
        self.editing=editing
        self.numberOfAttempts=numberOfAttempts
        self.numberOfAttemptsLeft=numberOfAttemptsLeft
        self.numberOfTryAnother=numberOfTryAnother
        self.numberOfTryAnotherLeft=numberOfTryAnotherLeft
        self.privacy=privacy
        self.modifiedIn = modifiedIn
        self.allowRepublish=allowRepublish
        self.attributeAuthor=attributeAuthor
        self.difficulty=difficulty
        self.text=text
        self.width=width
        self.weighting=weighting
        self.numbering=numbering
        self.parts=[]
        if part != None:
            self.parts.append(part)

    def append_part(self, part):
        self.parts.append(part)
        
    def get_parts(self):
        return self.parts
        
    def set_name(self,q_name):
        self.name = q_name
    
    def get_name(self):
        return self.name
    
    def get_uid(self):
        return self.uid
    
    def get_comment(self):
        return self.comment
    
    def set_comment(self,comment):
        self.comment = comment
        
    def set_text(self,text):
        self.text = text
        
    def get_text(self):
        return self.text
    
    def generate_xml_parts(self):
        xml_parts = etree.Element('parts')    
        for part in self.parts:
            part_xml = part.generate_xml()
            xml_parts.append(part_xml)
        return xml_parts       
    def generate_xml(self):
        question = generate_question(self.uid, self.name,self.comment, self.text, self.mode,self.cmAttributed, self.cmWeight, self.modifiedBy, self.school ,  self.chainId , self.editing, self.numberOfAttempts, self.numberOfAttemptsLeft, self.numberOfTryAnother, self.numberOfTryAnotherLeft, self.privacy, self.modifiedIn, self.allowRepublish, self.attributeAuthor, self.difficulty,  self.width, self.weighting, self.numbering )
        question.append(self.generate_xml_parts())
        return question