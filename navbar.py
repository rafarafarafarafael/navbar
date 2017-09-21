from PySide2 import QtWidgets
from PySide2 import QtCore

class Navbar(QtWidgets.QWidget):
    # create interface elements
    s_incr_parm = s_incr_parm = QtWidgets.QLineEdit('12')
    l_rew_btn = QtWidgets.QPushButton('<<')
    s_rew_btn = QtWidgets.QPushButton('<')
    l_incr_parm = QtWidgets.QLineEdit('24')
    s_ff_btn = QtWidgets.QPushButton('>')
    l_ff_btn = QtWidgets.QPushButton('>>')
    
    # class initializer
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        
        self.setProperty("houdiniStyle", True)

        self.s_incr_parm.setPlaceholderText('12')
        self.s_incr_parm.setGeometry(QtCore.QRect(0, 0, 10, 20))
        self.l_incr_parm.setPlaceholderText('24')
        self.l_incr_parm.setGeometry(QtCore.QRect(0, 0, 10, 20))
        self.s_ff_btn.clicked.connect(self.nav_sff)
        self.s_rew_btn.clicked.connect(self.nav_srw)
        self.l_ff_btn.clicked.connect(self.nav_lff)
        self.l_rew_btn.clicked.connect(self.nav_lrw)

        layout = QtWidgets.QHBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.l_rew_btn)
        layout.addWidget(self.s_rew_btn)
        layout.addWidget(self.s_incr_parm)
        layout.addWidget(self.l_incr_parm)
        layout.addWidget(self.s_ff_btn)
        layout.addWidget(self.l_ff_btn)
        layout.addStretch(1)

        self.setLayout(layout)


    # created methods
    def navigate(self, frame_incr = 12, direction = 'f'):
        frameTo = hou.frame()
        if direction == 'f' or direction == 1:
            frameTo += frame_incr
        elif direction == 'r' or direction == 0:
            frameTo -= frame_incr
        hou.setFrame(frameTo)

    def nav_sff(self):
        frame_incr = int(self.s_incr_parm.text())
        self.navigate(frame_incr, 'f')

    def nav_srw(self):
        frame_incr = int(self.s_incr_parm.text())
        self.navigate(frame_incr, 'r')

    def nav_lff(self):
        frame_incr = int(self.l_incr_parm.text())
        self.navigate(frame_incr, 'f')

    def nav_lrw(self):
        frame_incr = int(self.l_incr_parm.text())
        self.navigate(frame_incr, 'r')

def createInterface():
    root_widget = Navbar() 
    return root_widget