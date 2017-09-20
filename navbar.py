from PySide2 import QtWidgets

def createInterface():
    adv_btn = QtWidgets.QPushbutton()
    adv_btn.label = "Advance"

    root_widget = QtWidgets.QWidget()
    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(adv_btn)
    root_widget.setLayout(layout)

    return root_widget