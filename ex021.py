import pygame
pygame.init()
pygame.mixer.init()

print("""Cheiro de pneu queimado e furado.
O X9 foi torrado, foi queimado.
Cheiro de carburador furado.
Eu quero contenção do lado.
Tira no miolo e tá destravado.

O X9 foi torrado, quero contenção do lado.
Cheiro de pneu queimado, de carburador furado.
Cheiro de carburador furado, cheiro de carburador queimado.
Tira no miolo e tá destravado.

Cheiro de pneu queimado, de carburador furado, o X9 foi torrado,\neu quero contenção do lado, tira no miolo e eu tá destravado.

Cheiro de pneu queimado, de carburador furado, o X9 foi torrado,\neu quero contenção do lado, tira no miolo e eu tá destravado. (Tira no miolo e eu tá destravado, tira no miolo e eu tá destravado)

O X9 foi torrado, quero contenção do lado.
Cheiro de pneu queimado, de carburador furado.

O X9 foi torrado, eu quero contenção do lado, e meus fuzis tá \ndestravado. Cheiro de carburador furado, cheiro de pneu queimado.

Cheiro de pneu queimado, de carburador furado, o X9 foi torrado, \neu quero contenção do lado, tem tira no miolo e eu tá destravado.

Cheiro de pneu queimado, de carburador furado, o X9 foi torrado, \neu quero contenção do lado, tem tira no miolo e eu tá destravado.

Queimado!
(Pneu queimado)
Torrado!
Tira no miolo e eu tá destravado.
Queimado!
(Pneu queimado)
Torrado!
Tira no miolo e eu tá destravado.

(Pneu queimado, pneu queimado, pneu queimado)
Torrado!""")

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
