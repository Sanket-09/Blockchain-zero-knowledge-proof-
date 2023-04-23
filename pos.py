from models import User


def verify(curr_user, current_owner, property_chosen):
    if (curr_user.wealth >= property_chosen.amount):
        return True
    else:
        return False


def find_pos(curr_user, current_owner, property_chosen):

    balance = -1
    leader = None
    for user in User.users:
        if user.wealth >= balance:
            balance = user.wealth
            leader = user

    if verify(curr_user, current_owner, property_chosen):
        return leader
    else:
        return -1


