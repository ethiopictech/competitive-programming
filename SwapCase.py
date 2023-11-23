def chr(c):
    if str.islower(c):
        return str.upper(c)
    else:
        return str.lower(c)
def swap_case(s):
    return "".join(map(chr,s))

if __name__ == '__main__':
