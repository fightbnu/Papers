from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Self_Concept(Page):
    form_model = 'player'
    form_fields = [
                    "int1", "int2", "int3", "int4", "int5", "int6", "int7", "int8", "int9", "int10",
                    "ind1", "ind2", "ind3", "ind4", "ind5", "ind6", "ind7", "ind8",
                   ]
    random.shuffle(form_fields)
    pass


page_sequence = [
    Self_Concept,
]
