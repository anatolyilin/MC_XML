from lxml import etree
import uuid

def convert_to_cdata(data):
    return etree.CDATA(str(data))


def generate_block(elements_xml, elements_content, parent_element):
    for index_counter, elements_type in enumerate(elements_xml):
        if elements_type == 'choices':
            parent_element.append(generate_choices(elements_content[index_counter]))
            continue
        element = etree.Element(elements_type)
        if isinstance(elements_content[index_counter], etree.CDATA):
            element.text = elements_content[index_counter]
        else:
            element.text = str(elements_content[index_counter])
        parent_element.append(element)
    return parent_element


def generate_meta(name, description, privacy='10', autoModule='false',
                  exportedFrom='f496fbff-6a44-46d8-a95c-82e23a24712e'):
    module = etree.Element('module')
    entries_meta = [name, description, privacy, autoModule, uuid.uuid4(), exportedFrom]
    elements_meta = ['name', 'description', 'privacy', 'autoModule', 'uid', 'exportedFrom']
    module = generate_block(elements_meta, entries_meta, module)
    return module


def generate_choices(choice_elements):
    choices = etree.Element('choices')
    for choice in choice_elements:
        element = etree.Element('choice')
        element.text = etree.CDATA(str(choice))
        choices.append(element)
    return choices


def generate_part(mode, text, answer, possible_answers, name='  responseNaN  ', editing='useHTML', num_attempts=1,
                  numberOfAttemptsLeft=1, numberOfTryAnother=0, numberOfTryAnotherLeft=0, allowRepublish='false',
                  attributeAuthor='false', difficulty='0.0', display='vertical', fixed='    ', width='0.0'):
    nameCDATA = etree.CDATA(str(name))
    textCDATA = etree.CDATA(str(text))
    answerCDATA = etree.CDATA(str(answer))
    fixedCDATA = etree.CDATA(str(fixed))

    entries_part = [mode, nameCDATA, editing, num_attempts, numberOfAttemptsLeft, numberOfTryAnother,
                    numberOfTryAnotherLeft, allowRepublish, attributeAuthor, difficulty, textCDATA, answerCDATA,
                    display, fixedCDATA, possible_answers, width]

    entries_elements = ['mode', 'name', 'editing', 'numberOfAttempts', 'numberOfAttemptsLeft', 'numberOfTryAnother',
                        'numberOfTryAnotherLeft', 'allowRepublish', 'attributeAuthor', 'difficulty', 'text', 'answer',
                        'display', 'fixed', 'choices', 'width']

    part = etree.Element('part')
    part = generate_block(entries_elements, entries_part, part)
    return part


def generate_course_module():
    return etree.Element('courseModule')


def generate_school(school_uid, name):
    school = etree.Element('school', uid=school_uid)
    name_element = etree.Element('name')
    name_element.text = etree.CDATA(str(name))
    school.append(name_element)
    return school


def generate_author(author_uid, instance_uid, default_school, name):
    author = etree.Element('author', uid=author_uid, instanceUid=instance_uid, defaultSchool=default_school)
    name_element = etree.Element('displayName')
    name_element.text = etree.CDATA(str(name))
    author.append(name_element)
    return author


def generate_question(uid_code, question_name, comment_feedback, text, mode="Inline", cmAttributed="true",
                      cmWeight="0.0", modifiedBy="02037092-3d70-4051-8447-b7cd2beef048",
                      school="4d371c02-0aef-47ff-a091-c676055f80fc", chainId=0, editing='useHTML', num_attempts=1,
                      numberOfAttemptsLeft=1, numberOfTryAnother=0, numberOfTryAnotherLeft=0, privacy=10,
                      modifiedIn=13.0, allowRepublish='false', attributeAuthor='false', difficulty='0.0', width=0.0,
                      weighting=1, numbering='alpha'):
    chainIdCDATA = etree.CDATA(str(chainId))
    nameCDATA = etree.CDATA(str(question_name))
    commentCDATA = etree.CDATA(str(comment_feedback))
    textCDATA = etree.CDATA(str(text))

    question_element_entries = [mode, chainIdCDATA, nameCDATA, commentCDATA, editing, num_attempts,
                                numberOfAttemptsLeft, numberOfTryAnother, numberOfTryAnotherLeft, privacy,
                                allowRepublish, attributeAuthor, modifiedIn, difficulty, textCDATA, width, weighting,
                                numbering]

    question_elements = ['mode', 'chainId', 'name', 'comment', 'editing', 'numberOfAttempts', 'numberOfAttemptsLeft',
                         'numberOfTryAnother', 'numberOfTryAnotherLeft', 'privacy', 'allowRepublish', 'attributeAuthor',
                         'modifiedIn', 'difficulty', 'text', 'width', 'weighting', 'numbering']

    question = etree.Element('question', uid=uid_code, cmAttributed=cmAttributed, cmWeight=cmWeight,
                             modifiedBy=modifiedBy, school=school)

    question = generate_block(question_elements, question_element_entries, question)
    return question


def module_to_string(element):
    return etree.tostring(element)


def module_print(element):
    print(etree.tostring(element, pretty_print=True))