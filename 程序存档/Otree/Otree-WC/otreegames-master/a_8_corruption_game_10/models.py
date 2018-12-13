from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Your name here'

doc = """
This is the main bribery game.
"""


class Constants(BaseConstants):
    name_in_url = 'main'
    players_per_group = None
    num_rounds = 10


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            random_num = random.randint(14, 18)
            player.sentAccountA = random.choice([random_num, 0])
            if player.sentAccountA == 0:
                player.sentAccountB = random_num
            else:
                player.sentAccountB = 0
        return
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    offerAcceptedA = models.BooleanField(blank=True)
    offerAcceptedB = models.BooleanField(blank=True)
    sentAccountA = models.IntegerField()
    sentAccountB = models.IntegerField()
    roundWinner = models.StringField()
    playerAGive = models.IntegerField()
    playerBGive = models.IntegerField()
    playerAGain = models.IntegerField()
    playerBGain = models.IntegerField()
    selfGain = models.IntegerField()
    All_A = models.IntegerField()
    All_B = models.IntegerField()

    pass
