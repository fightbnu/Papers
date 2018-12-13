from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.05,
    'participation_fee': 12.5,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'games',
        'display_name': "怀旧与腐败决策",
        'num_demo_participants': 10,
        'app_sequence': [
                            'a_1_introduction', 'a_2_roles', 'a_3_0_role_practice','a_3_1_practice_report', 'a_4_understanding_check',
                            'a_0_rest', 'a_5_nostalgia_manipulation_recall', 'a_6_positive_affect',
                            'a_7_1_social_connection', 'a_8_0_game_start_info',
                            'a_8_corruption_game_10', 'a_9_morality', 'a_10_demographic', 'a_11_end_report'
                        ],
    },
    {
        'name': 'introduction',
        'display_name': "introduction",
        'num_demo_participants': 10,
        'app_sequence': ['a_1_introduction'],
    },
    {
        'name': 'roles',
        'display_name': "roles",
        'num_demo_participants': 10,
        'app_sequence': ['a_2_roles'],
    },
    {
        'name': 'roles_practice_0',
        'display_name': "roles_practice_0",
        'num_demo_participants': 10,
        'app_sequence': ['a_3_0_role_practice'],
    },
    {
        'name': 'understanding_check',
        'display_name': "understanding_check",
        'num_demo_participants': 10,
        'app_sequence': ['a_4_understanding_check'],
    },
    {
        'name': 'rest',
        'display_name': "rest",
        'num_demo_participants': 10,
        'app_sequence': ['a_0_rest'],
    },
    {
        'name': 'nostalgia_manipulation_recall',
        'display_name': "nostalgia_manipulation_recall",
        'num_demo_participants': 10,
        'app_sequence': ['a_5_nostalgia_manipulation_recall'],
    },
    {
        'name': 'positive_affect',
        'display_name': "positive_affect",
        'num_demo_participants': 10,
        'app_sequence': ['a_6_positive_affect'],
    },
    {
        'name': 'social_connection',
        'display_name': "social_connection",
        'num_demo_participants': 10,
        'app_sequence': ['a_7_1_social_connection'],
    },
    {
        'name': 'self_concept',
        'display_name': "self_concept",
        'num_demo_participants': 10,
        'app_sequence': ['a_7_2_self_concept'],
    },
    {
        'name': 'role_assignment',
        'display_name': "role_assignment",
        'num_demo_participants': 10,
        'app_sequence': ['a_8_0_game_start_info'],
    },
    {
        'name': 'A_bribery_game',
        'display_name': "A_bribery_game",
        'num_demo_participants': 10,
        'app_sequence': ['a_8_corruption_game_10'],
    },
    {
        'name': 'moral_perception',
        'display_name': "moral_perception",
        'num_demo_participants': 10,
        'app_sequence': ['a_9_morality'],
    },
    {
        'name': 'demographic',
        'display_name': "demographic",
        'num_demo_participants': 10,
        'app_sequence': ['a_10_demographic'],
    },
    {
        'name': 'end_report',
        'display_name': "end_report",
        'num_demo_participants': 10,
        'app_sequence': ['a_11_end_report'],
    },
    {
        'name': 'practice_report',
        'display_name': "practice_report",
        'num_demo_participants': 10,
        'app_sequence': ['a_3_1_practice_report'],
    },
]
# see the end of this file for the inactive session configs


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'zh_hans'
POINTS_CUSTOM_NAME = '代币'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CNY'
USE_POINTS = True

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """
Here are various games implemented with
oTree. These games are open
source, and you can modify them as you wish.
"""

# don't share this with anybody.
SECRET_KEY = 'un36cwg+k(b5b+osh3_%yz)=eo$a4kjnb$!7+m952)_5^^5)vg'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# inactive session configs
### {
###     'name': 'trust',
###     'display_name': "Trust Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust', 'payment_info'],
### },
### {
###     'name': 'prisoner',
###     'display_name': "Prisoner's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['prisoner', 'payment_info'],
### },
### {
###     'name': 'ultimatum',
###     'display_name': "Ultimatum (randomized: strategy vs. direct response)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
### },
### {
###     'name': 'ultimatum_strategy',
###     'display_name': "Ultimatum (strategy method treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': True,
### },
### {
###     'name': 'ultimatum_non_strategy',
###     'display_name': "Ultimatum (direct response treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': False,
### },
### {
###     'name': 'vickrey_auction',
###     'display_name': "Vickrey Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['vickrey_auction', 'payment_info'],
### },
### {
###     'name': 'volunteer_dilemma',
###     'display_name': "Volunteer's Dilemma",
###     'num_demo_participants': 3,
###     'app_sequence': ['volunteer_dilemma', 'payment_info'],
### },
### {
###     'name': 'cournot',
###     'display_name': "Cournot Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'cournot', 'payment_info'
###     ],
### },
### {
###     'name': 'principal_agent',
###     'display_name': "Principal Agent",
###     'num_demo_participants': 2,
###     'app_sequence': ['principal_agent', 'payment_info'],
### },
### {
###     'name': 'dictator',
###     'display_name': "Dictator Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['dictator', 'payment_info'],
### },
### {
###     'name': 'matching_pennies',
###     'display_name': "Matching Pennies",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'matching_pennies',
###     ],
### },
### {
###     'name': 'traveler_dilemma',
###     'display_name': "Traveler's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['traveler_dilemma', 'payment_info'],
### },
### {
###     'name': 'bargaining',
###     'display_name': "Bargaining Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['bargaining', 'payment_info'],
### },
### {
###     'name': 'common_value_auction',
###     'display_name': "Common Value Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['common_value_auction', 'payment_info'],
### },
### {
###     'name': 'bertrand',
###     'display_name': "Bertrand Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'bertrand', 'payment_info'
###     ],
### },
### {
###     'name': 'real_effort',
###     'display_name': "Real-effort transcription task",
###     'num_demo_participants': 1,
###     'app_sequence': [
###         'real_effort',
###     ],
### },
### {
###     'name': 'lemon_market',
###     'display_name': "Lemon Market Game",
###     'num_demo_participants': 3,
###     'app_sequence': [
###         'lemon_market', 'payment_info'
###     ],
### },
### {
###     'name': 'public_goods_simple',
###     'display_name': "Public Goods (simple version from tutorial)",
###     'num_demo_participants': 3,
###     'app_sequence': ['public_goods_simple', 'payment_info'],
### },
### {
###     'name': 'trust_simple',
###     'display_name': "Trust Game (simple version from tutorial)",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust_simple'],
### },
# {
#     'name': 'guess_two_thirds',
#     'display_name': "Guess 2/3 of the Average",
#     'num_demo_participants': 3,
#     'app_sequence': ['guess_two_thirds', 'payment_info'],
# },
# {
#     'name': 'survey',
#     'num_demo_participants': 1,
#     'app_sequence': ['survey', 'payment_info'],
# },
# {
#     'name': 'quiz',
#     'num_demo_participants': 1,
#     'app_sequence': ['quiz'],
# },
