from ursina import *
from panda3d.core import FrameBufferProperties
from panda3d.core import Camera
from panda3d.core import PerspectiveLens
import panda3d.core as p3d

window.borderless = False
window.size = (800, 600)

app = Ursina()

my_shader = Shader(
vertex="""
#version 150

// Uniform inputs
uniform mat4 p3d_ModelViewProjectionMatrix;

// Vertex inputs
in vec4 p3d_Vertex;
in vec2 p3d_MultiTexCoord0;

// Output to fragment shader
out vec2 texcoord;

void main() {
  gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
  texcoord = p3d_MultiTexCoord0;
}
""",
fragment="""
#version 150

uniform sampler2D p3d_Texture0;

uniform sampler2D depth;
uniform float near;
uniform float far;

// Input from vertex shader
in vec2 texcoord;

// Output to the screen
out vec4 p3d_FragColor;


// See https://learnopengl.com/Advanced-OpenGL/Depth-testing or other resource on this equation.
// It takes the depth and makes it linear between [near, far].
float linearize_depth(float depth) {
    float z = depth * 2.0 - 1.0;
    return (2.0 * near * far) / (far + near - z * (far - near));
}

void main() {
  float d = texture(depth, texcoord).r;
  d = linearize_depth(d) / far; // Divide by far for the visualization.
  // Set output color to depth.
  vec4 color = vec4(vec3(d), 1.0);
  p3d_FragColor = color;
}
""")

for i in range(10):
    box = Entity(model="cube", texture="white_cube", color=color.red, scale=3.0)
    box.x = 10.0 * math.cos(i / 10.0 * 2.0 * 3.14)
    box.z = 10.0 * math.sin(i / 10.0 * 2.0 * 3.14)
    box.scale_y = 3.0 + i
    box.y += i * 0.5
plane = Entity(model="plane", texture="white_cube", y=-1, scale=50, color=color.cyan)
screen = Entity(model="quad", parent=camera.ui, scale_x=0.3*window.aspect_ratio, scale_y=0.3, x=-0.4, y=0.3, shader=my_shader)
ed = EditorCamera()

# Make the camera far plane smaller to make this demo's depth more visible.
camera.lens.setNear(0.1)
camera.lens.setFar(1000.0)

# Creating the depth buffer and texutre.
props = FrameBufferProperties()
props.set_depth_bits(24)
tex = p3d.Texture()
tex.set_format(p3d.Texture.F_depth_component24)
tex.set_component_type(p3d.Texture.T_float)
depth_buffer = base.win.makeTextureBuffer("depth", 0, 0, tex, False, props)
depth_buffer.setSort(-100)

# A camera is needed to render into the texture buffer.
cam_np = base.makeCamera(depth_buffer, lens=camera.lens)
cam_np.reparentTo(scene)
# Optionally you can render this texture with a dsiplay region.
#dr = base.win.makeDisplayRegion()
#dr.setCamera(cam_np)

def update():
    # updating the camera so it matches the normal camera (normal camera is moved by EditorCamera).
    cam_np.setPos(camera.world_position)
    cam_np.look_at((0, 0, 0))
    # Set shader inputs.
    screen.set_shader_input("depth", tex)
    screen.set_shader_input("near", camera.lens.getNear())
    screen.set_shader_input("far", camera.lens.getFar())

app.run()