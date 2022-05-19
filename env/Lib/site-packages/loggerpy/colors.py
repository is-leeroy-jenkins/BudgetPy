def get_color(type='0', bg='0', fg='0', text=' '):
    start = '\x1b['
    stop = '\x1b[0m'
    color = '{};{};{}m'.format(type, fg, bg)
    s = start + color + text + stop
    return s


def test_color():
    """
    Print all combination of colors
    """
    for style in range(10):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                # print('{} {} {}'.format(style, fg, bg))
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


class colors:
    start = '\x1b['
    stop = '\x1b[0m'

    reset = '0'
    bold = '01'
    disable = '02'
    underline = '04'
    reverse = '07'
    strikethrough = '09'
    invisible = '08'

    @staticmethod
    def get_color(type='0', bg='0', fg='30'):
        return '{};{};{}m'.format(type, bg, fg)

    class fg:
        black = '30'
        red = '31'
        green = '32'
        orange = '33'
        blue = '34'
        purple = '35'
        cyan = '36'
        lightgrey = '37'
        darkgrey = '90'
        lightred = '91'
        lightgreen = '92'
        yellow = '93'
        lightblue = '94'
        pink = '95'
        lightcyan = '96'

    class bg:
        black = '40'
        red = '41'
        green = '42'
        orange = '43'
        blue = '44'
        purple = '45'
        cyan = '46'
        lightgrey = '47'
