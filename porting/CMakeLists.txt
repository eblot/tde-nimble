#-----------------------------------------------------------------------------
# NimBLE porting layer
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

# define subprojects
find_subprojects (SUBPROJECTS examples)

#-----------------------------------------------------------------------------
# Build configuration
#-----------------------------------------------------------------------------

nrf52_no_warnings ()

# build all projects
FOREACH (project ${subprojects})
  ADD_SUBDIRECTORY (${project} ${project})
ENDFOREACH ()
