from PySide2 import QtWidgets
from PySide2 import QtCore

def navigate(frame_incr = 12, direction = 'f'):
    frameTo = hou.frame()
    if direction == 'f' or direction == 1:
        frameTo += frame_incr
    elif direction == 'r' or direction == 0:
        frameTo -= frame_incr
    hou.setFrame(frameTo)

def nav_sff():
    frame_incr = 12
    navigate(frame_incr, 'f')

def createInterface():
    l_rew_btn = QtWidgets.QPushButton('<<')
    s_rew_btn = QtWidgets.QPushButton('<')
    s_incr_parm = QtWidgets.QLineEdit('12')
    s_incr_parm.setPlaceholderText('12')
    l_incr_parm = QtWidgets.QLineEdit('24')
    l_incr_parm.setPlaceholderText('24')
    s_incr_parm.setGeometry(QtCore.QRect(0, 0, 10, 20))
    l_incr_parm.setGeometry(QtCore.QRect(0, 0, 10, 20))
    s_ff_btn = QtWidgets.QPushButton('>')
    l_ff_btn = QtWidgets.QPushButton('>>')

    root_widget = QtWidgets.QWidget()
    layout = QtWidgets.QHBoxLayout()
    layout.addStretch(1)
    layout.addWidget(l_rew_btn)
    layout.addWidget(s_rew_btn)
    layout.addWidget(s_incr_parm)
    layout.addWidget(l_incr_parm)
    layout.addWidget(s_ff_btn)
    layout.addWidget(l_ff_btn)
    layout.addStretch(1)
    root_widget.setLayout(layout)

    s_ff_btn.clicked.connect(nav_sff)
    
    return root_widget