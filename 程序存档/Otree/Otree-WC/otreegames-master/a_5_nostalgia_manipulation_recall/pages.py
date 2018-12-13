from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Manipulation(Page):
    form_model = 'player'
    form_fields = ['recall_keyword_1', 'recall_keyword_2', 'recall_keyword_3', 'recall_keyword_4', 'recall_statement']

    def is_displayed(self):
        return self.player.id_in_group == 1

    pass


class Control(Page):
    form_model = 'player'
    form_fields = ['recall_keyword_1', 'recall_keyword_2', 'recall_keyword_3', 'recall_keyword_4', 'recall_statement']

    def is_displayed(self):
        return self.player.id_in_group == 2

    pass


class Check(Page):
    form_model = 'player'
    form_fields = ['recall_manipulation_check_1', 'recall_manipulation_check_2', 'recall_manipulation_check_3']
    pass


page_sequence = [
    Manipulation,
    Control,
    Check
]
