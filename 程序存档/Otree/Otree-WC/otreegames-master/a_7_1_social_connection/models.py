from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Cong Wei'

doc = """
This study was designed for testify the positive correlation between nostalgia and corruption.
This part is designed for social connection measurement.
"""


class Constants(BaseConstants):
    name_in_url = 'social_connection'
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


social_connection_items = [
    "回忆这件事让我感到自己是被关爱的。",
    "回忆这件事让我感到我和我所喜欢的人之间是有联系的。",
    "回忆这件事让我感到一种被人保护的安全感。",
    "回忆这件事让我觉得自己与他人的关系比较亲近。",
    "回忆这件事让我觉得自己与许多人都是有联系的。",
    "回忆这件事让我觉得自己被他人所接纳。",
    "回忆这件事让我觉得很温暖。",
    "回忆这件事让我觉得自己与周围的世界是有联系的。",
    "回忆这件事让我觉得自己可以理解他人，能融入到集体中。",
    "回忆这件事让我觉得自己与别人比较亲近。",
    "回忆这件事让我觉得自己能够与同伴交往。",
    "回忆这件事让我觉得自己与他人之间是有关联的。",
    "回忆这件事让我觉得自己能够与其他人建立联系。",
    "回忆这件事让我觉得人们是友好且平易近人的。",
    "回忆这件事让我觉得我在熟人身边有归属感。",
    "回忆这件事让我觉得我身边的人能理解我。",
    "回忆这件事让我觉得我可以良好地适应新环境。",
    "回忆这件事让我觉得我与同伴之间相处和睦。",
    "回忆这件事让我觉得朋友就像家人一样亲切。",
    "回忆这件事让我觉得我自己主动卷入到我身边人的生活。",
    "回忆这件事让我觉得我与朋友之间有真挚的情谊。",
    "回忆这件事让我觉得我与周围的世界很合拍。",
    "回忆这件事让我觉得我在陌生人面前很自如。",
]


class Player(BasePlayer):
    social_connection_1 = set_model_field(social_connection_items[0])
    social_connection_2 = set_model_field(social_connection_items[1])
    social_connection_3 = set_model_field(social_connection_items[2])
    social_connection_4 = set_model_field(social_connection_items[3])
    social_connection_5 = set_model_field(social_connection_items[4])
    social_connection_6 = set_model_field(social_connection_items[5])
    social_connection_7 = set_model_field(social_connection_items[6])
    social_connection_8 = set_model_field(social_connection_items[7])
    social_connection_9 = set_model_field(social_connection_items[8])
    social_connection_10 = set_model_field(social_connection_items[9])
    social_connection_11 = set_model_field(social_connection_items[10])
    social_connection_12 = set_model_field(social_connection_items[11])
    social_connection_13 = set_model_field(social_connection_items[12])
    social_connection_14 = set_model_field(social_connection_items[13])
    social_connection_15 = set_model_field(social_connection_items[14])
    social_connection_16 = set_model_field(social_connection_items[15])
    social_connection_17 = set_model_field(social_connection_items[16])
    social_connection_18 = set_model_field(social_connection_items[17])
    social_connection_19 = set_model_field(social_connection_items[18])
    social_connection_20 = set_model_field(social_connection_items[19])
    social_connection_21 = set_model_field(social_connection_items[20])
    social_connection_22 = set_model_field(social_connection_items[21])
    social_connection_23 = set_model_field(social_connection_items[22])
    pass
