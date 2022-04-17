def gold_calculator(start_gold, turns):

    """

    Args:
        start_gold: (int) Inital Amount Of Gold
        turns: (int) Number Of Future Turns That Are To Go By

    Returns:

    """

    if type(start_gold) == int and type(turns) == int:

        if turns >= 0 and start_gold >= 0:

            final_amount = start_gold
            base_income = 5

            for turn in range(turns):

                if final_amount <= 9:
                    final_amount += base_income

                elif 10 <= final_amount <= 19:
                    final_amount += base_income + 1

                elif 20 <= final_amount <= 29:
                    final_amount += base_income + 2

                elif 30 <= final_amount <= 39:
                    final_amount += base_income + 3

                elif 40 <= final_amount <= 49:
                    final_amount += base_income + 4

                else:   # It Is 50 Or Greater
                    final_amount += base_income + 5

            result_text = f'In {turns} Turn(s) You Will Have {final_amount} Gold.'

        else:   # Inform To Enter A Non-Negative Number
            result_text = 'Please Enter Non-Negative Integer Arguments'

    else:   # Inform Them To Enter Strictly Integers
        result_text = 'Please Enter Non-Negative Integer Arguments'

    # We Iterate Through Text In Html So Need It As List
    return [result_text]