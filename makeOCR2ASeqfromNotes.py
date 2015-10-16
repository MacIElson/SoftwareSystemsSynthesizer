"""
notetoocr0a.py
-----
Written by team c-slugs for softsys Fall 2015

Conversion script that allows mapping a list of note names
to a list of OCR2A settings to be inputted to the Arduino synthesizer
"""

# Range D2#-C7# (77.8 - 2217.5), OCR0A Range 78 - 2222 (Rounded)
# F6# begins mapping to same freq - top of effective range
test_seq = ["A4", "B4", "C4"]

test_song1 = {
  "notes": [("C4",1.0),("C4#",1.0),("D4",1.0),("D4#",1.0),("E4",1.0),("F4",1.0),("F4#",1.0),("G4",1.0),("G4#",1.0),("A4",1.0),("A4#",1.0),("B4",1.0)],
  "tempo": 1000 #ms
  }

fzero = {
  "notes": [
    ("F5", 1.5), ("E5b", 1.5), ("D5", 1),  # 17
    ("C5", 1.5), ("D5", 1.5), ("E5b", 1),  # 18
    ("F5", 1.5), ("E5b", 1.5), ("D5", 1),  # 19
    ("C5", 2), ("silent", 1),  # 20 (to beat 3)
    ("C5", .25), ("D5", .25), ("E5b", .25), ("F5", .25),  # 20
    ("G5", 1.5), ("F5", 1.5), ("B5b", 1),  # 21
    ("A5b", 1.5), ("G5", 1.5), ("F5", 1),  # 22
    ("G5", 1.5), ("F5", 1.5), ("E5b", 1),  # 23
    ("D5", 1.5), ("C5", 1.5), ("B4b", 1),  # 24
    ("F5", 1.5), ("E5b", 1.5), ("D5", 1),  # 25
    ("C5", 1.5), ("D5", 1.5), ("E5b", 1),  # 26
    ("F5", 1.5), ("E5b", 1.5), ("D5", 1),  # 27
    ("C5", 2), ("silent", 1),  # 28 (to beat 3)
    ("C5", .25), ("D5", .25), ("E5b", .25), ("F5", .25),  # 28
    ("G5", 1.5), ("F5", 1.5), ("B5b", 1),  # 29
    ("A5b", 1.5), ("G5", 1.5), ("F5", 1),  # 30
    ("G5", 1.5), ("F5", 1.5), ("E5b", 1),  # 31
    ("D5", 1.5), ("C5", 1.5), ("B4b", 1),  # 32
    ("A4", 1), ("silent", 1.5), ("G4", .25), ("A4", .25), ("B4b", .25),  # 33
    ("C5", 1), ("silent", 1.5), ("G4", .25), ("A4", .25), ("B4b", .25),  # 34
    ("D5", 1), ("silent", 1.5), ("G4#", .25), ("B4b", .25), ("D5", .25),  # 35
    ("E5b", 1), ("silent", 1.5), ("G4#", .25), ("D5b", .25), ("E5b", .25),  # 36
    ("F5", 1), ("silent", 1.5), ("A2b", .25), ("C3#", .25), ("D3#", .25),  # 37
    ("F3", 1), ("silent", 1.5), ("D4b", .25), ("F4", .25), ("A4b", .25),  # 38
    ("D5b", 1), ("silent", 1.5), ("F4", .25), ("A4b", .25), ("D5b", .25),  # 39
    ("F5", 1), ("silent", 1.5), ("A4b", .25), ("D5b", .25), ("F5", .25),  # 40
    ("G5b", .666), ("F5", .666), ("E5b", .666), ("D5b", .666), ("C5", .666), ("D5b", .666),  # 41
    ("E5b", .666), ("D5b", .666), ("B4", .666), ("B4b", .666), ("A4b", .666), ("G4b", .666),  # 42
    ("E4b", .666),  ("F4", .666), ("G4b", .666), ("E4b", .666),  ("G4b", .666),  ("B4b", .666),  # 43
    ("E5b", 4),  # 44
    ("silent", 2), ("E5b", .25), ("D5", .25), ("D5b", .25), ("C5", .25),  # 45 (to beat 3)
    ("B4", .25), ("B4b", .25), ("A4", .25), ("A4b", .25)
  ],
  "tempo": 312  # ~ 193 BPM
}

mario_song = []

# Constant Declarations
CLOCK_FREQ = 16000000
PRESCALER = 8
TIMER_FREQ = CLOCK_FREQ / PRESCALER
LOOKUPS = 100

# Map from Notes to Frequencies
note_map = {
  "silent": 0,
  "A2b": 103.83,
  "A2" : 110.00,
  "A2#": 116.54,
  "B2b": 116.54,
  "B2" : 123.47,

  "C3" : 130.81,
  "C3#": 138.59,
  "D3b": 138.59,
  "D3" : 146.83,
  "D3#": 155.56,
  "E3b": 155.56,
  "E3" : 164.81,
  "F3" : 174.61,
  "F3#": 185.00,
  "G3b": 185.00,
  "G3" : 196.00,
  "G3#": 207.65,
  "A3b": 207.65,
	"A3" : 220.00,
  "A3#": 233.08, 
  "B3b": 233.08,
  "B3" : 246.94,
  
  "C4" : 261.33,
  "C4#": 277.18,
  "D4b": 277.18,
  "D4" : 293.66,
  "D4#": 311.13,
  "E4b": 311.13,
  "E4" : 329.66,
  "F4" : 349.23,
  "F4#": 369.99,
  "G4b": 369.99,
  "G4" : 392.00,
  "G4#": 415.30,
  "A4b": 415.30,
	"A4" : 440.00,
  "A4#": 466.16, 
  "B4b": 466.16,
  "B4" : 493.88,

  "C5" : 523.25,
  "C5#": 554.37,
  "D5b": 554.37,
  "D5" : 587.33,
  "D5#": 622.25,
  "E5b": 622.25,
  "E5" : 659.25,
  "F5" : 698.46,
  "F5#": 739.99,
  "G5b": 739.99,
  "G5" : 783.99,
  "G5#": 830.61,
  "A5b": 830.61,
  "A5" : 880.00,
  "A5#": 932.33,
  "B5b": 932.33,
  "B5" : 987.77,
  
  "C6" : 1046.5,
  "C6#": 1108.7,
  "D6b": 1108.7,
  "D6" : 1174.7,
  "D6#": 1244.5,
  "E6b": 1244.5,
  "E6" : 1318.5,
  "F6" : 1386.9,
  "F6#": 1480.0,
  "G6b": 1480.0
}


def freqToOCR2A(desired_freq):
	""" Maps from a sound frequency to a comparison register setting """
	desired_interrupt_freq = LOOKUPS * desired_freq
	return (TIMER_FREQ / desired_interrupt_freq) - 1
  
def noteToOCR2A(note):
	""" Maps from a note's name to a comparison register setting """
	return int(round(freqToOCR2A(note_map[note])))

def noteSeqToOCR2ASeq(song):
	""" Maps from a list of note names to a list of comparison register settings """
	return [ 256 if (note[0] == "silent") else noteToOCR2A(note[0]) for note in song["notes"]]

def noteDurations(song):
	""" Maps from a list of relative note lengths to a list of note lengths in milliseconds"""
  	return [int(round(note[1] * song["tempo"])) for note in song["notes"]]

if __name__ == "__main__":
  print "int notes[] = {" + ",".join(str(x) for x in noteSeqToOCR2ASeq(fzero)) + "};"
  print "int durations[] = {" + ",".join(str(x) for x in noteDurations(fzero)) + "};"