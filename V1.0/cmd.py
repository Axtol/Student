#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
# in conjunction with Tcl version 8.6
# May 27, 2022 10:49:47 PM CST  platform: Windows NT
import os
import pickle
import re  # 引入正则表达式
import tkinter as tk  # /
#                        |  兼容性
from tkinter import *  # \


def rese(text):
    cPre = re.compile(
        """update <.*> if id == <.*> change <.*> to <.*>|delete <.*> if id == <.*>|create HashFile dir == <.*>|show all <.*>|save text all <.*>|search <.*> if id == <.*>""")  # 编译正则表达式
    # 语句格式：
    # update <hashTabelFileLoad> if id == <id> change <key> to <item> √
    # 使用这个来改变某一项。
    # delete <hashTabelFileLoad> if id == <id> √
    # 使用这个删除某一项。
    # search <hashTabel> if id == <id> √
    # 使用这个搜索某一项。
    # create HashFile dir == <hashTabelFileLoad> √
    # 使用这个来创造一个哈希表文件（*.htf/*.hash）
    # show all <HashFile> √
    # save text all <HashFile> √
    try:
        tmp = re.findall(cPre, text)
        res = re.findall("<.*?>", tmp[0])
        print(tmp)
        print(res)
        if res:
            if len(res) == 2:
                hashLoad = res[0].lstrip("<").rstrip(">")
                idS = res[1].lstrip("<").rstrip(">")
                return hashLoad, idS
            elif len(res) == 1:
                hashLoad = res[0].lstrip("<").rstrip(">")
                return hashLoad,
            elif len(res) == 4:
                hashLoad = res[0].lstrip("<").rstrip(">")
                idS = res[1].lstrip("<").rstrip(">")
                key = res[2].lstrip("<").rstrip(">")
                value = res[3].lstrip("<").rstrip(">")
                return hashLoad, idS, key, value
            else:
                return False
    except Exception:
        pass
    else:
        return False


class Toplevel1:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("960x540+439+199")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("command-line pattern")
        top.configure(background="#000000")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Labelframe1 = tk.LabelFrame(self.top)
        self.Labelframe1.place(relx=0.0, rely=0.0, relheight=0.694, relwidth=1.0)

        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(font="-family {Envy Code R} -size 12")
        self.Labelframe1.configure(foreground="#ffffff")
        self.Labelframe1.configure(text='''command display area''')
        self.Labelframe1.configure(background="#000000")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.sb = Scrollbar(self.Labelframe1)
        self.sb.place(relx=0.98, rely=0, relheight=1.0, relwidth=0.02)

        self.Text1 = tk.Text(self.Labelframe1)
        self.Text1.place(relx=0.0, rely=0.053, relheight=1.0, relwidth=0.978,
                         bordermode='ignore')
        self.Text1.configure(background="#000000")
        self.Text1.configure(font="-family {Envy Code R} -size 12")
        self.Text1.configure(foreground="#ffffff")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="#ffffff")
        self.Text1.configure(selectbackground="#ffffff")
        self.Text1.configure(selectforeground="#000000")
        self.Text1.configure(wrap="word")
        self.Text1.configure(yscrollcommand=self.sb.set)
        self.sb.configure(command=self.Text1.yview)
        self.Text1["state"] = DISABLED

        self.Labelframe2 = tk.LabelFrame(self.top)
        self.Labelframe2.place(relx=0.0, rely=0.822, relheight=0.176,
                               relwidth=1.0)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(font="-family {Envy Code R} -size 12")
        self.Labelframe2.configure(foreground="#ffffff")
        self.Labelframe2.configure(text='''command input area''')
        self.Labelframe2.configure(background="#000000")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.Labelframe2)
        self.Entry1.place(relx=0.003, rely=0.232, height=67, relwidth=0.9,
                          bordermode='ignore')
        self.Entry1.configure(background="#000000")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Envy Code R} -size 12")
        self.Entry1.configure(foreground="#ffffff")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="#ffffff")
        self.Entry1.configure(selectbackground="#ffffff")
        self.Entry1.configure(selectforeground="#000000")
        self.Entry1.bind("<Control-Up>", self.on_input_search)

    def on_input_search(self, event):
        print(event)
        text = self.Entry1.get()
        res = rese(text=text)  # 搜索
        print(text)
        print(res)

        if not res:
            self.Text1["state"] = NORMAL
            self.Text1.insert(END, f"""Error!
Traceback (most recent call):
    File "memory", line 1, in input:
        {text}
    Syntax Error: [{text}] none action item in this statement.\a
""")  # 异常显示
            self.Text1["state"] = DISABLED

        else:

            if len(res) == 1:
                if text.startswith("show"):
                    if os.path.exists(os.path.dirname(res[0])):
                        with open(os.path.join(res[0]), "rb") as f:
                            dicStr = str(pickle.load(f))
                        self.Text1["state"] = NORMAL
                        self.Text1.configure(wrap=WORD)
                        self.Text1.insert(END, "\n\n" + dicStr)  # 写入
                        self.Text1["state"] = DISABLED
                    else:
                        self.Text1["state"] = NORMAL
                        self.Text1.insert(END, f"""Error!
Traceback (most recent call):
    File "memory", line 1, in input:
        {text}
    File Not Found Error: No such path:{res[0]}.\a
                                            """)
                        self.Text1["state"] = DISABLED
                elif text.startswith("create"):
                    if os.path.exists(os.path.dirname(res[0])):  # 如果没有就创建
                        os.chdir(os.path.dirname(res[0]))
                    else:
                        os.makedirs(os.path.dirname(res[0]))  # 创建
                    os.chdir(os.path.dirname(res[0]))
                    with open(os.path.basename(res[0]), "wb") as f:
                        a = {}  # 写入哈希表
                        pickle.dump(a, f)  # 二进制保存

                elif text.startswith("save"):
                    if os.path.exists(os.path.dirname(res[0])):
                        f = open("./demo.txt", "w")
                        with open(os.path.join(res[0]), "rb") as d:
                            f.write(str(pickle.load(d)))
                        self.Text1["state"] = NORMAL
                        self.Text1.insert(END, f"File Save in {os.getcwd()}\\demo.txt")  # 写入
                        self.Text1["state"] = DISABLED
                        f.close()
                    else:
                        self.Text1["state"] = NORMAL
                        self.Text1.insert(END, f"""Error!
Traceback (most recent call):
    File "memory", line 1, in input:
        {text}
    File Not Found Error: No such path:{res[0]}.\a
                        """)
                        self.Text1["state"] = DISABLED

            elif len(res) == 2:
                if text.startswith("delete"):
                    if os.path.exists(os.path.dirname(res[0])):  # 如果没有就报错
                        if len(res[1]) == 8:  # ID格式
                            with open(os.path.basename(res[0]), "rb+") as f:
                                try:
                                    dic = pickle.load(f)
                                except EOFError:
                                    pass
                                del dic[res[1]]  # 执行删除操作
                            with open(os.path.basename(res[0]), "wb") as f:
                                pickle.dump(dic, f)
                            self.Text1["state"] = NORMAL
                            self.Text1.insert(END, f"""
Deleting……\n……\n\a
Delete successful.\n
                                            """)
                            self.Text1["state"] = DISABLED

                        else:
                            self.Text1["state"] = NORMAL
                            self.Text1.insert(END, f"""Error!
Traceback (most recent call):
    File "memory", line 1, in input:
        {text}
    ID Error: Error ID:{res[1]}.\a
                        """)
                            self.Text1["state"] = DISABLED

                    else:
                        self.Text1["state"] = NORMAL
                        self.Text1.insert(END, f"""Error!
Traceback (most recent call):
    File "memory", line 1, in input:
        {text}
    File Not Found Error: No such path:{res[0]}.\a
                        """)    # 显示错误
                        self.Text1["state"] = DISABLED
                elif text.startswith("search"):
                    if os.path.exists(os.path.dirname(res[0])):  # 如果没有就报错
                        if len(res[1]) == 8:  # ID格式
                            with open(os.path.basename(res[0]), "rb+") as f:
                                try:
                                    dic = pickle.load(f)
                                except EOFError:
                                    pass
                            self.Text1["state"] = NORMAL
                            self.Text1.insert(END, f"""
Searching……
Search Success.
in db<{res[0]}>.
↓↓↓↓↓\a
                                        """)    # 显示错误
                            self.Text1.insert(END, dic[res[1]])  # 执行查找
                            self.Text1["state"] = DISABLED

                        else:
                            self.Text1["state"] = NORMAL
                            self.Text1.insert(END, f"""Error!
                    Traceback (most recent call):
                        File "memory", line 1, in input:
                            {text}
                        ID Error: Error ID:{res[1]}\n.
                                        """)    # 显示错误
                            self.Text1["state"] = DISABLED

                    else:
                        self.Text1["state"] = NORMAL
                        self.Text1.insert(END, f"""Error!
Traceback (most recent call):
    File "memory", line 1, in input:
        {text}
    File Not Found Error: No such path:{res[0]}\n\a.
                                        """)    # 显示错误
                        self.Text1["state"] = DISABLED

            elif len(res) == 4:

                if os.path.exists(res[0]):  # 如果没有就报错

                    if len(res[1]) == 8:  # ID格式
                        with open(res[0], "rb+") as f:
                            dic = pickle.load(f)
                            dic[res[1]][res[2]] = [res[3]]
                            pickle.dump(dic, f)
                    else:
                        self.Text1["state"] = NORMAL
                        self.Text1.insert(END, f"""Error!
Traceback (most recent call):
    File "memory", line 1, in input:
        {text}
    ID Error: Error ID:{res[1]}.\n\a
                                            """)    # 显示cw
                        self.Text1["state"] = DISABLED
        self.Entry1.delete(0, END)


if __name__ == "__main__":
    import cmd_support
    cmd_support.main()
