__author__ = 'Kristy'

import bpy

class AddGameMasterOperator(bpy.types.Operator):
    """Add game master etc"""
    bl_idname="object.add_gamemaster"
    bl_label="Add Gamemaster"

    @classmethod
    def poll(cls, context):
        # TODO: Change polling for the fact that it doesn't already exist
        return context.active_object is not None

    def execute(self, context):
        from scripts.ema_blender.ema_bpy.bpy_add_game_objects import add_game_master
        add_game_master()
        return {'FINISHED'}


class AddCoilObjects(bpy.types.Operator):
    """Add game master etc"""
    bl_idname="object.add_coil_objects"
    bl_label="Add Coil Objects"

    @classmethod
    def poll(cls, context):
        # TODO: Change polling for the fact that it doesn't already exist
        return context.active_object is not None

    def execute(self, context):
        from scripts.ema_blender.ema_bpy.bpy_add_game_objects import spawn_hidden_coils
        from scripts.ema_blender.blender_shared_objects import ema_mesh_name_rule
        spawn_hidden_coils(ema_mesh_name_rule)
        return {'FINISHED'}


class AddInferredObjects(bpy.types.Operator):
    """Add objects that mirror/transform from other objects"""
    bl_idname="object.add_inferred_object"
    bl_label="Add Inferred Object"

    @classmethod
    def poll(cls, context):
        # TODO: Change polling for the fact that it doesn't already exist
        return context.active_object is not None

    def execute(self, context):
        from scripts.ema_blender.ema_bpy.bpy_add_game_objects import spawn_inferred_coil
        spawn_inferred_coil(context.scene.inferred_obj_name, *','.split(context.scene.inferred_obj_rule))
        return {'FINISHED'}


class LoadBasicGameAssets(bpy.types.Operator):
    bl_idname="object.load_basic_assets"
    bl_label="Load basic menu and status assets"

    @classmethod
    def poll(cls, context):
        # TODO: Change polling for the fact that it doesn't already exist
        return True

    def execute(self, context):
        from ematoblender.scripts.ema_blender.ema_bpy import bpy_import_assets as ia
        print('LOADING EXTERNALLY CONSTRUCTED ASSETS')
        #try:
        ia.add_statusbar_scene()    # add status bar and webcam image
        #except:
        #    print("Importing the statusbar failed")
        #try:
        ia.add_menu_scene()         # add the popup menu scene
        #except:
        #    print("Importing the menu scene failed")
        return {'FINISHED'}