import kivy
import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.checkbox import CheckBox
import getques
from getques import get_ques
import sys
kivy.require("1.11.1")