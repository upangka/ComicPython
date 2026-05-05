import os
print(__file__)
print(os.path.dirname(__file__))

GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGES_FOLDER = os.path.join(GAME_ROOT_FOLDER, 'images')

IMG_ROAD_FILE_PATH = os.path.join(IMAGES_FOLDER, 'Road.png')
IMG_PLAYER_FILE_PATH = os.path.join(IMAGES_FOLDER, 'Player.png')
IMG_ENEMY_FILE_PATH = os.path.join(IMAGES_FOLDER, 'Enemy.png')
IMG_ENEMY2_FILE_PATH = os.path.join(IMAGES_FOLDER, 'Enemy2.png')
IMG_ENEMY3_FILE_PATH = os.path.join(IMAGES_FOLDER, 'Enemy3.png')




if __name__ == '__main__':
    print(GAME_ROOT_FOLDER)
    print(IMAGES_FOLDER)
    """
    D:\Code\CommicPython\Github\ComicPython\src\game\crazydriver
    D:\Code\CommicPython\Github\ComicPython\src\game\crazydriver\images
    """
