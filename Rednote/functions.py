
from ursina import *

def create_net():
    x = -101 ; y = -101
    for i in range(200):
        x += 1 ; y += 1
        line_x = Entity(model = Mesh (vertices = [Vec3(x, -100, 0), Vec3(x, 100, 0)], mode = 'line', thickness = 1), z = -0.2, color = color.orange)
        text_x = Text(parent = line_x, text = str(x), position = (x, 0, 0), scale = 10)
        line_y = Entity(model = Mesh (vertices = [Vec3(-100, y, 0), Vec3(100, y, 0)], mode = 'line', thickness = 1), z = -0.2, color = color.orange)
        text_y = Text(parent=line_y, text = str(y), position = (0, y, 0), scale = 10)

    line_x = Entity(model = Mesh(vertices = [Vec3(0, -100, 0), Vec3(0, 100, 0)], mode = 'line', thickness = 3), z = -0.22, color = color.blue)
    line_y = Entity(model = Mesh(vertices = [Vec3(-100, 0, 0), Vec3(100, 0, 0)], mode = 'line', thickness = 3), z = -0.22, color = color.blue)

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]


def input(key):
    if key == 'left mouse down':
        try:
            print("(", round(mouse.world_point.x,2),", ", round(mouse.world_point.y,2) ,", ", 0 , "),", sep = "")
            Text(parent = scene, world_position = (mouse.world_point.x, mouse.world_point.y, -0.001 ), scale = 10, text = str(round(mouse.world_point.x,2)) + " / " + str(round(mouse.world_point.y,2)))
            Entity(parent = scene, model = 'sphere', color = color.red, scale = 0.1, world_position = (mouse.world_point.x, mouse.world_point.y, 0 )  )
        except: pass

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
# File line rewriter # Rewrites the selected line in the file < line starts with 1 >

def filewrite ( line : int , new_content : str , filename : str ) :
    try :
        with open ( filename , "r", encoding="utf-8") as file :
            lines = [ line.replace ( "\n" , "" ) for line in file.readlines ( ) ]
            length = len ( lines )
        if length == 0 :
            raise EOFError ( "Nothing in file." )
        if line > length :
            raise IndexError ( "Given row does not exitst." )
        for index , value in enumerate ( lines ) :
            if index == line - 1 :
                lines [ index ] = new_content
        with open ( filename , "w", encoding="utf-8" ) as file :
            for val in lines :
                file.write ( f"{ val }\n" )
    except ( FileNotFoundError , EOFError ) :
        with open ( filename , "w", encoding="utf-8" ) as  file :
            printed_line = 0
            while printed_line < line - 1 :
                file.write ( "\n" )
                printed_line += 1
            file.write ( new_content )
    except IndexError :
        with open ( filename , "w", encoding="utf-8" ) as file :
            for val in lines :
                file.write ( f"{ val }\n" )
            for rows in range ( line - length - 1 ) :
                file.write ( "\n" )
            file.write ( new_content )

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
# File READING # Returns the file lines in a list

def fileread ( filename : str ) -> list :
    try :
        with open ( filename , "r", encoding="utf-8" ) as file :
            return [ row.replace ( "\n" , "" ) for row in file.readlines ( ) ]
    except FileNotFoundError :
        return [ ]