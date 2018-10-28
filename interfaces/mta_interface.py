from TAClasses.ta_school import *
from TAClasses.ta_author import *
from TAClasses.ta_question_part import *
from TAClasses.ta_question import *
from TAClasses.ta_meta import *
from TAClasses.ta_module import *

import uuid

def ta_question_generation(question):
    
    if question.get_shuffle():
        qp_mode = ""
    else:
        qp_mode = "Non Permuting "
        
    if question.get_type() != "MS":
        qp_mode = qp_mode + "Multiple Selection"
    else:
        qp_mode = qp_mode + "Multiple Choice"
        
    qp_text = '    '
    ta_q_part = ta_question_part(mode=qp_mode, text=qp_text, answer=question.get_correct_ans(), possible_answers=question.get_choices())
    
    uid = str(uuid.uuid4())
    ta_q = ta_question(uid=uid, name=question.get_name(), text=question.get_text(), comment=question.get_comment(), part=ta_q_part)

    return ta_q
