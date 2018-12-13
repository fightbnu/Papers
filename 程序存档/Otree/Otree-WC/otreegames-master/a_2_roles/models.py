from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Cong Wei'

doc = """
This study was designed for testify the positive correlation between nostalgia and corruption.
This part gives out the roles of the corruption game.
"""


class Constants(BaseConstants):
    name_in_url = 'a_2_roles'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
