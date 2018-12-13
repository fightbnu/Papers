from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Cong Wei'

doc = """
This study was designed for testify the positive correlation between nostalgia and corruption.
This part is designed for self concept measurement.
"""


construal_lists = [
    "回忆这件事会让我觉得，我不会为了迎合大多数人而改变自己的观点。",
    "回忆这件事会让我觉得，当我所在的集体犯了错，我不会支持它。",
    "回忆这件事会让我觉得，当我与集体中其他成员意见相左时，我会提出异议。",
    "回忆这件事会让我觉得，无论和谁在一起，我的行为方式都是相同的。",
    "回忆这件事会让我觉得，在许多方面，我喜欢保持独特和与众不同。",
    "回忆这件事会让我觉得，当我被单独表扬或奖励的时候，我会感到心里很舒服。",
    "回忆这件事会让我觉得，在工作团队中发言对我来说不成问题。",
    "回忆这件事会让我觉得，我认为个人健康的价值高于一切。",

    "回忆这件事会让我觉得，我会牺牲自身利益来换取集体利益。",
    "回忆这件事会让我觉得，我会按照集体中其他成员喜欢的方式来行事。",
    "回忆这件事会让我觉得，即使在困难前面，我也会力挺我的集体。",
    "回忆这件事会让我觉得，保持集体的和谐很重要。",
    "回忆这件事会让我觉得，即使我对集体并不满意，但只要它需要我，我就会继续留在集体中。",
    "回忆这件事会让我觉得，即使我非常不赞同集体中其他成员的观点，我也会避免争执。",
    "回忆这件事会让我觉得，我尊重那些谦逊的人。",
    "回忆这件事会让我觉得，人际关系比个人成就更重要。",
    "回忆这件事会让我觉得，我的快乐源自于我身边人的快乐。",
    "回忆这件事会让我觉得，尊重集体的决定是一件很重要的事情。",
]


def set_model_field(label):
    return models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label=label
    )


class Constants(BaseConstants):
    name_in_url = 'self_concept'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ind1 = set_model_field(construal_lists[0])
    ind2 = set_model_field(construal_lists[1])
    ind3 = set_model_field(construal_lists[2])
    ind4 = set_model_field(construal_lists[3])
    ind5 = set_model_field(construal_lists[4])
    ind6 = set_model_field(construal_lists[5])
    ind7 = set_model_field(construal_lists[6])
    ind8 = set_model_field(construal_lists[7])

    int1 = set_model_field(construal_lists[8])
    int2 = set_model_field(construal_lists[9])
    int3 = set_model_field(construal_lists[10])
    int4 = set_model_field(construal_lists[11])
    int5 = set_model_field(construal_lists[12])
    int6 = set_model_field(construal_lists[13])
    int7 = set_model_field(construal_lists[14])
    int8 = set_model_field(construal_lists[15])
    int9 = set_model_field(construal_lists[16])
    int10 = set_model_field(construal_lists[17])
    pass
