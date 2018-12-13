from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class RolePart1(Page):
    pass


class RolePart21(Page):
    pass


class RolePart22(Page):
    pass


class RolePart3(Page):
    pass


class RolePart4(Page):
    pass

class RolePart5(Page):
    pass

class StartPage(Page):
    timeout_seconds = 3
    timeout_submission = {}
    pass

class RolePage(Page):
    pass

page_sequence = [
    RolePart1,
    RolePart21,
    RolePart22,
    RolePart3,
    RolePart4,
    RolePart5,
    StartPage,
    RolePage,
]
