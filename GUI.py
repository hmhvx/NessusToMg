import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog

class NessusDocumentOrganizer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle("Nessus文档整理工具")

        # 创建主布局
        layout = QVBoxLayout()

        # 创建日志框
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        layout.addWidget(self.log_text)

        # 创建按钮并添加到布局
        self.choose_nessus_button = QPushButton("选择Nessus文档")
        self.choose_nessus_button.clicked.connect(self.choose_nessus_document)
        layout.addWidget(self.choose_nessus_button)

        self.choose_awvs_button = QPushButton("选择AWVS文档")
        self.choose_awvs_button.clicked.connect(self.choose_awvs_document)
        layout.addWidget(self.choose_awvs_button)

        # 设置窗口布局
        self.setLayout(layout)
        self.setGeometry(100, 100, 900, 600)  # 设置窗口大小和位置


        # 获取主屏幕的几何信息
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()

        # 计算使窗口居中的坐标
        window_size = self.size()
        x = (screen_geometry.width() - window_size.width()) // 2
        y = (screen_geometry.height() - window_size.height()) // 2

        # 设置窗口位置至屏幕中心
        self.move(x, y)

    def choose_nessus_document(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择Nessus文件", "", "文本文件 (*.txt);;所有文件 (*)")
        if file_path:
            self.log_text.append(f"选择了Nessus文档: {file_path}")

    def choose_awvs_document(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择AWVS文件", "", "文本文件 (*.txt);;所有文件 (*)")
        if file_path:
            self.log_text.append(f"选择了AWVS文档: {file_path}")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NessusDocumentOrganizer()
    window.show()
    sys.exit(app.exec())


