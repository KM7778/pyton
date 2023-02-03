import arcade as arc 
import random as rand


SCREEN_WIDTH = 660
SCREEN_HEIGHT = 660
SCREEN_TITLE = "Bomber man"
CELL_WIDTH = 60
CELL_HEIGHT = 60
ROW_COUNT = 11
COLUMN_COUNT = 11

def difference(coordinate,distance):
    return coordinate * distance + distance / 2

class ExplodableBlocks(arc.Sprite):
    def __init__(self):
        super().__init__("Bomberman/Blocks/ExplodableBlock.png",1)


class SolidBlocks(arc.Sprite):
    def __init__(self):
        super().__init__("Bomberman/Blocks/SolidBlock.png",1)

class Game(arc.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

        #textures
        self.bg = arc.load_texture("Bomberman/Blocks/BackgroundTile.png")

        #spritelists
        self.solid_blocks = arc.SpriteList()
        self.explodable_blocks = arc.SpriteList()
    
        #initilization sprites        
        self.setup()

    def draw_background(self):
        for y in range (ROW_COUNT):
            for x in range (COLUMN_COUNT):
                arc.draw_texture_rectangle(
                    difference(x,CELL_WIDTH),
                    difference(y,CELL_HEIGHT),
                    CELL_WIDTH , CELL_HEIGHT,self.bg)
        
        
    def update(self,delta_time):
        pass

    def on_draw(self):
        self.draw_background()
        self.solid_blocks.draw()
        self.explodable_blocks.draw()

    def setup(self):
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                if x % 2 == 1 and y % 2 == 1:
                    solid_block = SolidBlocks()
                    solid_block.center_x = difference(x,CELL_WIDTH)
                    solid_block.center_y = difference(y,CELL_HEIGHT)
                    self.solid_blocks.append(solid_block)
                elif rand.randint(1,2) == 1:
                    exp_block = ExplodableBlocks()
                    exp_block.center_x = difference(x,CELL_WIDTH)
                    exp_block.center_y = difference(y,CELL_HEIGHT)
                    self.explodable_blocks.append(exp_block)






window = Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
arc.run()