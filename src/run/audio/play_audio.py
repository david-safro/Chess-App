import pygame


def play_audio(choice):
    audio_choices = ["audio/capture.mp3", "audio/move-self.mp3"]
    pygame.mixer.init()
    pygame.mixer.music.load(audio_choices[choice])
    pygame.mixer.music.play()
