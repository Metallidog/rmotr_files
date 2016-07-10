def string2number(a_string):
    if type(a_string) == str:
        try:
            return int(a_string)
        except:
            try:
                return float(a_string)
            except:
                raise ValueError
    raise ValueError


if __name__ == '__main__':
    print string2number('1')
    print string2number('2.3')
    print string2number('hello')
    print string2number(False)


      


