# напиши здесь код для второго экрана приложения
class TestWin(Qwidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_heigth)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout
        self.r_line = QVBoxLayout
        self.l_line = QVBoxLayout

        
    def connects(self):
        pass
    
