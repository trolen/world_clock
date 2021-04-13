#!/usr/bin/env python3

from datetime import datetime
import pytz
import time
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import QTimer


class Application:
    def __init__(self):
        self._clock_fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        self._tz_utc = pytz.timezone('UTC')
        self._tz_eastern = pytz.timezone('US/Eastern')
        self._tz_central = pytz.timezone('US/Central')
        self._tz_mountain = pytz.timezone('US/Mountain')
        self._tz_pacific = pytz.timezone('US/Pacific')
        self._tz_berlin = pytz.timezone('Europe/Berlin')
        self._tz_london = pytz.timezone('Europe/London')
        self._tz_paris = pytz.timezone('Europe/Paris')
        self._timer = QTimer()
        self._timer.timeout.connect(self._show_clock)

    def _create_label(self, owner, labelText, yPos, x1, x2):
        lab = QLabel(owner)
        lab.setText(labelText)
        lab.move(x1, yPos)
        result = QLabel(owner)
        result.setText(' '*60)
        result.move(x2, yPos)
        return result
    
    def _show_clock(self):
        utc_dt = datetime.now(self._tz_utc)
        eastern_dt = utc_dt.astimezone(self._tz_eastern)
        central_dt = utc_dt.astimezone(self._tz_central)
        mountain_dt = utc_dt.astimezone(self._tz_mountain)
        pacific_dt = utc_dt.astimezone(self._tz_pacific)
        berlin_dt = utc_dt.astimezone(self._tz_berlin)
        london_dt = utc_dt.astimezone(self._tz_london)
        paris_dt = utc_dt.astimezone(self._tz_paris)
        self._utc_label.setText(utc_dt.strftime(self._clock_fmt))
        self._eastern_label.setText(eastern_dt.strftime(self._clock_fmt))
        self._central_label.setText(central_dt.strftime(self._clock_fmt))
        self._mountain_label.setText(mountain_dt.strftime(self._clock_fmt))
        self._pacific_label.setText(pacific_dt.strftime(self._clock_fmt))
        self._berlin_label.setText(berlin_dt.strftime(self._clock_fmt))
        self._london_label.setText(london_dt.strftime(self._clock_fmt))
        self._paris_label.setText(paris_dt.strftime(self._clock_fmt))
    
    def execute(self):
        app = QApplication([])
        tab1 = 20
        tab2 = 110
        yStart = 10
        yInc = 20
        w = QWidget()
        w.setGeometry(100, 100, 320, 240)
        w.setWindowTitle('World Clock')
        self._utc_label = self._create_label(w, 'UTC:', yStart, tab1, tab2)
        self._eastern_label = self._create_label(w, 'US/Eastern:', yStart + yInc * 2, tab1, tab2)
        self._central_label = self._create_label(w, 'US/Central:', yStart + yInc * 3, tab1, tab2)
        self._mountain_label = self._create_label(w, 'US/Mountain:', yStart + yInc * 4, tab1, tab2)
        self._pacific_label = self._create_label(w, 'US/Pacific:', yStart + yInc * 5, tab1, tab2)
        self._berlin_label = self._create_label(w, 'Berlin:', yStart + yInc * 7, tab1, tab2)
        self._london_label = self._create_label(w, 'London:', yStart + yInc * 8, tab1, tab2)
        self._paris_label = self._create_label(w, 'Paris:', yStart + yInc * 9, tab1, tab2)
        w.show()
        self._timer.start(1000)
        exit(app.exec())


if __name__ == '__main__':
    app = Application()
    app.execute()
