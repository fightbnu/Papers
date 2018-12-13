from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Cong Wei'

doc = """
This study was designed for testify the positive correlation between nostalgia and corruption.
This part is designed to collect demographic information of the participants.
The survey contain five items: Age, Gender, Ethnic, Career, CareerAge.
This survey should appear at the end of the game.
"""


class Constants(BaseConstants):
    name_in_url = 'demographic'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(
        label="您的年龄",
        max=100, min=16,
    )
    gender = models.StringField(
        choices=['男', '女'],
        widget=widgets.RadioSelect,
        label="您的性别",
    )
    ethnic = models.StringField(
        label="您的民族",
    )
    career = models.StringField(
        label="您的职业",
    )
    careerTime = models.IntegerField(
        label="如果您是在职人员，截止目前，您参加工作的年限是：",
        max=60, min=0,
        blank="true"
    )

    pass