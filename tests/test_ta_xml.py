from interfaces.XML_interface import *
import unittest

class TestXMLmethods(unittest.TestCase):

    def test_meta(self):
        mod = generate_meta('titel', 'beschrijving')
        expected = b'<module><name>titel</name><description>beschrijving</description><privacy>10</privacy><autoModule>false</autoModule><exportedFrom>f496fbff-6a44-46d8-a95c-82e23a24712e</exportedFrom></module>'
        self.assertEqual(module_to_string(mod), expected )

    def test_choices(self):
        choices = ['<p>Optie 1</p>', '<p>Optie 2</p>', '<p>Optie 3</p>', '<p>Optie 4</p>']
        mod = generate_choices(choices)
        expected = b'<choices><choice><![CDATA[<p>Optie 1</p>]]></choice><choice><![CDATA[<p>Optie 2</p>]]></choice><choice><![CDATA[<p>Optie 3</p>]]></choice><choice><![CDATA[<p>Optie 4</p>]]></choice></choices>'
        self.assertEqual(module_to_string(mod), expected )
        
    def test_part(self):
        a = generate_part(mode='mode',text='leuke tekstje', answer=3, possible_answers=['a','b','c'] )
        expected = b'<part><mode>mode</mode><name><![CDATA[  responseNaN  ]]></name><editing>useHTML</editing><numberOfAttempts>1</numberOfAttempts><numberOfAttemptsLeft>1</numberOfAttemptsLeft><numberOfTryAnother>0</numberOfTryAnother><numberOfTryAnotherLeft>0</numberOfTryAnotherLeft><allowRepublish>false</allowRepublish><attributeAuthor>false</attributeAuthor><difficulty>0.0</difficulty><text><![CDATA[leuke tekstje]]></text><answer><![CDATA[3]]></answer><display>vertical</display><fixed><![CDATA[    ]]></fixed><choices><choice><![CDATA[a]]></choice><choice><![CDATA[b]]></choice><choice><![CDATA[c]]></choice></choices><width>0.0</width></part>'
        self.assertEqual(module_to_string(a), expected )
        
    def test_parts(self):
        a = generate_parts(mode='mode',text='leuke tekstje', answer=3, possible_answers=['a','b','c'] )
        expected = b'<parts><part><mode>mode</mode><name><![CDATA[  responseNaN  ]]></name><editing>useHTML</editing><numberOfAttempts>1</numberOfAttempts><numberOfAttemptsLeft>1</numberOfAttemptsLeft><numberOfTryAnother>0</numberOfTryAnother><numberOfTryAnotherLeft>0</numberOfTryAnotherLeft><allowRepublish>false</allowRepublish><attributeAuthor>false</attributeAuthor><difficulty>0.0</difficulty><text><![CDATA[leuke tekstje]]></text><answer><![CDATA[3]]></answer><display>vertical</display><fixed><![CDATA[    ]]></fixed><choices><choice><![CDATA[a]]></choice><choice><![CDATA[b]]></choice><choice><![CDATA[c]]></choice></choices><width>0.0</width></part></parts>'
        self.assertEqual(module_to_string(a), expected )
        
   
if __name__ == '__main__':
    unittest.main()