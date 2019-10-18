#-----------------------------------------------------------------------------
# NimBLE drivers
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

# define subprojects
find_subprojects (subprojects native nrf52)

#-----------------------------------------------------------------------------
# Build configuration
#-----------------------------------------------------------------------------

newt_no_warnings ()

# build all projects
FOREACH (project ${subprojects})
  ADD_SUBDIRECTORY (${project} ${project})
ENDFOREACH ()
