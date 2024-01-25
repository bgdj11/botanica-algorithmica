import pygame

pygame.init()
screen = pygame.display.set_mode((1362, 750)) 
pygame.display.set_caption('Botanica Algorithmica')

from Botanica import *

def save_plant_image():
    
    timestamp = int(time.time())
    image_name = f"../SavedPlants/screenshot_{timestamp}.png"

    plant_screen = pygame.Surface((2 * SCREEN_WIDTH // 3, SCREEN_HEIGHT))
    plant_screen.blit(screen, (0, 0), (SCREEN_WIDTH // 3, 0, 2 * SCREEN_WIDTH // 3, SCREEN_HEIGHT))
    
    pygame.image.save(plant_screen, image_name)

app = Botanica()
scale_factor = app._generate_plant()

running = True
need_redraw = True
current_time = 0

clock = pygame.time.Clock()
fps = 60

ui_surface = pygame.Surface((SCREEN_WIDTH // 3, SCREEN_HEIGHT))
app._render_ui(ui_surface) 

need_ui_update = False

while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if app.generate_button_rect.collidepoint(event.pos):
                scale_factor = app._generate_plant()
                need_ui_update = True
            elif app._handle_slider_events(event):  
                app._modify_plant()
                need_ui_update = True
            elif app._handle_growth_factor_slider_events(event): 
                need_ui_update = True
            elif app.random_leaf_button_rect.collidepoint(event.pos):
                app.leaf_shape = app.leaf_shape = random.choice(leaf_shapes)
            elif app.change_stem_color_button_rect.collidepoint(event.pos):
                app.color = pygame.Color(random.choice(app.colors))
            elif app.change_leaf_color_button_rect.collidepoint(event.pos):
                app.leaf_color = pygame.Color(random.choice(app.leaf_colors))
            elif app.save_button_rect.collidepoint(event.pos):
                save_plant_image()

        elif event.type == pygame.MOUSEBUTTONUP:
            app.dragging_slider = False
            app.dragging_growth_factor_slider = False
            need_ui_update = True

        elif event.type == pygame.MOUSEMOTION:
            if app.dragging_slider and app._handle_slider_events(event):
                app._modify_plant()
                need_ui_update = True
            if app.dragging_growth_factor_slider and app._handle_growth_factor_slider_events(event):
                need_ui_update = True

    # Iscrtavanje biljke u svakom frejmu
    screen.fill(pygame.Color('#000000'), (SCREEN_WIDTH // 3, 0, 2 * SCREEN_WIDTH // 3, SCREEN_HEIGHT))
    app._render(screen, scale_factor, current_time)

    if need_ui_update:
        # Azuriranje UI-a
        ui_surface.fill(pygame.Color('#000000'))
        app._render_ui(ui_surface)
        need_ui_update = False

    screen.blit(ui_surface, (0, 0))

    current_time += 1
    pygame.display.flip()

pygame.quit()