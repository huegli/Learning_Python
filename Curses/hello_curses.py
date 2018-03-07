#!/usr/bin/env python

import curses

def main(stdscr):
    stdscr.addstr(5 ,5 ," Hello World " )
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
