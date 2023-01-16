
from ursina import *
from pandas import DataFrame, read_excel, ExcelWriter
from openpyxl import load_workbook

def create_net():
    x = 0 ; y = 0
    for i in range(200):
        x += 1 ; y += 1
        line_x = Entity(model = Mesh (vertices = [Vec3(x, 0, 0), Vec3(x, 200, 0)], mode = 'line', thickness = 1), z = 0, color = color.orange)
        text_x = Text(parent = line_x, text = str(x), position = (x, 0, 0), scale = 10)
        line_y = Entity(model = Mesh (vertices = [Vec3(0, y, 0), Vec3(200, y, 0)], mode = 'line', thickness = 1), z = 0, color = color.orange)
        text_y = Text(parent=line_y, text = str(y), position = (0, y, 0), scale = 10)

    line_x = Entity(model = Mesh(vertices = [Vec3(0, 0, 0), Vec3(0, 200, 0)], mode = 'line', thickness = 3), z = -0.01, color = color.blue)
    line_y = Entity(model = Mesh(vertices = [Vec3(0, 0, 0), Vec3(200, 0, 0)], mode = 'line', thickness = 3), z = -0.01, color = color.blue)

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

def input(key):
    if key == 'left mouse down':
        try:
            print("(", floor(mouse.world_point.x),", ", floor(mouse.world_point.y),"),", sep = "")
            Text(parent = scene, world_position = (mouse.world_point.x, mouse.world_point.y, -0.001 ), scale = 10, text = str(floor(mouse.world_point.x)) + " / " + str(floor(mouse.world_point.y)))
            Entity(parent = scene, model = 'sphere', color = color.red, scale = 0.005, world_position = (mouse.world_point.x, mouse.world_point.y, 0 )  )
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

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
# Working with EXCEL Table

def new_excel(size_x, size_y):
    matrix_dict = {}
    matrix_list = []
    matrix_counter = 0

    for i in range(size_y):
        matrix_list.append('0')

    for i in range(size_x):
        matrix_dict['reserved_'+ str(matrix_counter)] = matrix_list
        matrix_dict['type_'+ str(matrix_counter)] = matrix_list
        matrix_dict['hp_'+ str(matrix_counter)] = matrix_list
        matrix_dict['arg1_' + str(matrix_counter)] = matrix_list
        matrix_dict['arg2_' + str(matrix_counter)] = matrix_list

        matrix_counter += 1

    data_frame = DataFrame(matrix_dict)

    return data_frame

def save_excel(data_frame, path, sheet):
    data_frame.to_excel(path, sheet_name = sheet, index = False)

# ----------------------------------------------------------------------------------------------------------------------

# Az excel fájlból beolvassa a mátrixba
def load_from_excel(data_frame, matrix, excel_path):
    print('indulamandula')
    for y in range(matrix.size_y):
        for x in range(matrix.size_x):

            matrix.matrix[y][x]['reserved'] = data_frame['reserved_' + str(x)][y]
            matrix.matrix[y][x]['type'] = data_frame['type_' + str(x)][y]
            matrix.matrix[y][x]['hp'] = data_frame['hp_' + str(x)][y]
            matrix.matrix[y][x]['arg1'] = data_frame['arg1_' + str(x)][y]
            matrix.matrix[y][x]['arg2'] = data_frame['arg2_' + str(x)][y]

# A mátrixból beolvassa az excel fájlba
def load_to_excel(data_frame, matrix, excel_path, sheet):
    print('indulacucc')
    for y in range(matrix.size_y):
        for x in range(matrix.size_x):

            data_frame['reserved_' + str(x)][y] = matrix.matrix[y][x]['reserved']
            data_frame['type_' + str(x)][y] = matrix.matrix[y][x]['type']
            data_frame['hp_' + str(x)][y] = matrix.matrix[y][x]['hp']
            data_frame['arg1_' + str(x)][y] = matrix.matrix[y][x]['arg1']
            data_frame['arg2_' + str(x)][y] = matrix.matrix[y][x]['arg2']

    data_frame.to_excel(excel_path, sheet_name = sheet, index = False)
