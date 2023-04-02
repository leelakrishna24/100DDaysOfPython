def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    #   vanity plates may contain a maximum of 6 characters (letters or numbers)
    #   and a minimum of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False
    #   All vanity plates must start with at least two letters.
    if s[0].isdigit != True and s[1].isdigit != True:
        return True

    #   Numbers cannot be used in the middle of a plate; they must come at the end.
    i = 0
    while i <= len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1
    #   No periods, spaces, or punctuation marks are allowed.”
    for c in s:
        if c in ['.',' ','!','?']:
            return False
    # If we pass all the tests return truw
    return True

main()