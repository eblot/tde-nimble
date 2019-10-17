#-----------------------------------------------------------------------------
# NimBLE
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

ADD_DEFINITIONS(-DBLE_ROLE_CENTRAL=1)
ADD_DEFINITIONS(-DBLE_ROLE_PERIPHERAL=1)
ADD_DEFINITIONS(-DBLE_ROLE_BROADCASTER=1)
ADD_DEFINITIONS(-DBLE_ROLE_OBSERVER=1)
ADD_DEFINITIONS(-DBLE_MAX_CONNECTIONS=1)
ADD_DEFINITIONS(-DBLE_MAX_PERIODIC_SYNCS=1)
ADD_DEFINITIONS(-DBLE_WHITELIST=1)
ADD_DEFINITIONS(-DBLE_MULTI_ADV_INSTANCES=0)
ADD_DEFINITIONS(-DBLE_EXT_ADV=0)
ADD_DEFINITIONS(-DBLE_PERIODIC_ADV=0)
ADD_DEFINITIONS(-DBLE_EXT_ADV_MAX_SIZE=31)
ADD_DEFINITIONS(-DBLE_VERSION=50)

# define subprojects
find_subprojects (SUBPROJECTS include src)

#-----------------------------------------------------------------------------
# Build configuration
#-----------------------------------------------------------------------------

nrf52_no_warnings ()

# build all projects
FOREACH (project ${subprojects})
  ADD_SUBDIRECTORY (${project} ${project})
ENDFOREACH ()


build_component_from (
  src/ble_util.c
)
