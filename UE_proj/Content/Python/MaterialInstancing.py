import unreal

def get_selected_browser_assets():
    # Получение выбранных активов из Content Browser
    editor_utility = unreal.EditorUtilityLibrary()
    return editor_utility.get_selected_assets()

def log_assets_type(assets):
    # Логирование типов активов
    for asset in assets:
        unreal.log(f'Asset {asset.get_name()} is a {type(asset)}')

def find_material_in_assets(assets):
    # Поиск материала среди активов
    return next((asset for asset in assets if isinstance(asset, unreal.Material)), None)

def find_textures2d_in_assets(assets):
    # Поиск текстур среди активов
    return [asset for asset in assets if isinstance(asset, unreal.Texture2D)]

def create_material_instance(parent_material, asset_path, new_asset_name):
    # Создание материального инстанса
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    material_factory = unreal.MaterialInstanceConstantFactoryNew()
    new_asset = asset_tools.create_asset(new_asset_name, asset_path, None, material_factory)
    unreal.MaterialEditingLibrary.set_material_instance_parent(new_asset, parent_material)
    return new_asset

# Оставшиеся функции без изменений

def run():
    unreal.log('Running create material instances script')
    selected_assets = get_selected_browser_assets()
    log_assets_type(selected_assets)

    material = find_material_in_assets(selected_assets)
    textures = find_textures2d_in_assets(selected_assets)

    if not material:
        unreal.log_error('No material selected')
        return

    if not textures:
        unreal.log_error('No textures selected')
        return

    unreal.log(f'Selected material: {material.get_name()}')
    unreal.log(f'{len(textures)} textures selected')

    material_instances = create_material_instances_variations(material, textures)

run()
