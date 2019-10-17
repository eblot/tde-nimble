#-----------------------------------------------------------------------------
# NimBLE drivers
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

# define subprojects
find_subprojects (SUBPROJECTS native)

#-----------------------------------------------------------------------------
# Build configuration
#-----------------------------------------------------------------------------

nrf52_no_warnings ()

# build all projects
FOREACH (project ${subprojects})
  ADD_SUBDIRECTORY (${project} ${project})
ENDFOREACH ()
