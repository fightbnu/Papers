from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Rest(Page):
    timeout_seconds = 120
    timeout_submission = {}
    pass


class Start(Page):
    pass


page_sequence = [
    Rest,
    Start
]
