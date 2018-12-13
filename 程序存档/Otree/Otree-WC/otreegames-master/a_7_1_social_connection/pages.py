from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class SocialConnection(Page):
    form_model = 'player'
    form_fields = [
                    'social_connection_1', 'social_connection_2', 'social_connection_3', 'social_connection_4',
                    'social_connection_5', 'social_connection_6', 'social_connection_7', 'social_connection_8',
                    'social_connection_9', 'social_connection_10', 'social_connection_11', 'social_connection_12',
                    'social_connection_13', 'social_connection_14', 'social_connection_15', 'social_connection_16',
                    'social_connection_17', 'social_connection_18', 'social_connection_19', 'social_connection_20',
                    'social_connection_21', 'social_connection_22', 'social_connection_23'
                    ]
    random.shuffle(form_fields)
    pass


page_sequence = [
    SocialConnection,
]
