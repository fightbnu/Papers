from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class StartPage(Page):
    timeout_seconds = 3
    timeout_submission = {}
    pass


class RolePage(Page):
    pass


page_sequence = [
    StartPage,
    RolePage,
]
