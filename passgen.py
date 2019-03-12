''' Generate passwords based on https://xkcd.com/936/ '''

import sys
import random
from lib import gen, ui
from PyQt5 import QtWidgets

class qtpassgen(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    ''' Initialize Qt window '''

    def __init__(self, parent=None):
        super(qtpassgen, self).__init__(parent)

        self.setupUi(self)
        self.gen_button.clicked.connect(self.generate)

    def generate(self):
        ''' Call gen module based on UI input '''

        self.output.clear()
        self.output.insert(gen.pass_gen(int(self.word_count.currentText()), \
                                        self.caps.isChecked(), \
                                        int(self.max_length.currentText()), \
                                        int(self.min_length.currentText()), \
                                        self.special_char.isChecked(), \
                                        self.num.isChecked()))

def main():
    ''' Main function '''

    app = QtWidgets.QApplication(sys.argv)
    ex = qtpassgen()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
