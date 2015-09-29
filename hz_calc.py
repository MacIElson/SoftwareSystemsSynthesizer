CLOCK_FREQ = 16000000
PRESCALER = 8
OCR0A = 252
LOOKUPS = 100

# What freq should the arduino be outputting based on current settings
timer_freq = CLOCK_FREQ / PRESCALER
interrupt_frequency = timer_freq / (OCR0A + 1)
sound_frequency = interrupt_frequency / LOOKUPS

print("Sound frequency: " + str(sound_frequency))


# # How should we set
# DESIRED_SOUND_FREQ = 200
# desired_interrupt_freq = LOOKUPS * sound_frequency
# desired_OCR0A = (timer_freq / desired_interrupt_freq) - 1

# print("OCR0A setting: " + str(desired_OCR0A))

TIMER_FREQ = 2000000
LOOKUPS = 100
desired_freq = 200

desired_interrupt_freq = LOOKUPS * desired_freq
desired_OCR0A = (TIMER_FREQ / desired_interrupt_freq) - 1
print(desired_OCR0A)