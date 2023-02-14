
character = Actor('character')
character.pos = 0, 10

WIDTH = 500
HEIGHT = character.height + 20


def draw():
    screen.clear()
    screen.fill((175, 50, 99))
    character.draw()

def update():
    character.left += 2
    if character.left > WIDTH:
        character.right = 0

def on_mouse_down(pos):
    if character.collidepoint(pos):
        set_character_clicked()

def set_character_clicked():
    character.image = 'character_clicked'
    sounds.sound.play()
    clock.schedule_unique(set_character, 1.0)

def set_character():
    character.image = 'character'







