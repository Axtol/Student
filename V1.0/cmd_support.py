#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 27, 2022 10:47:46 PM CST  platform: Windows NT

import tkinter as tk

import cmd


def main():
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = cmd.Toplevel1(_top1)
    root.mainloop()


if __name__ == '__main__':
    main()
