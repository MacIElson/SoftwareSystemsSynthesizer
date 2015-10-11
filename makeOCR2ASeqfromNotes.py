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
test_seq1 = ["A4", "B4", "C4"]
mario_song = []

# Constant Declarations
CLOCK_FREQ = 16000000
PRESCALER = 8
TIMER_FREQ = CLOCK_FREQ / PRESCALER
LOOKUPS = 100

# Map from Notes to Frequencies
note_map = {
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
  "D6b": 1480.0
}


def freqToOCR2A(desired_freq):
	""" Maps from a sound frequency to a comparison register setting """
	desired_interrupt_freq = LOOKUPS * desired_freq
	return (TIMER_FREQ / desired_interrupt_freq) - 1
  
def noteToOCR2A(note):
	""" Maps from a note's name to a comparison register setting """
	return int(round(freqToOCR2A(note_map[note])))

def noteSeqToOCR2ASeq(sequence):
	""" Maps from a list of note names to a list of comparison register settings """
	return [noteToOCR2A(note) for note in sequence]

if __name__ == "__main__":
	print(noteSeqToOCR2ASeq(test_seq))