#-----------------------------------------------------------------------------
# NimBLE Link Loss Service
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

ADD_DEFINITIONS (-DBLE_SVC_IAS_SYSINIT_STAGE=303)

build_component_from (
  src/ble_svc_lls.c
)
