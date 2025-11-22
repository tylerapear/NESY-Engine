from src.classes.effects.Animation import Animation

player_animations = {
    "IdleUp": Animation("./src/assets/Sprites/Link/IdleUp", 10, 250, 250),
    "IdleDown": Animation("./src/assets/Sprites/Link/IdleDown", 10, 250, 250),
    "IdleLeft": Animation("./src/assets/Sprites/Link/IdleLeft", 10, 250, 250),
    "IdleRight": Animation("./src/assets/Sprites/Link/IdleRight", 10, 250, 250),
    "Up": Animation("./src/assets/Sprites/Link/Up", 50, 250, 250),
    "Down": Animation("./src/assets/Sprites/Link/Down", 50, 250, 250),
    "Left": Animation("./src/assets/Sprites/Link/Left", 50, 250, 250),
    "Right": Animation("./src/assets/Sprites/Link/Right", 50, 250, 250),
    "AttackUp": Animation("./src/assets/Sprites/Link/AttackUp", 10, 250, 250),
    "AttackDown": Animation("./src/assets/Sprites/Link/AttackDown", 10, 250, 250),
    "AttackLeft": Animation("./src/assets/Sprites/Link/AttackLeft", 10, 250, 250),
    "AttackRight": Animation("./src/assets/Sprites/Link/AttackRight", 10, 250, 250),
    "Death": Animation("./src/assets/Sprites/Link/Death", 50, 250, 250)
    
}

enemy_animation_template = {
    "Idle": Animation("./src/assets/Sprites/Enemies/ChuChu/Idle", 10, 100, 100),
    "Death": Animation("./src/assets/Sprites/Enemies/ChuChu/Death", 60, 100, 100),
}

enemy_animations = []

for _ in range(8):
    enemy_animations.append(
        {
            "Idle": Animation("./src/assets/Sprites/Enemies/ChuChu/Idle", 10, 100, 100),
            "Death": Animation("./src/assets/Sprites/Enemies/ChuChu/Death", 60, 100, 100),
        }
    )