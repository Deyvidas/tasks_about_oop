import datetime
import time


class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None

    def __str__(self):
        quest_info = f'Цель квеста {self.name} - {self.goal}'
        if self.description[-1] != '.':
            quest_info += '.'
        situations = (' Квест выполняется.', ' Квест завершён.')
        if self.start_time and not self.end_time:
            return quest_info + situations[0]
        if self.start_time and self.end_time:
            return quest_info + situations[1]
        return quest_info

    def accept_quest(self):
        if not self.end_time:
            self.start_time = datetime.datetime.now()
            return f'Начало квеста "{self.name}" положено.'
        return 'С этим испытанием вы уже справились.'

    def pass_quest(self):
        if self.start_time:
            self.end_time = datetime.datetime.now()
            completion_time = self.end_time - self.start_time
            return (
                f'Квест "{self.name}" окончен. '
                f'Время выполнения квеста {completion_time}')
        return 'Нельзя завершить то, что не имеет начала!'


quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = (
    '\nВ древнем лесу Кодоборье растёт ягода "пиксельника".\n'
    'Она нужна для приготовления целебных снадобий.\n'
    'Соберите 12 ягод пиксельники.')

new_quest = Quest(quest_name, quest_description, quest_goal)

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())
print(new_quest)
