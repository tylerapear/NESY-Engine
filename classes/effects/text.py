from classes.effects.TextSurface import TextSurface

def drawTextSurface(surface, textSurface):
  surface.blit(textSurface, (textSurface.x_position, textSurface.y_position))
  
textSurface = TextSurface()
textSurface.text_content = "YOU BUFFOON!"
textSurface.background_color = (15,15,15)
textSurface.x_position = 20
textSurface.y_position = 300
textSurface.width = 1240
textSurface.height = 200
textSurface.opacity = 230
textSurface.text_color = (255,255,255)
textSurface.font_size = 128
textSurface.horizontal_alignment = "center"
textSurface.font_weight = "bold"