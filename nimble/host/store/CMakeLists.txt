#-----------------------------------------------------------------------------
# NimBLE host store
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

ADD_DEFINITIONS(-DBLE_STORE_CONFIG_PERSIST=1)
ADD_DEFINITIONS(-DBLE_STORE_SYSINIT_STAGE=500)
ADD_DEFINITIONS(-DBLE_STORE_RAM_SYSINIT_STAGE=500)

build_component_from (
  config/src/ble_store_config.c
  config/src/ble_store_config_conf.c
  ram/src/ble_store_ram.c
)
