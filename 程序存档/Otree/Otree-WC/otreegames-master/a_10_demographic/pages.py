from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Demographic(Page):
    form_model = "player"
    form_fields = ['age', 'gender', 'ethnic', 'career', 'careerTime']
    pass


page_sequence = [
    Demographic,
]
