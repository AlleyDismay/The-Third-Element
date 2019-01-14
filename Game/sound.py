# sound.py
# Paul Krishnamurthy 2015
# Plays sound effects

# The Third Element
# ICS3U Final Project

from pygame import *
from Game.const import *

class Sound(object):
	""" Play sound effects """

	def __init__(self):
		# All sound effects

		if not mac:
			self.coinCollected = mixer.Sound("sound/coinCollected.wav")

			# I was going to use dictionaries but it was too slow...

			self.themes = {
				"mainWorldFight" : "sound/mainWorldFight.ogg",
				"mainWorldTheme" : "sound/mainWorldTheme.ogg",
				"waterWorldTheme" : "sound/waterWorld.ogg",
				"shopTheme" : "sound/shop.ogg",
				"fireWorldTheme" : "sound/fireWorld.ogg",
				"conclusion" : "sound/conclusion.ogg",
				"introTheme" : "sound/introTheme.ogg",
				"churchTheme" : "sound/church.ogg",
				"castleTheme" : "sound/castle.ogg",
				"finalTempleTheme" : "sound/temple.ogg"
			}

			# # Key -> scenename | value -> theme name
			# self.sceneData = {
			# 	"mainWorld" : "mainWorldTheme",
			# 	"mainWorldShop" : "shopTheme",
			# 	"waterWorldEnter" : "waterWorldTheme",
			# 	"waterWorld" : "waterWorldTheme",
			# 	"waterWorldRoom1" : "waterWorldTheme",
			# 	"waterWorldRoom2" : "waterWorldTheme",
			# 	"waterWorldRoom3" : "waterWorldTheme",
			# 	"waterWorldRoom4" : "waterWorldTheme",
			# 	"fireWorldEnter" : "fireWorldTheme",
			# 	"fireWorld" : "fireWorldTheme",
			# 	"fireWorldRoom1" : "fireWorldTheme",
			# 	"fireWorldRoom2" : "fireWorldTheme",
			# 	"church" : "churchTheme",
			# 	"ultimateShop" : "shopTheme",
			# 	"surpriseTemple" : "castleTheme",
			# 	"finalTemple" : "finalTempleTheme"
			# }

			# Set sound and theme volumes
			self.coinCollected.set_volume(.8)
			mixer.music.set_volume(.6)

	def getMusic(self, sound):
		""" Return music themes """
		return self.themes[sound]

	def stopSound(self, sound):
		""" Stops specific sound """
		self.sounds[sound].fadeout(500)

	def stopMusic(self):
		""" Stop mixer """
		mixer.music.fadeout(500)

	# def setVolume(self, amount):
	# 	""" Set volume """
	# 	mixer.music.set_volume(amount)