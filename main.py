from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import os

app = QApplication([])
main_win = QWidget()

main_line = QHBoxLayout()
left_line = QVBoxLayout()
middle_line = QVBoxLayout()
down_line = QHBoxLayout()
#
main_line.addLayout(left_line)
main_line.addLayout(middle_line)

def set_filenames(workdir):
    names_list.clear()
    all_files = os.listdir(workdir)
    norm_formats = [".jpg",".jpeg",".png"]
    norm_filenames = []
    for filename in all_files:
        for format in norm_formats:
            if filename.endswith(format):
                norm_filenames.append(filename)

    names_list.addItems(norm_filenames)

def choose_folder():
    global workdir
    username = os.environ.get('USERNAME')
    directory = "C:/Users/{0}/Pictures".format(username)

    workdir = QFileDialog.getExistingDirectory(directory=directory)
    if workdir:
        set_filenames(workdir)
    else:
        print("Выбери папку по нормальному")
        return 0

def show_pic():
    global workdir
    os.chdir(workdir)
    filename = names_list.selectedItems()[0].text()
    test = QPixmap(filename)
    pic_label.setPixmap(test)


folder_btn = QPushButton("Папка")
folder_btn.clicked.connect(choose_folder)

names_list = QListWidget()
names_list.clicked.connect(show_pic)

pic_label = QLabel()

wd_btn = QPushButton('Ч/Б')

mirror_btn = QPushButton("Отзеркалить")

left_line.addWidget(folder_btn)
left_line.addWidget(names_list)
middle_line.addWidget(pic_label)
middle_line.addLayout(down_line)
down_line.addWidget(mirror_btn)
down_line.addWidget(wd_btn)

main_win.setLayout(main_line)
main_win.resize(600, 400)
main_win.show()
app.exec()