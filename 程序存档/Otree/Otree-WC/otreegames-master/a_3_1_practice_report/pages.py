from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class End(Page):
    def vars_for_template(self):
        totlepoints = self.participant.vars['practice_fee'] + 250
        return{
            'totleGain': self.participant.vars['practice_fee'],
            'totlePoints': totlepoints,
            'totleMoney': totlepoints.to_real_world_currency(self.session)
            }

page_sequence = [
    End
]
