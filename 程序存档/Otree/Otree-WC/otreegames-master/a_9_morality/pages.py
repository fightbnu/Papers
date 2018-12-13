from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class Moral(Page):
    form_model = 'player'
    form_fields = ['moral_1', 'moral_2', 'moral_3', 'moral_4', 'moral_5', 'moral_6', 'moral_7']
    random.shuffle(form_fields)
    pass


page_sequence = [
    Moral,
]
