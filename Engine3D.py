from gl import Renderer, color, V3, V2

width = 960
height = 540

rend = Renderer(width, height)

rend.glLoadModel("mariohead.obj",
                 translate = V3(width/2, height/2, 0),
                 scale = V3(50,50,50))

rend.glFinish("output.bmp")