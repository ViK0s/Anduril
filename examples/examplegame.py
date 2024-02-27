import pyglet


import sys
sys.path.append("/Users/micha/Desktop/tofy-main/")

import tofy



class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.active = 1
    def on_draw(self):
        self.render()
    def render(self):
        self.clear()

        self.pre_render()

        playerobject.draw()
        #enemie1s.draw()
        batch.draw()
        self.flip()

    def run(self):
        while self.active == 1:
            self.render()

            # -----------> This is key <----------
            # This is what replaces pyglet.app.run()
            # but is required for the GUI to not freeze
            #
            event = self.dispatch_events()
            #self.push_handlers(playerobject.key_handler)
    def pre_render(self):
        pass  
    def on_close(self):
        pyglet.app.exit()
        self.active = 0
        self.close()






class Snake(tofy.entitytools.entity.Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def on_attack(self):
        print("the enemy is getting attacked")



class GamePlayer(tofy.entitytools.player.Player):
    def __init__(self, window, img, relativex, relativey, z, batch, group, tileset):
        super().__init__(window, img, relativex, relativey, z, batch, group, tileset)
    def on_key_press(self, symbol, modifiers):
        if symbol == self.key.SPACE and not self.detect_collision(1, 0, worldobject):
            print("im tha playa")
            #self.dispatch_event("on_attack")
            self.relativex += 1
            print(self.x)
            worldobject.checkFOV()

x = GameWindow()


tileimages = pyglet.resource.image("curses_800x600.png")



tilemap = tofy.tiletools.tilemap.Tilemap()
tilemap.create_from_img(tileimages, 16, 16)

#print(tilemap.tile_height, tilemap.tile_width)
foreground = pyglet.graphics.Group(order=1)
background = pyglet.graphics.Group(order=0)
batch = pyglet.graphics.Batch()

#testcollisiontile = tofy.tiletools.tile.Tile(tilemap.tilemap[5][5], 40, 40, 0.1, batch, foreground, True)


tilesetdef = tofy.tiletools.tileset.Tileset(20, 20, 10, 10, tilemap, batch, background, [4, 10])
esa = tilesetdef.createsquare(2, 2)


playerobject = GamePlayer(x, tilemap.tilemap[15][1], 1, 0, 0.1, batch, foreground, tilesetdef)
playerobject.create_new_topic("on_attack")


#print(playerobject.y)
#print(tilesetdef.tilelist[0][2].x, tilesetdef.tilelist[0][2].y)
#tilesetdef.tilelist[0][5].collidable = True

enemie1s = Snake(tilemap.tilemap[1][1], 3, 0, 0.1, batch, foreground, tilesetdef)
#enemie1s.listen_to_subject(playerobject)

worldobject = tofy.world.World([tilesetdef], playerobject, [enemie1s])
worldobject.checkFOV()


x.run()

