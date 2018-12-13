from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class AssignPage(Page):
    def vars_for_template(self):
        return{
            'current_round': self.round_number,
        }

    timeout_seconds = 3
    timeout_submission = {}
    pass


class PlayGround(Page):
    def vars_for_template(self):
        return{
            'current_round': self.round_number,
            'totoleMoney': sum([p.payoff for p in self.player.in_all_rounds()]) + 250,
            'sentAll': self.player.sentAccountA + self.player.sentAccountB,
            'AfterReceive': sum([p.payoff for p in self.player.in_all_rounds()]) + 250 + self.player.sentAccountA + self.player.sentAccountB,
            "punish": (self.player.sentAccountA + self.player.sentAccountB) * 3,
            "AfterPunish": 250 - (self.player.sentAccountA + self.player.sentAccountB) * 3,
        }

    form_model = 'player'
    form_fields = ['offerAcceptedA', 'offerAcceptedB', 'roundWinner',
                   'playerAGive', 'playerBGive',
                   'playerAGain', 'playerBGain',
                   'All_A', 'All_B',
                   'selfGain',
                   ]


class CheckPage(Page):
    def vars_for_template(self):
        return{
            'current_round': self.round_number,
            "punish": (self.player.sentAccountA + self.player.sentAccountB) * 3,
            "AfterPunish": 250 - (self.player.sentAccountA + self.player.sentAccountB) * 3,
        }
    timeout_seconds = 5
    timeout_submission = {}

    def before_next_page(self):
        self.player.payoff = c(self.player.selfGain)
        self.participant.vars['main_fee'] = sum([p.payoff for p in self.player.in_all_rounds()])
        print(self.player.payoff)
        print(self.participant.vars['main_fee'])
    pass



class ResultPage(Page):
    def vars_for_template(self):
        return{
            'current_round': self.round_number,
            'totoleMoney': sum([p.payoff for p in self.player.in_all_rounds()]) + 250,
        }
    pass

page_sequence = [
    AssignPage,
    PlayGround,
    CheckPage,
    ResultPage,
]
