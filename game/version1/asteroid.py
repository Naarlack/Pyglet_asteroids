import pyglet
import random
import math
# from game import resources


def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


def asteroids(num_asteroids, player_position, batch=None):
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y, _ = player_position
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = pyglet.sprite.Sprite(
            img=asteroid_image, x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        asteroids.append(new_asteroid)
    return asteroids


def player_lives(num_icons, batch=None):
    player_lives = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=player_image,
                                          x=785-i*30, y=585, batch=batch)
        new_sprite.scale = 0.5
        new_sprite.rotation = -90
        player_lives.append(new_sprite)
    return player_lives


game_window = pyglet.window.Window(800, 600)

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="My Amazing Game",
                                x=game_window.width//2,
                                y=game_window.height//2,
                                anchor_x='center',
                                batch=main_batch)

player_image = pyglet.resource.image("player.png")
bullet_image = pyglet.resource.image("bullet.png")
asteroid_image = pyglet.resource.image("asteroid.png")

center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)

player_ship = pyglet.sprite.Sprite(
    img=player_image, x=400, y=300, batch=main_batch)

asteroids = asteroids(3, player_ship.position, main_batch)

player_lives = player_lives(3, main_batch)


@game_window.event
def on_draw():
    game_window.clear()

    main_batch.draw()

    # level_label.draw()
    # score_label.draw()
    # player_ship.draw()
    # for asteroid in asteroids:
    #     asteroid.draw()


if __name__ == '__main__':
    pyglet.app.run()
