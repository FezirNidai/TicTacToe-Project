#decide win

def check_win(entries, player):
    if entries[0] == entries[1] == entries[2] == player or \
        entries[3] == entries[4] == entries[5] == player or 
        entries[6] == entries[7] == entries[8] == player:
        return True
    elif entries[0] == entries[3] == entries[6] == player or 
        entries[1] == entries[4] == entries[7] == player or 
        entries[2] == entries[5] == entries[8] == player:
        return True
    elif entries[0] == entries[4] == entries[8] == player or 
        entries[2] == entries[4] == entries[6] == player:
        return True
    return False 