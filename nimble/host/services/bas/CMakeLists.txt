#-----------------------------------------------------------------------------
# NimBLE Battery Service
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

ADD_DEFINITIONS(-DBLE_SVC_BAS_BATTERY_LEVEL_READ_PERM=0)
ADD_DEFINITIONS(-DBLE_SVC_BAS_BATTERY_LEVEL_NOTIFY_ENABLE=1)
ADD_DEFINITIONS(-DBLE_SVC_BAS_SYSINIT_STAGE=303)

build_component_from (
  src/ble_svc_bas.c
)
