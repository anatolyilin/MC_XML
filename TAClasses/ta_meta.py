from interfaces.XML_interface import *

class ta_meta:
    def __init__(self, name, description, privacy='10',autoModule='false', exportedFrom='f496fbff-6a44-46d8-a95c-82e23a24712e' ):
        self.name = convert_to_cdata(name)
        self.description = convert_to_cdata(description)
        self.privacy = privacy
        self.autoModule = autoModule
        self.exportedFrom = exportedFrom
        
    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name
        
    def generate_xml(self):
        return generate_meta(self.name, self.description, self.privacy, self.autoModule, self.exportedFrom)