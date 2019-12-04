

def validate_passwd(passwd, start, end):
    if passwd > end or passwd < start:
        return False

    lst_passwd = list(str(passwd))

    # Six-digit number
    if len(lst_passwd) != 6:
        return False

    # If decreases
    for i in range(len(lst_passwd)):
        for j in range(i+1, len(lst_passwd)):
            if int(lst_passwd[i]) > int(lst_passwd[j]):
                return False

    # If two adjacent digits are the same
    has_adjacent = False
    for i in range(len(lst_passwd)-1):
        if lst_passwd[i] == lst_passwd[i+1]:
            has_adjacent = True

    if has_adjacent:
        return True
    else:
        return False

if __name__ == "__main__":
    start = 307237
    end = 769058

    valid_passwds = 0
    for passwd in range(start, end+1):
        if validate_passwd(passwd, start, end):
            valid_passwds += 1

    print(valid_passwds)
