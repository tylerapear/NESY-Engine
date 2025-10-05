import pygame

class HUD:
    
    def __init__(self, player, screen_size, anchor="top-left", offset=(10,10)):
        self.player = player
        self.screen_size = screen_size
        self.anchor = anchor
        self.offset = offset

        #font setup
        self.font = pygame.font.Font(None, 24)
        self.bar_x = 30
        self.bar_y = 600

        #dragging variables
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

    def update(self, events, dt):
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                hud_rect = pygame.Rect(self.bar_x, self.bar_y - 20, 1225, 120)
                if hud_rect.collidepoint(e.pos):
                    self.dragging = True
                    self.offset_x = e.pos[0] - self.bar_x #calculating offset so that HUD doesn't
                    self.offset_y = e.pos[1] - self.bar_y #snap to mouse click

            elif e.type == pygame.MOUSEMOTION and self.dragging:
                    self.bar_x = e.pos[0] - self.offset_x
                    self.bar_y = e.pos[1] - self.offset_y
                
            elif e.type == pygame.MOUSEBUTTONUP:
                    self.dragging = False

    def draw(self, surface):
        #dyanamic coords
        bar_x = self.bar_x
        bar_y = self.bar_y

        #draggable zone for debugging
        #pygame.draw.rect(surface, (255, 255, 0), (self.bar_x, self.bar_y - 20, 1225, 120), 2)

        #bar config
        rec_width = 1225
        rec_height = 120
        padding = 20
        
        #gray bar bg
        bar_surf = pygame.Surface((rec_width, rec_height), pygame.SRCALPHA) #gray bar
        bar_surf.fill((50, 50, 50, 180)) 
        surface.blit(bar_surf, (bar_x, bar_y - 20))

        #anchor points
        gray_left   = bar_x
        gray_top    = bar_y - 20
        gray_center_x = gray_left + rec_width // 2
        gray_center_y = gray_top + rec_height // 2

        #health bar
        bar_width = 100
        bar_height = 20
        health_ratio = self.player.health / self.player.max_health
        current_bar_width = bar_width * health_ratio
        
        pygame.draw.rect(surface, (128, 128,128), 
                         (gray_left + padding, gray_top + padding, bar_width, bar_height))
        pygame.draw.rect(surface, (255, 0, 0), 
                         (gray_left + padding, gray_top + padding, current_bar_width, bar_height))

        hp_text = self.font.render(f"HP: {self.player.health}", True, (255, 255, 255))
        surface.blit(hp_text, (gray_left + padding, gray_top + padding + bar_height + 5))
        
        #WASD diamond
        key_size = 30
        gap = 5
        wasd_center = (gray_left + 250, gray_center_y)

        keys = { #left aligning keys relative to grey bar
            "W": (wasd_center[0] + 320, wasd_center[1] - (key_size + gap)),
            "A":(wasd_center[0] - (key_size + gap) +320, wasd_center[1]),
            "S": (wasd_center[0] + 320, wasd_center[1]),
            "D": (wasd_center[0] + (key_size + gap) + 320, wasd_center[1]),
        }

        for k, (kx, ky) in keys.items():
            rect = pygame.Rect(kx, ky, key_size, key_size)
            pygame.draw.rect(surface, (200, 200, 200), rect) #button box
            text = self.font.render(k, True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            surface.blit(text, text_rect)
    #320
        label_text = self.font.render("Movement Keys", True, (255, 255, 255))
        label_rect = label_text.get_rect(center=(wasd_center[0] + 340, wasd_center[1] - key_size - 20))
        surface.blit(label_text, label_rect)

        #j key
        #j_x = gray_center_x - 460 #right of WASD diamond
        #j_y = wasd_center[1]
        j_rect = pygame.Rect(wasd_center[0] + 120, wasd_center[1]-15, key_size, key_size)
        pygame.draw.rect(surface, (200, 200, 200), j_rect)
        j_text = self.font.render("J", True, (0, 0, 0))
        j_text_rect = j_text.get_rect(center=j_rect.center)
        surface.blit(j_text, j_text_rect)

        #j label
        j_label = self.font.render("Attack", True, (255, 255, 255))
        surface.blit(j_label, (j_rect.x, j_rect.y - 25))

        #print("drawing HUD", self.player.health)