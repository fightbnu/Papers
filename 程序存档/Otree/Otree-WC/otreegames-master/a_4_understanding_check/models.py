from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Cong Wei'

doc = """
This study was designed for testify the positive correlation between nostalgia and corruption.
This part would check whether the participants fully understand the roles of the corruption game.
"""


class Constants(BaseConstants):
    name_in_url = 'understanding_check'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    check_1 = models.IntegerField(
        max=50, min=50,
        label="玩家A获胜拿到50个代币的概率为",
    )
    check_2 = models.IntegerField(
        max=50, min=50,
        label="玩家B获胜拿到50个代币的概率为"
    )
    check_3 = models.IntegerField(
        max=0, min=0,
        label="裁判C在本轮的收益为多少个代币"
    )
    check_4 = models.IntegerField(
        max=0, min=0,
        label="裁判C在本轮被惩罚的概率为"
    )

    check_5 = models.IntegerField(
        max=50, min=50,
        label="玩家A获胜拿到50个代币的概率为",
    )
    check_6 = models.IntegerField(
        max=50, min=50,
        label="玩家B获胜拿到50个代币的概率为"
    )
    check_7 = models.IntegerField(
        max=0, min=0,
        label="裁判C在本轮的收益为多少个代币"
    )
    check_8 = models.IntegerField(
        max=0, min=0,
        label="裁判C在本轮被惩罚的概率为"
    )

    check_9 = models.IntegerField(
        max=90, min=90,
        label="玩家A获胜拿到50个代币的概率为",
    )
    check_10 = models.IntegerField(
        max=10, min=10,
        label="玩家B获胜拿到50个代币的概率为"
    )
    check_11 = models.IntegerField(
        max=10, min=10,
        label="裁判C在本轮的收益为多少个代币"
    )
    check_12 = models.IntegerField(
        max=5, min=5,
        label="裁判C在本轮被惩罚的概率为"
    )
    check_13 = models.StringField(
        choices=[
            "A：裁判C前面轮次所有收益归零，并被罚10个代币，游戏继续",
            "B：裁判C前面轮次所有收益归零，并被罚30个代币，游戏继续",
            "C：裁判C前面轮次所有收益归零，并被罚10个代币，游戏终止",
            "D：裁判C前面轮次所有收益归零，并被罚30个代币，游戏终止"
        ],
        widget=widgets.RadioSelect
    )
    check_14 = models.StringField(
        choices=[
            "E: 玩家A将损失10个代币，游戏终止",
            "F: 玩家A将损失30个代币，游戏终止",
            "G: 玩家A将损失10个代币，游戏继续",
            "H: 玩家A将损失30个代币，游戏继续"
        ],
        widget=widgets.RadioSelect,
    )
    pass
