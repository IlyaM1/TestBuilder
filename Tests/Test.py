# class Test:
#     def __init__(self, name, theme, questions):
#         self.name = name
#         self.theme = theme
#         self.questions = questions

def create_new_test(name, theme, questions):
    return {'name': name, 'theme': theme, 'questions': questions}

def create_new_question(question, type, variants_of_answer, answer, balls):
    return {'question': question, 'type': type, 'variants_of_answer': variants_of_answer, 'answer': answer, 'balls': balls}
