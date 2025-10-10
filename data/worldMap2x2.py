#refactoring the old code in just a few lines
from classes.entities.Tile import Tile
from classes.entities.Screen import Screen
from classes.entities.WorldMap import WorldMap
from classes.entities.WanderingEnemy import WanderingEnemy

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

# formerly called "layouts"

def buildMap():

  screen_details = {
    "screen1": {
      "layout": [
        "MMMMMMMMMMMMMMMM",
        "MMMMSSSSSSSSSSSS",
        "MMMSSSSSSSSSSSSS",
        "MMSSSSSSSSSSSSSS",
        "MSSSSSSSSPSSSSSS",
        "MSSSSSSSSMPSSSSS",
        "MSSSSSSSSSSSSSSS",
        "MSSSSSSSSSSSSSSS",
        "MSSSSSSSSSSSSSSS",
      ],
      "creatures": [
        WanderingEnemy( 
          spritePath = './assets/Sprites/Enemies/ChuChu', 
          animationSpeed = 25, 
          width = 100, 
          height = 100,
          health = 30,
          x = 1000, 
          y = 500, 
          hitbox_offset_dimentions = {"x": 10, "y": 15, "width": 85, "height": 80}, 
          hitbox_visible = hitbox_visible 
        ),
        WanderingEnemy( 
          spritePath = './assets/Sprites/Enemies/ChuChu', 
          animationSpeed = 25, 
          width = 100, 
          height = 100,
          health = 30, 
          x = 800, 
          y = 200, 
          hitbox_offset_dimentions = {"x": 10, "y": 15, "width": 85, "height": 80}, 
          hitbox_visible = hitbox_visible 
        )
      ]
    },
    "screen2": {
      "layout": [
        "MMMMMMMMMMMMMMMM",
        "SSSSSSSSSSSSMMMM",
        "SSSSSSSSSSSSSSMM",
        "SSSSSSSSSSSSSSSM",
        "SSSSSSSSSSSSSSSM",
        "SSSSSSSPPPSSSSSM",
        "SSSSSSSSSSSSSSSM",
        "SSSSSSSSSSSSSSSM",
        "SSSSSSSSSSSSSSSM",
      ],
      "creatures": [
        WanderingEnemy( 
          spritePath = './assets/Sprites/Enemies/ChuChu', 
          animationSpeed = 25, 
          width = 100, 
          height = 100,
          health = 30, 
          x = 1000, 
          y = 400, 
          hitbox_offset_dimentions = {"x": 10, "y": 15, "width": 85, "height": 80}, 
          hitbox_visible = hitbox_visible 
        ),
        WanderingEnemy( 
          spritePath = './assets/Sprites/Enemies/ChuChu', 
          animationSpeed = 25, 
          width = 100, 
          height = 100,
          health = 30,
          x = 200, 
          y = 350, 
          hitbox_offset_dimentions = {"x": 10, "y": 15, "width": 85, "height": 80}, 
          hitbox_visible = hitbox_visible 
        )
      ]
    },
    "screen3": {
      "layout": [
        "MSSSSSSSSSSSSSSS",
        "MSSSSSSSSSSSSSSS",
        "MSSSSSSSSSSSSSSS",
        "MSSSSSSSSSPPSSSS",
        "MSSSSSSSSSSMSSSS",
        "MSSSSSSSSSPMSSSS",
        "MPPSSSSSSSSSSSSS",
        "MMMPSSSSSSSSSSSS",
        "MMMMPPPPPPPPPPPP",
      ],
      "creatures": [
        WanderingEnemy( 
          spritePath = './assets/Sprites/Enemies/ChuChu', 
          animationSpeed = 25, 
          width = 100, 
          height = 100,
          health = 30,
          x = 1000, 
          y = 350, 
          hitbox_offset_dimentions = {"x": 10, "y": 15, "width": 85, "height": 80}, 
          hitbox_visible = hitbox_visible 
        ),
        WanderingEnemy( 
          spritePath = './assets/Sprites/Enemies/ChuChu', 
          animationSpeed = 25, 
          width = 100, 
          height = 100,
          health = 30,
          x = 200, 
          y = 300, 
          hitbox_offset_dimentions = {"x": 10, "y": 15, "width": 85, "height": 80}, 
          hitbox_visible = hitbox_visible 
        )
      ]
    },
    "screen4": {
      "layout": [
        "SSSSSSSSSSSSSSSM",
        "SSSSSSSSSSSSSSSM",
        "SSSSSSSSSSSSSSSM",
        "SSSSSSSSSSSSSSSM",
        "SSSSSSSSSSSSSSPM",
        "SSSSSSSSSSSSSSMM",
        "SSSSSSSSSSSSSPMM",
        "SSSSSSSSSSSSPMMM",
        "PPPPPPPPPPPPMMMM",
      ],
      "creatures": [
        WanderingEnemy( 
          spritePath = './assets/Sprites/Enemies/ChuChu', 
          animationSpeed = 25, 
          width = 100, 
          height = 100,
          health = 30,
          x = 1000, 
          y = 150, 
          hitbox_offset_dimentions = {"x": 10, "y": 15, "width": 85, "height": 80}, 
          hitbox_visible = hitbox_visible 
        ),
        WanderingEnemy( 
          spritePath = './assets/Sprites/Enemies/ChuChu', 
          animationSpeed = 25, 
          width = 100, 
          height = 100,
          health = 30,
          x = 200, 
          y = 350, 
          hitbox_offset_dimentions = {"x": 10, "y": 15, "width": 85, "height": 80}, 
          hitbox_visible = hitbox_visible 
        )
      ]
    }
      #can add more screens for layouts as needed
  }

  screens = []

  for screen_name, screen in screen_details.items():
      tiles = [] #making tiles for every screen
      for row in screen["layout"]:
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
                      #hitbox, #collision hitbox
                      {"x": 0, "y": 0, "width": 1, "height": 1}, #dev hitbox
                      hitbox_visible
                  )
              )
      screens.append(Screen(LOGICAL_W, LOGICAL_H, len(screen["layout"][0]), len(screen["layout"]), tiles, screen["creatures"]))
  
  return WorldMap(2, 2, screens, 0)