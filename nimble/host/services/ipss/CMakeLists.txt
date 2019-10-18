#-----------------------------------------------------------------------------
# NimBLE service Alert Notification Service Server
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

ADD_DEFINITIONS (-DBLE_SVC_IPSS_SYSINIT_STAGE=303)

build_component_from (
  src/ble_svc_ipss.c
)
