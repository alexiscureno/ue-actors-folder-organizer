import unreal

# class instances

editor_level_lib = unreal.EditorLevelLibrary()
editor_filter_lib = unreal.EditorFilterLibrary()

actors = editor_level_lib.get_all_level_actors()
static_meshes = editor_filter_lib.by_class(actors, unreal.StaticMeshActor)
reflection_cap = editor_filter_lib.by_class(actors, unreal.ReflectionCapture)
bp = editor_filter_lib.by_id_name(actors, "BP_")

moved_actors = 0

# dictionary of the folders names
folder_names = {
    "StaticMeshActors": static_meshes,
    "ReflectionCaptures": reflection_cap,
    "Blueprints": bp
}
for folder_name  in folder_names:
    for actor in folder_names[folder_name]:
        actor_name = actor.get_fname(folder_name)
        unreal.log("Moved actors {} into {}". format(actor_name, folder_name))

        moved_actors += 1
unreal.log("Moved actors {} into their folders")