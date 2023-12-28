import unreal

def get_selected_content_browser_assets():
    editor_utility = unreal.EditorUtilityLibrary()
    selected_assets = editor_utility.get_selected_assets()
    return selected_assets

def generate_new_name_for_asset(asset, rename_config):
    name = asset.get_name()
    asset_type = type(asset)

    for asset_class, prefix in rename_config.items():
        if isinstance(asset, asset_class) and not name.startswith(prefix):
            return prefix + name

    return name

def rename_assets(assets, rename_config):
    for asset in assets:
        old_name = asset.get_name()
        new_name = generate_new_name_for_asset(asset, rename_config)

        if new_name != old_name:
            asset_old_path = asset.get_path_name()
            asset_folder = unreal.Paths.get_path(asset_old_path)
            new_path = asset_folder + '/' + new_name

            if unreal.EditorAssetLibrary.rename_asset(asset_old_path, new_path):
                unreal.log(f'{old_name} successfully renamed to {new_name}')
            else:
                unreal.log_error(f'Could not rename {old_name}')

def run():
    rename_config = {
        unreal.MaterialInstance: 'MI_',
        unreal.Material: 'M_',
        unreal.Texture: 'T_',
        unreal.NiagaraSystem: 'NS_',
        unreal.ParticleSystem: 'C_'
    }

    selected_assets = get_selected_content_browser_assets()
    rename_assets(selected_assets, rename_config)

run()
