from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Cong Wei'

doc = """
This study was designed for testify the positive correlation between nostalgia and corruption.
This part is designed for measuring participants' sense of moral.
There are seven items. The items should be randomly assigned.
"""


class Constants(BaseConstants):
    name_in_url = 'moral'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def set_model_field(label):
    return models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label=label
    )


moral_items = [
    '我在游戏中的选择会损害其他玩家的利益。',
    '我在游戏中的选择是一种腐败行为。',
    '我在游戏中的选择对其他玩家不太公平。',
    '我在游戏中的选择是不公正的。',
    '我在游戏中的选择是不道德的。',
    '我在游戏中的选择可能不会被我的家庭所接受。',
    '我在游戏中的选择可能不会被我们的文化所接受。',
]


class Player(BasePlayer):
    moral_1 = set_model_field(moral_items[0])
    moral_2 = set_model_field(moral_items[1])
    moral_3 = set_model_field(moral_items[2])
    moral_4 = set_model_field(moral_items[3])
    moral_5 = set_model_field(moral_items[4])
    moral_6 = set_model_field(moral_items[5])
    moral_7 = set_model_field(moral_items[6])
    pass
