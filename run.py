import eel
from ViewClasses.question import *
from interfaces.XML_interface import *

from TAClasses.ta_module import *
from TAClasses.ta_meta import *
from TAClasses.ta_author import *
from TAClasses.ta_school import *

import shutil

eel.init('webpages')                     # Give folder containing web files

question_list = []
json_questions = []

@eel.expose
def getQuestionsCount():
    return len(question_list)

@eel.expose
def generateModule(data):
    print(data)

    name = data["module_titel"]
    meta = ta_meta(name=name, description="externally generated v1.0")

    school = ta_school(name="TU Delft")

    author = ta_author(displayName="PoC TA GUI")

    # provision for assignment
    assignment_name = data['assignment_titel']

    module = ta_module(meta=meta, author=author, school=school)
    for question in question_list:
        module.append_question(question.generate_ta_question())

    mod = module_to_string(module.generate_xml())

    file = open("/Users/user43671/Desktop/test45/manifest.xml","w")
    file.write(mod.decode('utf-8'))
    file.close()

    shutil.make_archive('/Users/user43671/Desktop/file', 'zip', '/Users/user43671/Desktop/test45/')

@eel.expose
def handleinput(ui_question):

    json_questions.append(ui_question)
    name = ui_question['question_name']
    text = ui_question['question_text']
    text = text + "<1>"
    shuffle = ui_question['shuffle']
    choices = ui_question['question_answers']
    comment = ui_question['question_feedback']
    dict_type = ui_question['type']

    if dict_type:
        type="MS"
    else:
        type="MC"

    correct_choices = ""
    dict_choices = ui_question['question_correct_answer']
    print(dict_choices)
    for element, counter in enumerate(dict_choices):
        if (element):
            correct_choices = correct_choices + "," + str(counter+1)
    correct_choices = correct_choices[1:]

    temp_question = mc_question(name=name, text=text, type=type, shuffle=shuffle, choices=choices, correct=correct_choices, comment=comment)

    question_list.append(temp_question)
    print(module_to_string(temp_question.generate_ta_question().generate_xml()))
    eel.all_json_questions(json_questions)

eel.start('UI.html', size=(1000, 760))