from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import *

width = 1208
height = 1208

rend = Renderer(width, height)

# rend.dirLight = V3(-1,0,0)

rend.background = Texture("models/tvbackground.bmp")
rend.glClearBackground()
# rend.active_texture = Texture("models/t0364_0.bmp")


rend.active_shader = greyscale
rend.glLoadModel("models/jerry.obj",
                 translate = V3(-2.7, -1, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,10,0))


rend.active_shader = toongreyscale
rend.glLoadModel("models/pikachu.obj",
                 translate = V3(2.5, -4.5, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))

rend.active_shader = heatmap
rend.glLoadModel("models/Mario.obj",
                 translate = V3(-2.7, -4.5, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))

rend.glLoadModel("models/vegeta.obj",
                 translate = V3(-3, 4.2, -10),
                 scale = V3(1.5,1.5,1.5),
                 rotate = V3(0,0,0))

rend.active_texture = Texture("models/seraphine.bmp")
rend.active_shader = randomstatic
rend.glLoadModel("models/garfield.obj",
                 translate = V3(2, 0.5, -10),
                 scale = V3(4,4,4),
                 rotate = V3(0,0,0))

rend.active_texture = Texture("models/seraphine.bmp")
rend.active_shader = pinkjelly
rend.glLoadModel("models/fallguy.obj",
                 translate = V3(2, -0.5, -10),
                 scale = V3(1.5,1.5,1.5),
                 rotate = V3(0,0,0))



rend.glFinish("output.bmp")

