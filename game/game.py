import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from pathlib import Path
from game.enums.misc import Misc
from game.interface.start_window import StartWindow
from game.interface.loading_window import LoadingWindow
from game.interface.initialise_new_game_task import InitialiseNewGameTask

class Game:

    def __init__(self, debug):

        # Main Game Objects
        self._debug = debug
        #self._places = None
        #self._leagues = None

        # Player Selected Game Objects
        #self._current_selected_team = None
        #self._current_teams_league = None

        # UI Windows
        self._start_window = None
        self._loading_window = None
        #self._select_team_window = None
        #self._intro_window = None
        #self._main_window = None

        # Threads & Worker Tasks
        self._game_set_up_thread = None
        self._new_game_task = None

    def start_game(self):
        app = QApplication(sys.argv)
        app.setApplicationName(Misc.GameName.value)

        folder = Path(Misc.DataFolderPath.value)
        icon_file = folder / Misc.IconFileName.value
        app.setWindowIcon(QIcon(str(icon_file)))

        css_file = folder / Misc.CSSFileName.value
        app.setStyleSheet(open(css_file).read())

        if not self._debug:
            self._start_window = StartWindow(self._new_game_button_event)
            self._start_window.show()
        else:
            self._debug_jumper()

        sys.exit(app.exec())

    def _new_game_button_event(self):
        self._start_window.close()
        self._loading_window = LoadingWindow()
        self._loading_window.show()

        self._game_set_up_thread = QtCore.QThread()
        self._new_game_task = InitialiseNewGameTask()
        self._new_game_task.moveToThread(self._game_set_up_thread)

        self._game_set_up_thread.started.connect(self._new_game_task.run)
        self._new_game_task.finished.connect(self._game_set_up_thread.quit)
        self._game_set_up_thread.finished.connect(self._after_game_set_up)

        #self.new_game_task.places_signal.connect(self.update_places)
        #self.new_game_task.league_signal.connect(self.update_leagues)

        self._game_set_up_thread.start()

    def _after_game_set_up(self):
        self._loading_window.close()
        #self.select_team_window = SelectTeamWindow(self.leagues, self.team_selected)
        #self.select_team_window.show()

    def _debug_jumper(self):
        # DEBUG METHOD TO JUMP TO SPECIFIC POINTS
        print("beep")