#------------------------------------------------------------------------------
# Applications based on NimBLE for nRF52
#
# @file CMakeLists.txt
#------------------------------------------------------------------------------

# Import useful macros
CMAKE_MINIMUM_REQUIRED (VERSION 3.5)

PROJECT (nrf52 C ASM)

use_target ()
use_default_xcc_warnings ()
use_default_xcc_settings ()
use_default_xas_settings ()

#------------------------------------------------------------------------------
# CMake definitions
#------------------------------------------------------------------------------

# If trace probe mode is enable, force redirection of GPIO as trace probe
# outputs
IF (DEFINED TRACE_PROBE)
  # workaround stupid CMake bugged warning
  STRING (TOLOWER "${TRACE_PROBE}" _TRACE_PROBE)
  ADD_DEFINITIONS(-DENABLE_TRACE=1)
ENDIF ()

find_subprojects (SUBPROJECTS docs)

#------------------------------------------------------------------------------
# Disable many warnings while building Nordic Semi code
#------------------------------------------------------------------------------
MACRO (nrf52_no_warnings)
  ADD_DEFINITIONS(-Wno-documentation)
  ADD_DEFINITIONS(-Wno-documentation-unknown-command)
  ADD_DEFINITIONS(-Wno-sign-conversion)
  ADD_DEFINITIONS(-Wno-implicit-int-conversion)
  ADD_DEFINITIONS(-Wno-missing-prototypes)
  ADD_DEFINITIONS(-Wno-vla)
ENDMACRO ()

#------------------------------------------------------------------------------
# Select nRF5 SDK headers
#------------------------------------------------------------------------------
MACRO (use_sdk_headers)
  SET (inc_dirs)
  FOREACH (header ${ARGV})
    assert_directory ("Component" ${CMAKE_SOURCE_DIR}/${header}/include)
    LIST (APPEND inc_dirs ${CMAKE_SOURCE_DIR}/${header}/include)
  ENDFOREACH (header)
  INCLUDE_DIRECTORIES (${inc_dirs})
ENDMACRO ()

#------------------------------------------------------------------------------
# Select nrf52832 target
#------------------------------------------------------------------------------
MACRO (use_nrf52832)
ENDMACRO()

#------------------------------------------------------------------------------
# Select nrf52840 target
#------------------------------------------------------------------------------
MACRO (use_nrf52840)
ENDMACRO()

#------------------------------------------------------------------------------
# Build configuration
#------------------------------------------------------------------------------

use_sdk_headers(
  nimble/common
  porting/nimble
  porting/npl/dummy
)

SET (NIMBLE_SYSLIBS)
LIST (APPEND NIMBLE_SYSLIBS
      ans
      bas
      bleuart
      common
      controller
      dis
      gap
      gatt
      host
      ias
      ipss
      lls
      nimble
      nrf52
      ram
      store
      tinycrypt
      tps
      uart)

# build all projects
FOREACH (project ${SUBPROJECTS})
  ADD_SUBDIRECTORY (${project} ${project})
ENDFOREACH ()
