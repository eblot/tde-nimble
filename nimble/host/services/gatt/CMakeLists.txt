#-----------------------------------------------------------------------------
# NimBLE Generic Attribute profile service
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

ADD_DEFINITIONS (-DBLE_SVC_GATT_SYSINIT_STAGE=302)

build_component_from (
  src/ble_svc_gatt.c
)
