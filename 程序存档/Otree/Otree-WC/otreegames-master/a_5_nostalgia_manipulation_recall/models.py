from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Cong Wei'

doc = """
This study was designed for testify the positive correlation between nostalgia and corruption.
This part is designed for Nostalgia manipulation.
There are two groups, one group in the experimental condition and the other group in the control condition.
First, Each participant complete a memory task according to the group condition.
Then, complete the manipulation check items.
"""


class Constants(BaseConstants):
    name_in_url = 'recall'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'manipulation'
        if self.id_in_group == 2:
            return 'control'

    recall_keyword_1 = models.StringField()
    recall_keyword_2 = models.StringField()
    recall_keyword_3 = models.StringField()
    recall_keyword_4 = models.StringField()
    recall_statement = models.LongStringField()

    recall_manipulation_check_1 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="此时此刻，我感到很怀旧。"
    )
    recall_manipulation_check_2 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="我回忆的这个事件很有怀旧感。"
    )
    recall_manipulation_check_3 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="回忆这个事件，此时此刻让我感到很怀旧。"
    )
    pass
