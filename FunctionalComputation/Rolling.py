# {Shop Level: {Unit Cost : Prob Of Rolling Unit For Unit Cost In Range(1,6) } For Shop Level In Range(1,10)}
shop_unit_prob_dict = {

    1: {1: 100, 2: 0, 3: 0, 4: 0, 5: 0},
    2: {1: 100, 2: 0, 3: 0, 4: 0, 5: 0},
    3: {1: 75, 2: 25, 3: 0, 4: 0, 5: 0},
    4: {1: 55, 2: 30, 3: 15, 4: 0, 5: 0},
    5: {1: 45, 2: 33, 3: 20, 4: 2, 5: 0},
    6: {1: 25, 2: 40, 3: 30, 4: 5, 5: 0},
    7: {1: 19, 2: 30, 3: 35, 4: 15, 5: 1},
    8: {1: 16, 2: 20, 3: 35, 4: 25, 5: 4},
    9: {1: 9, 2: 15, 3: 30, 4: 30, 5: 16},

    # These Are Not Usually Avaailable But If We Want To Include latter Uncomments
    # 10: {1: 5, 2: 10, 3: 20, 4: 40, 5: 25},
    # 11: {1: 1, 2: 2, 3: 12, 4: 50, 5: 35},
}


# Working As Intended
def reccomend_shop_level(unit_cost):

    """
        Gives Details About The Rolling Probabilities For Units Of A Particular Cost.

    Returns:
        A Dictionary With String Keys And List Values Such That:
            {Some Condition As A String: List Of All Shop Levels That Satisfy This Condition}

    """

    def average_prob():

        # Probablities Of Getting A Unit Of That Cost At All Shop Levels
        unit_probs_list = [shop_unit_prob_dict[shop_level][unit_cost] for shop_level in shop_unit_prob_dict]

        if 0 in unit_probs_list:
            unit_probs_list.remove(0)   # Don't Want Zeroes To Impact The Average

        average = sum(unit_probs_list)/len(unit_probs_list)

        return average

    def highest_prob():

        # Saves Resources If Leading Probs Have A Value Of 0
        highest_val = 0

        for shop_level in shop_unit_prob_dict:

            # Probability Of Rolling Unit With That Cost
            unit_prob = shop_unit_prob_dict[shop_level][unit_cost]

            if unit_prob > highest_val:
                highest_val = unit_prob

        return highest_val

    if unit_cost in range(1, 6):
        # These Are The Shop Levels Where It Is Impossible To Get A Unit Of The Inputted Cost
        # Note That In This Context That A Prob Of 0 Implies That The Event Is Impossible As It Is Discretely Defined
        cant_get_at = [str(shop_level) for shop_level in shop_unit_prob_dict if shop_unit_prob_dict[shop_level][unit_cost] < 1]

        # Possible Shop Levels To Get Units Of That Cost
        can_get_at = [str(shop_level) for shop_level in shop_unit_prob_dict if shop_unit_prob_dict[shop_level][unit_cost] >= 1]

        # Better Than Average Shop Levels To Roll For A Unit Of That Cost
        good_at = [str(shop_level) for shop_level in shop_unit_prob_dict if shop_unit_prob_dict[shop_level][unit_cost] >= average_prob()]

        # Best Shop Level(s) To Roll For A Unit Of That Cost
        best_at = [str(shop_level) for shop_level in shop_unit_prob_dict if shop_unit_prob_dict[shop_level][unit_cost] == highest_prob()]

        dict_to_return = {
            'cant_get_at': cant_get_at,
            'can_get_at': can_get_at,
            'good_at': good_at,
            'best_at': best_at
        }

        return dict_to_return

#Old Code That Would Cause The Shop Levels To Be On The Same Line As The Text
# def format_data(data_dict, unit_cost):
#
#     join_str = ", "
#     suffix_str = "Cost Units At These Shop Levels\t"
#
#     available_str = f'It Is Possible To Get {unit_cost} {suffix_str}:' \
#                     f'{join_str.join(data_dict["can_get_at"])}\n'
#
#     good_str = f'We Reccomend Rolling For {unit_cost} {suffix_str}:' \
#                f'{join_str.join(data_dict["good_at"])}\n'
#
#     best_str = f'The Best Shop Levels To Roll For {unit_cost} {suffix_str.replace("At", "Are")}:' \
#                f'{join_str.join(data_dict["best_at"])}\n'
#
#     return [available_str, good_str, best_str]


# This Is Cringe But Its What We Call A Quick Fix In Buissness (Man I Can't Spell)
def format_data(data_dict, unit_cost):

    # How We Want To Connect Shop Levels That Pop Up In The Same Result
    join_str = ", "

    # Easier Than Typign The Same Crap Every Time
    suffix_str = "Cost Units At These Shop Levels\t"

    available_text_str = f'It Is Possible To Get {unit_cost} {suffix_str}:'
    available_shops_nums_str = f'{join_str.join(data_dict["can_get_at"])}\n'

    good_text_str = f'We Reccomend Rolling For {unit_cost} {suffix_str}:'
    good_shop_nums_str = f'{join_str.join(data_dict["good_at"])}\n'

    best_text_str = f'The Best Shop Levels To Roll For {unit_cost} {suffix_str.replace("At", "Are")}:'
    best_shop_nums_str = f'{join_str.join(data_dict["best_at"])}\n'

    return [
        available_text_str, available_shops_nums_str,
        good_text_str, good_shop_nums_str,
        best_text_str, best_shop_nums_str
    ]


