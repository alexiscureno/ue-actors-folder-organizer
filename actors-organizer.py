import unreal

# Get all actors in the current level
editor_level_lib = unreal.EditorLevelLibrary()
editor_filter_lib = unreal.EditorFilterLibrary()

# Filter the actors by class and ID
actors = editor_level_lib.get_all_level_actors()
static_meshes = editor_filter_lib.by_class(actors, unreal.StaticMeshActor)
reflection_cap = editor_filter_lib.by_class(actors, unreal.ReflectionCapture)
lights = editor_filter_lib.by_class(actors, unreal.Light)
atmos = editor_filter_lib.by_class(actors, unreal.AtmosphericFog)
skylights = editor_filter_lib.by_class(actors, unreal.SkyLight)
player_start = editor_filter_lib.by_class(actors, unreal.PlayerStart)
cue = editor_filter_lib.by_class(actors, unreal.AmbientSound)
glb_pos_vol = editor_filter_lib.by_class(actors, unreal.PostProcessVolume)
bp = editor_filter_lib.by_id_name(actors, "BP_")

# Initialize a counter for moved actors
moved_actors = 0

# Create a dictionary with folders and their corresponding actors
folder_names = {
    "StaticMeshActors": static_meshes,
    "ReflectionCaptures": reflection_cap,
    "Blueprints": bp,
    "Lights": lights,
    "AtmosphericFogs": atmos,
    "SkyLights": skylights,
    "PlayerStarts": player_start,
    "StarterBackgroundCues": cue,
    "GlobalPostProcessVolumes": glb_pos_vol


}

# Loop through the dictionary and move each actor to its corresponding folder
for folder_name  in folder_names:
    for actor in folder_names[folder_name]:
        actor_name = actor.get_fname()
        actor.set_folder_path(folder_name)
        unreal.log("Moved actors {} into {}". format(actor_name, folder_name))

        moved_actors += 1
        # Output the number of actors that were moved
unreal.log("Moved {} actors into their folders".format(moved_actors))
