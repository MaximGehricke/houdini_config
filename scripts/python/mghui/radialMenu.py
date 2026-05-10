import hou, math
from PySide6 import QtWidgets, QtCore, QtGui

class InfiniteRadialMenu(QtWidgets.QWidget):
    def __init__(self, menu_dict, radius=130, btn_size=80):
        super(InfiniteRadialMenu, self).__init__(hou.qt.mainWindow(), QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        
        self.menu_dict = menu_dict
        self.labels = list(menu_dict.keys())
        self.radius = radius
        self.btn_size = btn_size
        
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        self.setFixedSize(1000, 1000)
        self.center = self.rect().center()
        self.hovered_idx = -1
        self.buttons = []
        
        self._build_buttons()
        self.move(QtGui.QCursor.pos() - self.center)

    def get_style(self, hovered):
        bg = "#00aaff" if hovered else "#333"
        return f"""
            QPushButton {{
                background-color: {bg};
                color: white;
                border: 2px solid {"#fff" if hovered else "#555"};
                border-radius: {self.btn_size // 2}px;
                font-size: 10px;
                padding: 2px;
            }}
        """

    def _build_buttons(self):
        num_items = len(self.labels)
        for i, label in enumerate(self.labels):
            btn = QtWidgets.QPushButton(label, self)
            btn.setFixedSize(self.btn_size, self.btn_size)
            btn.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
            
            angle = math.radians((i * 360 / num_items) - 90)
            x = self.center.x() + self.radius * math.cos(angle) - self.btn_size / 2
            y = self.center.y() + self.radius * math.sin(angle) - self.btn_size / 2
            
            btn.move(int(x), int(y))
            btn.setStyleSheet(self.get_style(False))
            self.buttons.append(btn)

    def get_index_at_pos(self, pos):
        offset = pos - self.center
        dist = math.sqrt(offset.x()**2 + offset.y()**2)
        if dist < 30: return -1
        
        angle = math.degrees(math.atan2(-offset.y(), offset.x()))
        adj = (90 - angle + 360) % 360
        slice_size = 360 / len(self.labels)
        return int((adj + (slice_size / 2)) % 360 // slice_size)

    def mouseMoveEvent(self, event):
        new_idx = self.get_index_at_pos(event.pos())
        if new_idx != self.hovered_idx:
            if self.hovered_idx != -1:
                self.buttons[self.hovered_idx].setStyleSheet(self.get_style(False))
            self.hovered_idx = new_idx
            if self.hovered_idx != -1:
                self.buttons[self.hovered_idx].setStyleSheet(self.get_style(True))

    def mousePressEvent(self, event):
        if self.hovered_idx != -1:
            label = self.labels[self.hovered_idx]
            func = self.menu_dict[label]
            if func: func() # Execute the passed function
        self.close()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape: self.close()

def run(menu_config):
    """Utility function to launch the menu safely."""
    if hasattr(hou.session, 'radial_menu'):
        try: hou.session.radial_menu.close()
        except: pass
    
    hou.session.radial_menu = InfiniteRadialMenu(menu_config)
    hou.session.radial_menu.show()