from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Cong Wei'

doc = """
This is for roles introduction.
"""


class Constants(BaseConstants):
    name_in_url = 'practice_0'
    players_per_group = None
    num_rounds = 4


# note: 一个subsession 相当于一次“给-接受-判断”的流程
class Subsession(BaseSubsession):
    def creating_session(self):     # judge A or B
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
    sentAccountA = models.IntegerField()    #
    sentAccountB = models.IntegerField()    #
    roundWinner = models.StringField()      #
    playerAGive = models.IntegerField() # A给
    playerBGive = models.IntegerField() # B给
    playerAGain = models.IntegerField() # A收
    playerBGain = models.IntegerField() # B收
    selfGain = models.IntegerField()    # 裁判收
    All_A = models.IntegerField()   #A总
    All_B = models.IntegerField()   #B总

    pass
# function：定义玩家属性；
# function: 定义sentAcountA,B：为什么在subsession里边定义