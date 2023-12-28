import unreal

def get_selected_content_browser_assets():
    editor_utility = unreal.EditorUtilityLibrary()
    selected_assets = editor_utility.get_selected_assets()

    return selected_assets

def generate_new_name_for_asset(asset):
    rename_config = {
        'prefix_per_type': [
            {'type': unreal.MaterialInstance, 'prefix': 'MI_'},
            {'type': unreal.Material, 'prefix': 'M_'},
            {'type': unreal.Texture, 'prefix': 'T_'},
            {'type': unreal.NiagaraSystem, 'prefix': 'NS_'},
            {'type': unreal.ParticleSystem, 'prefix': 'C_'}
        ]
    }

    name = asset.get_name()
    print(f'Asset {name} is a {type(asset)}')

    for i in range(len(rename_config['prefix_per_type'])):
        prefix_config = rename_config['prefix_per_type'][i]

        prefix = prefix_config['prefix']
        asset_type = prefix_config['type']

        if isinstance(asset, asset_type) and not name.startswith(prefix):
            return prefix + name

    return name

def rename_assets(assets):
    for i in range(len(assets)):
        asset = assets[i]

        old_name = asset.get_name()
        asset_old_path = asset.get_path_name()
        asset_folder = unreal.Paths.get_path(asset_old_path)

        new_name = generate_new_name_for_asset(asset)
        new_path = asset_folder + '/' + new_name
        print(f'{old_name} -> {new_name}')

        rename_success = unreal.EditorAssetLibrary.rename_asset(asset_old_path, new_path)
        if not rename_success:
            unreal.log_error('Could not rename:' + asset_old_path)

def run():
    selected_assets = get_selected_content_browser_assets()
    rename_assets(selected_assets)

run()