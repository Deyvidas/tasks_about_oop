class Human:
    answers = {
        'Марина, мне грустненько, что делать?': ('Держись, всё получится.'
                                                 ' Хочешь видео с котиками?'),
        'Ира, мне грустненько, что делать?': ('Отдохни и возвращайся с'
                                              ' вопросами по теории.'),
        'Евгений, что не так с моим проектом?': ('О, вопрос про проект,'
                                                 ' это я люблю.'),
        'Ира, как устроиться работать питонистом?': 'Сейчас расскажу.'
        }

    def __init__(self, name: str) -> None:
        self.name = name

    def answer_question(self, question: str) -> tuple[str, str]:
        question = question
        if self.name not in question:
            question = f'{self.name}, {question}'
        answer = 'Очень интересный вопрос! Не знаю.'
        return question, answer


class Student(Human):
    @staticmethod
    def ask_question(someone, question: str) -> None:
        question, answer = someone.answer_question(question)
        print(f'{question}\n{answer}\n')


class Mentor(Human):
    def answer_question(self, question: str) -> tuple[str, str]:
        question = f'{self.name}, {question}'
        answer = self.answers.get(question, None)
        if not answer:
            question, answer = super().answer_question(question)
        return question, answer


class CodeReviewer(Human):
    def answer_question(self, question: str) -> tuple[str, str]:
        question = f'{self.name}, {question}'
        answer = self.answers.get(question, None)
        if not answer:
            question, answer = super().answer_question(question)
        return question, answer


class Curator(Human):
    def answer_question(self, question: str) -> tuple[str, str]:
        question = f'{self.name}, {question}'
        answer = self.answers.get(question, None)
        if not answer:
            question, answer = super().answer_question(question)
        return question, answer


student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
