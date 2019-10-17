#-----------------------------------------------------------------------------
# NimBLE BLE uart service
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

ADD_DEFINITIONS(-DBLEUART_MAX_INPUT=120)
ADD_DEFINITIONS(-DBLEUART_SYSINIT_STAGE=500)

build_component_from (
  src/bleuart.c
)
