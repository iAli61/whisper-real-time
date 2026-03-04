from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 700)
        MainWindow.setStyleSheet(
            "QTabBar::tab { width: 200px; } QMenuBar::item  { padding-left: 25px;   padding-right: 20px; }")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(4, 4, 4, 4)
        main_layout.setSpacing(4)

        # ── Tab Widget ──
        self.tabWidget = QtWidgets.QTabWidget()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        main_layout.addWidget(self.tabWidget, 1)

        # ═══════════════════════════════════════════════
        # Tab 1 – STT Recorder
        # ═══════════════════════════════════════════════
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        tab1_layout = QtWidgets.QVBoxLayout(self.tab_1)

        # Labels
        tab1_labels = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel("File List")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel("Recorder Result")
        self.label_2.setObjectName("label_2")
        tab1_labels.addWidget(self.label)
        tab1_labels.addWidget(self.label_2)
        tab1_layout.addLayout(tab1_labels)

        # Content
        tab1_content = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.tableView = QtWidgets.QTableView()
        self.tableView.setObjectName("tableView")
        self.textEdit_recorder = QtWidgets.QTextEdit()
        self.textEdit_recorder.setObjectName("textEdit_recorder")
        tab1_content.addWidget(self.tableView)
        tab1_content.addWidget(self.textEdit_recorder)
        tab1_content.setStretchFactor(0, 1)
        tab1_content.setStretchFactor(1, 1)
        tab1_layout.addWidget(tab1_content, 1)

        # Status row
        tab1_status = QtWidgets.QHBoxLayout()
        self.label_8 = QtWidgets.QLabel("File Status")
        self.label_8.setObjectName("label_8")
        self.lineEdit_file = QtWidgets.QLineEdit()
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.label_7 = QtWidgets.QLabel("Recorder Status")
        self.label_7.setObjectName("label_7")
        self.lineEdit_recorder = QtWidgets.QLineEdit()
        self.lineEdit_recorder.setObjectName("lineEdit_recorder")
        tab1_status.addWidget(self.label_8)
        tab1_status.addWidget(self.lineEdit_file, 1)
        tab1_status.addWidget(self.label_7)
        tab1_status.addWidget(self.lineEdit_recorder, 1)
        tab1_layout.addLayout(tab1_status)

        # Buttons row
        tab1_buttons = QtWidgets.QHBoxLayout()
        self.pushButton_play = QtWidgets.QPushButton("Play")
        self.pushButton_play.setObjectName("pushButton_play")
        self.pushButton_play.setMinimumHeight(36)
        self.pushButton_delete = QtWidgets.QPushButton("Delete")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_delete.setMinimumHeight(36)
        self.pushButton_record = QtWidgets.QPushButton("Record")
        self.pushButton_record.setObjectName("pushButton_record")
        self.pushButton_record.setMinimumHeight(36)
        self.pushButton_submit = QtWidgets.QPushButton("Submit")
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.pushButton_submit.setMinimumHeight(36)
        tab1_buttons.addWidget(self.pushButton_play)
        tab1_buttons.addWidget(self.pushButton_delete)
        tab1_buttons.addStretch()
        tab1_buttons.addWidget(self.pushButton_record)
        tab1_buttons.addWidget(self.pushButton_submit)
        tab1_layout.addLayout(tab1_buttons)

        self.tabWidget.addTab(self.tab_1, "")

        # ═══════════════════════════════════════════════
        # Tab 2 – STT Real Time
        # ═══════════════════════════════════════════════
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        tab2_layout = QtWidgets.QVBoxLayout(self.tab)

        # Labels
        tab2_labels = QtWidgets.QHBoxLayout()
        self.label_12 = QtWidgets.QLabel("Transcribe Result")
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel("Real Time Result")
        self.label_11.setObjectName("label_11")
        tab2_labels.addWidget(self.label_12)
        tab2_labels.addWidget(self.label_11)
        tab2_layout.addLayout(tab2_labels)

        # Content
        tab2_content = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.textEdit_transcribe = QtWidgets.QTextEdit()
        self.textEdit_transcribe.setObjectName("textEdit_transcribe")
        self.textEdit_realtime = QtWidgets.QTextEdit()
        self.textEdit_realtime.setObjectName("textEdit_realtime")
        tab2_content.addWidget(self.textEdit_transcribe)
        tab2_content.addWidget(self.textEdit_realtime)
        tab2_content.setStretchFactor(0, 1)
        tab2_content.setStretchFactor(1, 1)
        tab2_layout.addWidget(tab2_content, 1)

        # Status row
        tab2_status = QtWidgets.QHBoxLayout()
        self.label_10 = QtWidgets.QLabel("Transcribe Status")
        self.label_10.setObjectName("label_10")
        self.lineEdit_transcribe = QtWidgets.QLineEdit()
        self.lineEdit_transcribe.setObjectName("lineEdit_transcribe")
        self.label_9 = QtWidgets.QLabel("Real Time Status")
        self.label_9.setObjectName("label_9")
        self.lineEdit_realtime = QtWidgets.QLineEdit()
        self.lineEdit_realtime.setObjectName("lineEdit_realtime")
        tab2_status.addWidget(self.label_10)
        tab2_status.addWidget(self.lineEdit_transcribe, 1)
        tab2_status.addWidget(self.label_9)
        tab2_status.addWidget(self.lineEdit_realtime, 1)
        tab2_layout.addLayout(tab2_status)

        # Buttons row
        tab2_buttons = QtWidgets.QHBoxLayout()
        self.pushButton_begin = QtWidgets.QPushButton("Begin")
        self.pushButton_begin.setObjectName("pushButton_begin")
        self.pushButton_begin.setMinimumHeight(36)
        self.pushButton_end = QtWidgets.QPushButton("End")
        self.pushButton_end.setObjectName("pushButton_end")
        self.pushButton_end.setMinimumHeight(36)
        tab2_buttons.addWidget(self.pushButton_begin)
        tab2_buttons.addStretch()
        tab2_buttons.addWidget(self.pushButton_end)
        tab2_layout.addLayout(tab2_buttons)

        self.tabWidget.addTab(self.tab, "")

        # ═══════════════════════════════════════════════
        # Tab 3 – STT Live
        # ═══════════════════════════════════════════════
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        tab3_layout = QtWidgets.QVBoxLayout(self.tab_2)

        # Labels
        tab3_labels = QtWidgets.QHBoxLayout()
        self.label_3 = QtWidgets.QLabel("Final Result")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel("Live Result")
        self.label_4.setObjectName("label_4")
        tab3_labels.addWidget(self.label_3)
        tab3_labels.addWidget(self.label_4)
        tab3_layout.addLayout(tab3_labels)

        # Content
        tab3_content = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.textEdit_final = QtWidgets.QTextEdit()
        self.textEdit_final.setObjectName("textEdit_final")
        self.textEdit_live = QtWidgets.QTextEdit()
        self.textEdit_live.setObjectName("textEdit_live")
        tab3_content.addWidget(self.textEdit_final)
        tab3_content.addWidget(self.textEdit_live)
        tab3_content.setStretchFactor(0, 1)
        tab3_content.setStretchFactor(1, 1)
        tab3_layout.addWidget(tab3_content, 1)

        # Status row
        tab3_status = QtWidgets.QHBoxLayout()
        self.label_5 = QtWidgets.QLabel("Final Status")
        self.label_5.setObjectName("label_5")
        self.lineEdit_final = QtWidgets.QLineEdit()
        self.lineEdit_final.setObjectName("lineEdit_final")
        self.label_6 = QtWidgets.QLabel("Live Status")
        self.label_6.setObjectName("label_6")
        self.lineEdit_live = QtWidgets.QLineEdit()
        self.lineEdit_live.setObjectName("lineEdit_live")
        tab3_status.addWidget(self.label_5)
        tab3_status.addWidget(self.lineEdit_final, 1)
        tab3_status.addWidget(self.label_6)
        tab3_status.addWidget(self.lineEdit_live, 1)
        tab3_layout.addLayout(tab3_status)

        # Buttons row
        tab3_buttons = QtWidgets.QHBoxLayout()
        self.pushButton_live = QtWidgets.QPushButton("Live")
        self.pushButton_live.setObjectName("pushButton_live")
        self.pushButton_live.setMinimumHeight(36)
        self.pushButton_continue = QtWidgets.QPushButton("Continue")
        self.pushButton_continue.setObjectName("pushButton_continue")
        self.pushButton_continue.setMinimumHeight(36)
        self.pushButton_stop = QtWidgets.QPushButton("Stop")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_stop.setMinimumHeight(36)
        self.pushButton_finish = QtWidgets.QPushButton("Finish")
        self.pushButton_finish.setObjectName("pushButton_finish")
        self.pushButton_finish.setMinimumHeight(36)
        tab3_buttons.addWidget(self.pushButton_live)
        tab3_buttons.addWidget(self.pushButton_continue)
        tab3_buttons.addStretch()
        tab3_buttons.addWidget(self.pushButton_stop)
        tab3_buttons.addWidget(self.pushButton_finish)
        tab3_layout.addLayout(tab3_buttons)

        self.tabWidget.addTab(self.tab_2, "")

        # ═══════════════════════════════════════════════
        # Bottom status panel (shared across tabs)
        # ═══════════════════════════════════════════════
        status_group = QtWidgets.QGroupBox()
        status_layout = QtWidgets.QFormLayout(status_group)
        status_layout.setContentsMargins(6, 6, 6, 6)

        self.label_14 = QtWidgets.QLabel("Status Console")
        self.label_14.setObjectName("label_14")
        self.lineEdit_status = QtWidgets.QLineEdit()
        self.lineEdit_status.setObjectName("lineEdit_status")
        status_layout.addRow(self.label_14, self.lineEdit_status)

        self.label_13 = QtWidgets.QLabel("Progress Bar")
        self.label_13.setObjectName("label_13")
        self.lineEdit_progress = QtWidgets.QLineEdit()
        self.lineEdit_progress.setObjectName("lineEdit_progress")
        status_layout.addRow(self.label_13, self.lineEdit_progress)

        main_layout.addWidget(status_group)

        MainWindow.setCentralWidget(self.centralwidget)

        # ── Menu Bar ──
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menuqt_ui = QtWidgets.QMenu(self.menubar)
        self.menuqt_ui.setObjectName("menuqt_ui")
        self.menutest_ui = QtWidgets.QMenu(self.menubar)
        self.menutest_ui.setObjectName("menutest_ui")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionproperties = QtWidgets.QAction(MainWindow)
        self.actionproperties.setObjectName("actionproperties")
        self.actionimport = QtWidgets.QAction(MainWindow)
        self.actionimport.setObjectName("actionimport")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.menuqt_ui.addAction(self.actionimport)
        self.menutest_ui.addAction(self.actionproperties)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuqt_ui.menuAction())
        self.menubar.addAction(self.menutest_ui.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Whisper Real Time"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_play.setText(_translate("MainWindow", "Play"))
        self.pushButton_submit.setText(_translate("MainWindow", "Submit"))
        self.pushButton_record.setText(_translate("MainWindow", "Record"))
        self.label.setText(_translate("MainWindow", "File List"))
        self.label_2.setText(_translate("MainWindow", "Recorder Result"))
        self.label_7.setText(_translate("MainWindow", "Recorder Status"))
        self.label_8.setText(_translate("MainWindow", "File Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "STT Recorder"))
        self.label_9.setText(_translate("MainWindow", "Real Time Status"))
        self.label_10.setText(_translate("MainWindow", "Transcribe Status"))
        self.label_11.setText(_translate("MainWindow", "Real Time Result"))
        self.label_12.setText(_translate("MainWindow", "Transcribe Result"))
        self.pushButton_end.setText(_translate("MainWindow", "End"))
        self.pushButton_begin.setText(_translate("MainWindow", "Begin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "STT Real Time"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.pushButton_live.setText(_translate("MainWindow", "Live"))
        self.pushButton_finish.setText(_translate("MainWindow", "Finish"))
        self.pushButton_continue.setText(_translate("MainWindow", "Continue"))
        self.label_3.setText(_translate("MainWindow", "Final Result"))
        self.label_4.setText(_translate("MainWindow", "Live Result"))
        self.label_5.setText(_translate("MainWindow", "Final Status"))
        self.label_6.setText(_translate("MainWindow", "Live Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "STT Live"))
        self.label_13.setText(_translate("MainWindow", "Progress Bar"))
        self.label_14.setText(_translate("MainWindow", "Status Console"))
        self.menuqt_ui.setTitle(_translate("MainWindow", "File"))
        self.menutest_ui.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionproperties.setText(_translate("MainWindow", "Properties"))
        self.actionimport.setText(_translate("MainWindow", "Import"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
