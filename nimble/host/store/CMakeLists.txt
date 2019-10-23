#-----------------------------------------------------------------------------
# NimBLE host store
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

build_component_from (
  config/src/ble_store_config.c
  config/src/ble_store_config_conf.c
  ram/src/ble_store_ram.c
)
