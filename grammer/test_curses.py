#!/usr/bin/python
import curses


stdscr = curses.initscr()
def set_win():
    global stdscr
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(1)

def print_info(x, y, info, colorpair=2):
    global stdscr
    stdscr.addstr(y, x, info, colorpair)
    stdscr.refresh()

def get_ch_echo():
    global stdscr
    stdscr.nodelay(0)
    c = stdscr.getch()
    stdscr.nodelay(1)
    return True

def unset_win():
    global stdscr
    stdscr.nocbreak()
    stdscr.keypad(0)
    stdscr.echo()
    curses.endwin()

def main():
    try:
        set_win()
        print_info(0, 5, 'test string')
        print_info(0, 10, 'hello world')
        get_ch_echo()
    except Exception,e:
        raise e
    finally:
        unset_win()

if __name__ == '__main__':
    main()
