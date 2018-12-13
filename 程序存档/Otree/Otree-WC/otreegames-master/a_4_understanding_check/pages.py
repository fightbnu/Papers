from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Check1(Page):
    form_model = "player"
    form_fields = ['check_1', 'check_2', 'check_3', 'check_4']
    pass


class Check2(Page):
    form_model = "player"
    form_fields = ['check_5', 'check_6', 'check_7', 'check_8']
    pass


class Check3(Page):
    form_model = "player"
    form_fields = ['check_9', 'check_10', 'check_11', 'check_12']
    pass


class Check4(Page):
    form_model = "player"
    form_fields = ['check_13', 'check_14']
    pass


page_sequence = [
    Check1,
    Check2,
    Check3,
    Check4,
]
