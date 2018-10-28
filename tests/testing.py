from TAClasses.ta_school import *
from TAClasses.ta_author import *
from TAClasses.ta_question_part import *
from TAClasses.ta_question import *
from TAClasses.ta_meta import *
from TAClasses.ta_module import *
import unittest
from interfaces.XML_interface import *

class TestClasses(unittest.TestCase):

    def test_school(self):
        name = "TU Delft"
        my_school = ta_school(name)
        self.assertEqual(my_school.get_school_name(), name )
        
    def test_school_xml(self):
        expected = b'<school uid="4d371c02-0aef-47ff-a091-c676055f80fc"><name><![CDATA[TU Delft]]></name></school>'
        name = "TU Delft"
        my_school = ta_school(name)
        self.assertEqual(module_to_string(my_school.generate_xml()), expected )
        
    def test_author(self):
        name = "My Name"
        my_author = ta_author(name)
        self.assertEqual(my_author.get_author(), name )
        
    def test_author_xml(self):
        expected = b'<author defaultSchool="4d371c02-0aef-47ff-a091-c676055f80fc" instanceUid="899d2f9c-1ea7-4c10-9e5b-805f88434028" uid="02037092-3d70-4051-8447-b7cd2beef048"><displayName><![CDATA[My Name]]></displayName></author>'
        name = "My Name"
        my_author = ta_author(name)
        self.assertEqual(module_to_string(my_author.generate_xml()), expected )    
        
    def test_question_part(self):
        mode = "Multiple Choice"
        text = '    '
        answer = 3
        possible_answers = [1,2,3,4]
        q_part = ta_question_part(mode,text, answer, possible_answers , name='  responseNaN  ', editing='useHTML', num_attempts=1,numberOfAttemptsLeft=1, numberOfTryAnother=0, numberOfTryAnotherLeft=0, allowRepublish='false',attributeAuthor='false', difficulty='0.0',  display='vertical', fixed='    ',  width='0.0')
        self.assertEqual(q_part.get_mode(), mode)
        self.assertEqual(q_part.get_answer(), answer)
        self.assertEqual(q_part.get_possible_answers(), possible_answers)
        
    def test_question_part_xml(self):
        mode = "Multiple Choice"
        text = '    '
        answer = 3
        possible_answers = [1,2,3,4]
        q_part = ta_question_part(mode,text, answer, possible_answers , name='  responseNaN  ', editing='useHTML', num_attempts=1,numberOfAttemptsLeft=1, numberOfTryAnother=0, numberOfTryAnotherLeft=0, allowRepublish='false',attributeAuthor='false', difficulty='0.0',  display='vertical', fixed='    ',  width='0.0')
        expected = b'<part><mode>Multiple Choice</mode><name><![CDATA[  responseNaN  ]]></name><editing>useHTML</editing><numberOfAttempts>1</numberOfAttempts><numberOfAttemptsLeft>1</numberOfAttemptsLeft><numberOfTryAnother>0</numberOfTryAnother><numberOfTryAnotherLeft>0</numberOfTryAnotherLeft><allowRepublish>false</allowRepublish><attributeAuthor>false</attributeAuthor><difficulty>0.0</difficulty><text><![CDATA[    ]]></text><answer><![CDATA[3]]></answer><display>vertical</display><fixed><![CDATA[    ]]></fixed><choices><choice><![CDATA[1]]></choice><choice><![CDATA[2]]></choice><choice><![CDATA[3]]></choice><choice><![CDATA[4]]></choice></choices><width>0.0</width></part>'
        self.assertEqual(module_to_string(q_part.generate_xml()), expected)
        
    def test_question(self):
        uid = '1111-2222-3333'
        name = 'Multiple Choice Opgave'
        q = ta_question(uid, name)
        self.assertEqual(q.get_name(), name)
        self.assertEqual(q.get_uid(), uid)
        
    # def test_question_xml(self):
    #     mode = "Multiple Choice"
    #     text = '    '
    #     answer = 3
    #     possible_answers = [1,2,3,4]
    #     q_part = ta_question_part(mode,text, answer, possible_answers , name='  responseNaN  ', editing='useHTML', num_attempts=1,numberOfAttemptsLeft=1, numberOfTryAnother=0, numberOfTryAnotherLeft=0, allowRepublish='false',attributeAuthor='false', difficulty='0.0',  display='vertical', fixed='    ',  width='0.0')
    #
    #     uid = '1111-2222-3333'
    #     name = 'Multiple Choice Opgave'
    #     q = ta_question(uid, name)
    #     q.append_part(q_part)
    #
    #     self.assertEqual(module_to_string(q.get_parts()[-1].generate_xml()), module_to_string(q_part.generate_xml()))
    #
    #     expected = b'<parts><part><mode>Multiple Choice</mode><name><![CDATA[  responseNaN  ]]></name><editing>useHTML</editing><numberOfAttempts>1</numberOfAttempts><numberOfAttemptsLeft>1</numberOfAttemptsLeft><numberOfTryAnother>0</numberOfTryAnother><numberOfTryAnotherLeft>0</numberOfTryAnotherLeft><allowRepublish>false</allowRepublish><attributeAuthor>false</attributeAuthor><difficulty>0.0</difficulty><text><![CDATA[    ]]></text><answer><![CDATA[3]]></answer><display>vertical</display><fixed><![CDATA[    ]]></fixed><choices><choice><![CDATA[1]]></choice><choice><![CDATA[2]]></choice><choice><![CDATA[3]]></choice><choice><![CDATA[4]]></choice></choices><width>0.0</width></part></parts>'
    #
    #     self.assertEqual(module_to_string( q.generate_xml_parts() ), expected  )
    #
    #     expected = b'<question><mode>Inline</mode><chainId><![CDATA[0]]></chainId><name><![CDATA[Multiple Choice Opgave]]></name><comment><![CDATA[]]></comment><editing>useHTML</editing><numberOfAttempts>1</numberOfAttempts><numberOfAttemptsLeft>1</numberOfAttemptsLeft><numberOfTryAnother>0</numberOfTryAnother><numberOfTryAnotherLeft>0</numberOfTryAnotherLeft><privacy>10</privacy><allowRepublish>false</allowRepublish><attributeAuthor>false</attributeAuthor><modifiedIn>13.0</modifiedIn><difficulty>0.0</difficulty><text><![CDATA[]]></text><width>0.0</width><weighting>1</weighting><numbering>alpha</numbering><parts><part><mode>Multiple Choice</mode><name><![CDATA[  responseNaN  ]]></name><editing>useHTML</editing><numberOfAttempts>1</numberOfAttempts><numberOfAttemptsLeft>1</numberOfAttemptsLeft><numberOfTryAnother>0</numberOfTryAnother><numberOfTryAnotherLeft>0</numberOfTryAnotherLeft><allowRepublish>false</allowRepublish><attributeAuthor>false</attributeAuthor><difficulty>0.0</difficulty><text><![CDATA[    ]]></text><answer><![CDATA[3]]></answer><display>vertical</display><fixed><![CDATA[    ]]></fixed><choices><choice><![CDATA[1]]></choice><choice><![CDATA[2]]></choice><choice><![CDATA[3]]></choice><choice><![CDATA[4]]></choice></choices><width>0.0</width></part></parts></question>'
    #
    #     self.assertEqual(module_to_string(q.generate_xml()), expected)
          
    def test_question_append(self):
        uid = '1111-2222-3333'
        name = 'Multiple Choice Opgave'
        q = ta_question(uid, name)
        
        mode = "Multiple Choice"
        text = '    '
        answer = 3
        possible_answers = [1,2,3,4]
        q_part = ta_question_part(mode,text, answer, possible_answers , name='  responseNaN  ', editing='useHTML', num_attempts=1,numberOfAttemptsLeft=1, numberOfTryAnother=0, numberOfTryAnotherLeft=0, allowRepublish='false',attributeAuthor='false', difficulty='0.0',  display='vertical', fixed='    ',  width='0.0')

        expected_q_part = b'<part><mode>Multiple Choice</mode><name><![CDATA[  responseNaN  ]]></name><editing>useHTML</editing><numberOfAttempts>1</numberOfAttempts><numberOfAttemptsLeft>1</numberOfAttemptsLeft><numberOfTryAnother>0</numberOfTryAnother><numberOfTryAnotherLeft>0</numberOfTryAnotherLeft><allowRepublish>false</allowRepublish><attributeAuthor>false</attributeAuthor><difficulty>0.0</difficulty><text><![CDATA[    ]]></text><answer><![CDATA[3]]></answer><display>vertical</display><fixed><![CDATA[    ]]></fixed><choices><choice><![CDATA[1]]></choice><choice><![CDATA[2]]></choice><choice><![CDATA[3]]></choice><choice><![CDATA[4]]></choice></choices><width>0.0</width></part>'
        
        q.append_part(q_part)
        
        parts = q.get_parts()
        
        self.assertEqual(module_to_string(parts[-1].generate_xml()),expected_q_part )
        self.assertEqual(len(parts), 1)
        
    def test_ta_meta(self):
        name = "my module"
        description = ""
        m = ta_meta(name, description)
        
        expected = b'<module><name><![CDATA[my module]]></name><description><![CDATA[]]></description><privacy>10</privacy><autoModule>false</autoModule><exportedFrom>f496fbff-6a44-46d8-a95c-82e23a24712e</exportedFrom></module>'
        
        self.assertEqual(module_to_string(m.generate_xml()), expected)
        
        
    
    
    
    def test_ta_module(self):
        name = "my module"
        description = ""
        meta = ta_meta(name, description)
        
        name = "My Name"
        author = ta_author(name)
    
        name = "TU Delft"
        school = ta_school(name)
        
        mod = ta_module(meta, author, school)
        self.assertEqual(mod.get_num_questions(), 0)
        
        uid = '1111-2222-3333'
        name = 'Multiple Choice Opgave'
        q = ta_question(uid, name)
        
        mode = "Multiple Choice"
        text = '    '
        answer = 3
        possible_answers = [1,2,3,4]
        q_part = ta_question_part(mode,text, answer, possible_answers , name='  responseNaN  ', editing='useHTML', num_attempts=1,numberOfAttemptsLeft=1, numberOfTryAnother=0, numberOfTryAnotherLeft=0, allowRepublish='false',attributeAuthor='false', difficulty='0.0',  display='vertical', fixed='    ',  width='0.0')
        
        q.append_part(q_part)
        
        mod.append_question(q)
        
        self.assertEqual(mod.get_num_questions(), 1)
        
        q_xml = module_to_string((mod.get_questions()[-1]).generate_xml())
        
        expected = b'<question><mode>Inline</mode><chainId><![CDATA[0]]></chainId><name><![CDATA[Multiple Choice Opgave]]></name><comment><![CDATA[]]></comment><editing>useHTML</editing><numberOfAttempts>1</numberOfAttempts><numberOfAttemptsLeft>1</numberOfAttemptsLeft><numberOfTryAnother>0</numberOfTryAnother><numberOfTryAnotherLeft>0</numberOfTryAnotherLeft><privacy>10</privacy><allowRepublish>false</allowRepublish><attributeAuthor>false</attributeAuthor><modifiedIn>13.0</modifiedIn><difficulty>0.0</difficulty><text><![CDATA[]]></text><width>0.0</width><weighting>1</weighting><numbering>alpha</numbering><parts><part><mode>Multiple Choice</mode><name><![CDATA[  responseNaN  ]]></name><editing>useHTML</editing><numberOfAttempts>1</numberOfAttempts><numberOfAttemptsLeft>1</numberOfAttemptsLeft><numberOfTryAnother>0</numberOfTryAnother><numberOfTryAnotherLeft>0</numberOfTryAnotherLeft><allowRepublish>false</allowRepublish><attributeAuthor>false</attributeAuthor><difficulty>0.0</difficulty><text><![CDATA[    ]]></text><answer><![CDATA[3]]></answer><display>vertical</display><fixed><![CDATA[    ]]></fixed><choices><choice><![CDATA[1]]></choice><choice><![CDATA[2]]></choice><choice><![CDATA[3]]></choice><choice><![CDATA[4]]></choice></choices><width>0.0</width></part></parts></question>'
        
        self.assertEqual(q_xml, expected)
        
        expected_q = b'<courseModule><module><name><![CDATA[my module]]></name><description><![CDATA[]]></description><privacy>10</privacy><autoModule>false</autoModule><exportedFrom>f496fbff-6a44-46d8-a95c-82e23a24712e</exportedFrom></module><question><mode>Inline</mode><chainId><![CDATA[0]]></chainId><name><![CDATA[Multiple Choice Opgave]]></name><comment><![CDATA[]]></comment><editing>useHTML</editing><numberOfAttempts>1</numberOfAttempts><numberOfAttemptsLeft>1</numberOfAttemptsLeft><numberOfTryAnother>0</numberOfTryAnother><numberOfTryAnotherLeft>0</numberOfTryAnotherLeft><privacy>10</privacy><allowRepublish>false</allowRepublish><attributeAuthor>false</attributeAuthor><modifiedIn>13.0</modifiedIn><difficulty>0.0</difficulty><text><![CDATA[]]></text><width>0.0</width><weighting>1</weighting><numbering>alpha</numbering><parts><part><mode>Multiple Choice</mode><name><![CDATA[  responseNaN  ]]></name><editing>useHTML</editing><numberOfAttempts>1</numberOfAttempts><numberOfAttemptsLeft>1</numberOfAttemptsLeft><numberOfTryAnother>0</numberOfTryAnother><numberOfTryAnotherLeft>0</numberOfTryAnotherLeft><allowRepublish>false</allowRepublish><attributeAuthor>false</attributeAuthor><difficulty>0.0</difficulty><text><![CDATA[    ]]></text><answer><![CDATA[3]]></answer><display>vertical</display><fixed><![CDATA[    ]]></fixed><choices><choice><![CDATA[1]]></choice><choice><![CDATA[2]]></choice><choice><![CDATA[3]]></choice><choice><![CDATA[4]]></choice></choices><width>0.0</width></part></parts></question><author defaultSchool="4d371c02-0aef-47ff-a091-c676055f80fc" instanceUid="899d2f9c-1ea7-4c10-9e5b-805f88434028" uid="02037092-3d70-4051-8447-b7cd2beef048"><displayName><![CDATA[My Name]]></displayName></author><school uid="4d371c02-0aef-47ff-a091-c676055f80fc"><name><![CDATA[TU Delft]]></name></school></courseModule>'
        
        self.assertEqual(module_to_string(mod.generate_xml()), expected_q)
    
if __name__ == '__main__':
    unittest.main()