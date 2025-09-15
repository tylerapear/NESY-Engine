from classes.entities.Tile import Tile

hitbox_active = True
hitbox_visible = False

layout = [
    "MSSSSSSSSSSSSSSSS",
    "MSSSSSSSSSSSSSSSS",
    "MSSSSSSSSSSSSSSSS",
    "MSSSSSSSSSSSSSSSS",
    "MSSSSSSSSSSSPPSSS",
    "MSSSSSSSSSSSMSSSS",
    "MSSSSSSSSSSSPMSSS",
    "MSSSSSSSSSSSSSSSS",
    "MPPPPPPPPPPPPPPPP",
]

tiles = []

#base layer along w overlay layer
tile_mapping = {
    "S" : ("./assets/Tiles/sand.png", None),
    "M" : ("./assets/Tiles/sand.png" ,"./assets/Tiles/mountain.png"),
    "P" : ("./assets/Tiles/sand.png", "./assets/Tiles/mountainPeak.png")
  }

#loop to generate the map
tiles = []

for row in layout:
    for cell in row:
        base, overlay = tile_mapping[cell]
        tiles.append(
            Tile(
                base,
                overlay,
                hitbox_active,
                {"x": 0, "y": 0, "width": 50, "height": 50},
                {"x": 0, "y": 0, "width": 1, "height": 1}, #placeholder hitbox
                hitbox_visible
            )
          )