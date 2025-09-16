#refactoring the old code in just a few lines
from classes.entities.Tile import Tile
from classes.entities.Screen import Screen

hitbox_active = True
hitbox_visible = False
LOGICAL_W, LOGICAL_H = 1280, 720

#base + overlay mapping
tile_mapping = {"S": {"base": "assets/Tiles/sand.png", "overlay": None, "hitbox": None},
                "M": {"base": "assets/Tiles/sand.png", "overlay": "assets/Tiles/mountain.png",
                      "hitbox": {"x": 0, "y": 0, "width": 50, "height": 50}},
                "P": {"base": "assets/Tiles/sand.png", "overlay": "assets/Tiles/mountainPeak.png",
                      "hitbox": {"x": 0, "y": 0, "width": 50, "height": 50}}
                }

layouts = {
    "screen1": [
        "PPPPPPPPPPPPPPPP",
        "MMMMMMMMMMMMMMMM",
        "SSSSSSSSSSSSSSSS",
        "SSSSSSSSSSSSSSSS",
        "SSSSSSSSSSSSSSSS",
        "SSSSSSSSSSSSSSSS",
        "SSSSSSSSSSSSSSSS",
        "SSSSSSSSSSSSSSSS",
        "SSSSSSSSSSSSSSSS",
    ],
    "screen2": [
        "PPPPPPPPPPPPPPPP",
        "MMMMMMMMMMMMMMMM",
        "SSSMMMSSSSMSSSSS",
        "MMSSSSMSSSSMMSSS",
        "SMSMMSSSSSSMSSSS",
        "SSSSSSSSMSSSSSSS",
        "SSSSSSMSSSSSSSSS",
        "SMSSSMMSSMSSSSSS",
        "MSSSSSSSSSSSMSSS",
    ]
    #can add more screens for layouts as needed
}

screens = []

for screen_name, layout in layouts.items():
    tiles = [] #making tiles for every screen
    for row in layout:
        for cell in row:
            ''' only for debugging
            if cell.upper() not in tile_mapping:
                print(f"Unknown tile '{cell}' in {screen_name}, row {row_idx+1}, col {col_idx+1}, ord={ord(cell)}")
                raise ValueError(f"Unknown tile character: {cell}") 
            '''
            mapping = tile_mapping[cell]
            
            if mapping["hitbox"] is not None:
                hitbox_active = True
                hitbox = mapping["hitbox"]
            else:
                hitbox_active = False # for sand tiles
                hitbox = {"x": 0, "y": 0, "width": 0, "height": 0}
            tiles.append(
                Tile(
                    mapping["base"],
                    mapping["overlay"],
                    hitbox_active,
                    hitbox, #collision hitbox
                    {"x": 0, "y": 0, "width": 1, "height": 1}, #dev hitbox
                    hitbox_visible
                )
            )
    screens.append(Screen(LOGICAL_W, LOGICAL_H, len(layout[0]), len(layout), tiles))
