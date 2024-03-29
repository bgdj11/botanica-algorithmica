import pygame
from PIL import Image

pygame.init()
screen = pygame.display.set_mode((1362, 750)) 
pygame.display.set_caption('Botanica Algorithmica')

from Botanica import *

def remove_black_background(surface, output_path):
    # Pretvaranje pygame Surface objekta u PIL Image
    image_string = pygame.image.tostring(surface, "RGBA")
    img = Image.frombytes("RGBA", surface.get_size(), image_string)

    datas = img.getdata()
    new_data = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            new_data.append((255, 255, 255, 0))  # Postavljanje crnih piksela (pozadine) na bezbojne
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")

def save_plant_image():
    timestamp = int(time.time())
    image_name_transparent = f"../SavedPlants/plant_{timestamp}.png"

    plant_screen = pygame.Surface((2 * SCREEN_WIDTH // 3, SCREEN_HEIGHT))
    plant_screen.blit(screen, (0, 0), (SCREEN_WIDTH // 3, 0, 2 * SCREEN_WIDTH // 3, SCREEN_HEIGHT))

    remove_black_background(plant_screen, image_name_transparent)

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
                app.generate_button_pressed = True
                need_ui_update = True
            elif app._handle_slider_events(event):  
                app._modify_plant()
                need_ui_update = True
            elif app._handle_growth_factor_slider_events(event): 
                need_ui_update = True
            elif app.random_leaf_button_rect.collidepoint(event.pos):
                app.leaf_shape = app.leaf_shape = random.choice(leaf_shapes)
                app.random_leaf_button_pressed = True
                need_ui_update = True
            elif app.change_stem_color_button_rect.collidepoint(event.pos):
                app.stem_colors_variated = app._get_color_variations(pygame.Color(random.choice(app.colors)))
                app.change_stem_color_button_pressed = True
                need_ui_update = True
            elif app.change_leaf_color_button_rect.collidepoint(event.pos):
                app._change_leaf_color()
                app.change_leaf_color_button_pressed = True
                need_ui_update = True
            elif app.save_button_rect.collidepoint(event.pos):
                save_plant_image()
                app.save_button_pressed = True
                need_ui_update = True
            elif app.change_fruit_flower_color_button_rect.collidepoint(event.pos):
                app.change_fruit_flower_color()
                app.change_fruit_flower_color_button_pressed = True
                need_ui_update = True

        elif event.type == pygame.MOUSEBUTTONUP:
            app.dragging_slider = False
            app.dragging_growth_factor_slider = False
            app.generate_button_pressed = False
            app.random_leaf_button_pressed = False
            app.change_stem_color_button_pressed = False
            app.change_leaf_color_button_pressed = False
            app.save_button_pressed = False
            app.change_fruit_flower_color_button_pressed = False
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