#-----------------------------------------------------------------------------
# NimBLE Tx Power Service
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

ADD_DEFINITIONS(-DBLE_SVC_TPS_SYSINIT_STAGE=303)

build_component_from (
  src/ble_svc_tps.c
)
