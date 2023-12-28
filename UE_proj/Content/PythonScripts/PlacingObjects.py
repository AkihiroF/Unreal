import unreal
import math

def spawn_cube(location = unreal.Vector(), rotation = unreal.Rotator()):
    editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    actor_class = unreal.StaticMeshActor

    static_mesh_actor = editor_actor_subs.spawn_actor_from_class(actor_class, location, rotation)

    static_mesh = unreal.EditorAssetLibrary.load_asset('/Engine/BasicShapes/Cube.Cube')
    static_mesh_actor.static_mesh_component.set_static_mesh(static_mesh)

    return static_mesh_actor
def run():
    cube_count = 30
    circle_radius = 1000.0
    circle_center = unreal.Vector(9.0, 0.8, 0.0)

    for i in range(cube_count):

        circle_x_location = circle_radius * math.cos(math.radians(i * 360 / cube_count))
        circle_y_location = circle_radius * math.sin(math.radians(i * 360 / cube_count))

        location = unreal.Vector(circle_x_location, circle_y_location, 0.0)
        location_to_circle_center = location - circle_center

        rotation = location_to_circle_center.quaternion().rotator()
        spawn_actor = spawn_cube(location, rotation)

run()