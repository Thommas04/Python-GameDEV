from ursina import *from ursina.raycaster import raycastfrom functions import *from random import *app = Ursina()EditorCamera()development_mode = Falseclass Enemy(Entity):    def __init__(self, x, y, cimke, vezerles, szin, **kwargs):        super().__init__(self, **kwargs)        self.cimke = cimke        self.vezerles = vezerles        self.ugras = False        self.ugras_szabad = True        self.talajon_van = False        self.x = x # x pozíció        self.y = y # y pozíció        self.model = 'cube'        self.color = szin        self.scale = (1, 2, 0)        self.world_position = (self.x, self.y, 0)        self.rotation = (0, 0, 0)        self.right_collision = Entity(model = 'plane',color = color.blue, rotation = (90,0,0), collider = 'box', parent = self, visible = False,                                      scale = (0.1, 1, -1),                                      world_position = (self.x + 0.5, self.y, 0))        self.left_collision = Entity(model='plane', color=color.blue, rotation=(90, 0, 0), collider='box', parent = self,visible = False,                                     scale=(0.1, 1, -1),                                     world_position=(self.x - 0.5, self.y, 0))        self.upper_collision = Entity(model='plane', color=color.violet, rotation=(90, 0, 0), collider='box', parent = self, tag = 'talaj',visible = False,                                      scale=(1, 0, -0.1),                                      world_position=(self.x, self.y + 1, 0))        self.lower_collision = Entity(model='plane',color=color.violet, rotation=(90, 0, 0), collider='box', parent = self,visible = False,                                      scale=(1, 0, -0.1),                                      world_position=(self.x, self.y - 1, 0))        self.collision_list = [self.right_collision, self.left_collision, self.lower_collision, self.upper_collision]    #[]------------------------------------------------[]jatekos1 = Enemy(3, 0, 'p1','wasd', color.red)jatekos2 = Enemy(1, 0, 'p2','nyilak', color.yellow)jatekosok = [jatekos1, jatekos2]#[]------------------------------------------------[]mozgas_sebesseg = 3#[]------------------------------------------------[]def jump_duration(jatekos):    if jatekos == jatekos1:        jatekos1.ugras = False    if jatekos == jatekos2:        jatekos2.ugras = Falsedef input(key):    if key == 'space' and jatekos1.talajon_van == True: #UGRÁS        jatekos1.ugras = True        jatekos1.talajon_van = False        invoke(jump_duration, jatekos1, delay = 0.75)    if key == 'up arrow' and jatekos2.talajon_van == True:        jatekos2.ugras = True        jatekos2.talajon_van = False        invoke(jump_duration, jatekos2, delay = 0.75)#[]------------------------------------------------[]def update():                 # Minden frame-ben lefut egyszer ( FPS )    print('2')    pl_x1 = jatekos1.world_position.x ; pl_x2 = jatekos2.world_position.x    pl_y1 = jatekos1.world_position.y ; pl_y2 = jatekos2.world_position.y    if pl_x1 >= pl_x2:          camera_target.world_position = [((pl_x1 + pl_x2) / 2),((pl_y1 + pl_y2) / 2),0]    else: camera_target.world_position = [((pl_x2 + pl_x1) / 2),((pl_y2 + pl_y1) / 2),0]    # -------------------------------------------------------------------------------------#    # -------------------------------------------------------------------------------------#    for player in jatekosok:        right_hit = player.right_collision.intersects(debug = False, ignore = player.collision_list )        left_hit = player.left_collision.intersects(debug = False, ignore = player.collision_list )        upper_hit = player.upper_collision.intersects(debug = False, ignore = player.collision_list )        lower_hit = player.lower_collision.intersects(debug = False, ignore = player.collision_list )        # -------------------------------------------------------------------------------------#        if player.vezerles == 'wasd':            if left_hit.hit == False:                player.x -= held_keys['a'] * time.dt * mozgas_sebesseg # delta time - legutolsó képfrissítés óta eltelt idő (1-20ms)            if right_hit.hit == False:                player.x += held_keys['d'] * time.dt * mozgas_sebesseg        if player.vezerles == 'nyilak':            if left_hit.hit == False:                player.x -= held_keys['left arrow'] * time.dt * mozgas_sebesseg            if right_hit.hit == False:                player.x += held_keys['right arrow'] * time.dt * mozgas_sebesseg        # -------------------------------------------------------------------------------------#        # -------------------------------------------------------------------------------------#        # -------------------------------------------------------------------------------------#        if lower_hit.hit == False and player.ugras == False: # zuhanás feltételei            player.position += player.down * 0.035        #-------------------------------------------------------------------------------------#        try:            if lower_hit.entity.tag == 'talaj': # ha talajt ért ugorhasson mégegyszer                player.talajon_van = True            else:                player.talajon_van = False        except: pass # NoneType object has no attribute 'tag'        # -------------------------------------------------------------------------------------#        if player.ugras == True and upper_hit.hit == False: # ugrás feltételei            player.position += player.up * 0.035#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]camera_target = Entity(model = 'cube', scale = (1,1,0), visible = False)camera.add_script(SmoothFollow(target = camera_target, offset=[0, 1, -50], speed = 4))talajzat = Entity(model='cube', collider='box', scale=(15,1,0), color = color.green, x = 0, y = -2, tag = 'talaj')app.run()