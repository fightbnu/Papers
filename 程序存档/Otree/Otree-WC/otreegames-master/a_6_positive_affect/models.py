from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Cong Wei'

doc = """
This study was designed for testify the positive correlation between nostalgia and corruption.
This Part is designed for positive affect measurement. There are totally 4 items which should be randomly present.
"""

emotion_lists = [
    "快乐",
    "心情好",
    "不开心",
    "悲伤",
]


def set_moral_field(label):
    return models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label=label
    )


class Constants(BaseConstants):
    name_in_url = 'affect'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Affect_1 = set_moral_field(emotion_lists[0])
    Affect_2 = set_moral_field(emotion_lists[1])
    Affect_3R = set_moral_field(emotion_lists[2])
    Affect_4R = set_moral_field(emotion_lists[3])
    pass
