from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

lists = [
            'Affect_1', 'Affect_2', 'Affect_3R', 'Affect_4R',
        ]

list_01 = lists[0:4]


class PAffect(Page):
    form_model = 'player'
    # random.shuffle(lists)
    form_fields = lists
    pass


page_sequence = [
    PAffect,
]
