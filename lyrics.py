# iTunes Lyrics by tranquility

import AZLyricsParser
import LetrasTerraParser
import MetrolyricsParser
import ChartlyricsParser
import LyricsmaniaParser
import LeoslyricsParser
import LyricwikiParser
from osascript import osascript

sites = [LyricwikiParser, LetrasTerraParser, MetrolyricsParser,
	AZLyricsParser, LyricsmaniaParser, ChartlyricsParser,
	LeoslyricsParser]

def fetch(source, artist, title):
	parser = sites[source].Parser(artist, title)
	try:
		lyrics = parser.parse()
	except Exception:
		return ""
	return lyrics

state = osascript('tell application "iTunes" to player state as string')
artist = osascript('tell application "iTunes" to artist of current track as string')
track = osascript('tell application "iTunes" to name of current track as string')

if state == "playing":
	for r in range(0, len(sites)):
		output = fetch(r, artist, track)
		if output != "": break
	print "%s - %s\n\n" % (track, artist)
	print output.encode('ascii', 'ignore')
