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
  ADD_DEFINITIONS (-DENABLE_TRACE=1)
ENDIF ()

find_subprojects (SUBPROJECTS docs porting)

#------------------------------------------------------------------------------
# Disable many warnings while building Nordic Semi code
#------------------------------------------------------------------------------
MACRO (newt_no_warnings)
  ADD_DEFINITIONS (-Wno-documentation)
  ADD_DEFINITIONS (-Wno-documentation-unknown-command)
  ADD_DEFINITIONS (-Wno-sign-conversion)
  ADD_DEFINITIONS (-Wno-implicit-int-conversion)
  ADD_DEFINITIONS (-Wno-missing-prototypes)
  ADD_DEFINITIONS (-Wno-vla)
  ADD_DEFINITIONS (-Wno-unused-parameter)
  ADD_DEFINITIONS (-Wno-zero-length-array)
  ADD_DEFINITIONS (-Wno-cast-align)  # BEWARE !!
  ADD_DEFINITIONS (-Wno-packed)
  ADD_DEFINITIONS (-Wno-conditional-uninitialized)
  ADD_DEFINITIONS (-Wno-unreachable-code)
  ADD_DEFINITIONS (-Wno-shadow)
  ADD_DEFINITIONS (-Wno-variadic-macros)
  ADD_DEFINITIONS (-Wno-missing-noreturn)
  ADD_DEFINITIONS (-Wno-sign-compare)
  ADD_DEFINITIONS (-Wno-unreachable-code-return)
  ADD_DEFINITIONS (-Wno-macro-redefined)
  ADD_DEFINITIONS (-Wno-pointer-sign)
  ADD_DEFINITIONS (-Wno-pointer-arith)
  ADD_DEFINITIONS (-Wno-float-conversion)
  ADD_DEFINITIONS (-Wno-shorten-64-to-32)
  ADD_DEFINITIONS (-Wno-bad-function-cast)
  ADD_DEFINITIONS (-Wno-format)
  ADD_DEFINITIONS (-Wno-switch-enum)
  ADD_DEFINITIONS (-Wno-uninitialized)
  ADD_DEFINITIONS (-Wno-unused-variable)
  ADD_DEFINITIONS (-Wno-missing-field-initializers)
  ADD_DEFINITIONS (-Wno-char-subscripts)
ENDMACRO ()

# + invalid use of __...H__

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
  ADD_DEFINITIONS (-DNRF52 -DOS_CPUTIME_FREQ=32768)
  INCLUDE_DIRECTORIES(${CMAKE_SOURCE_DIR}/core/hw/nrfx
                      ${CMAKE_SOURCE_DIR}/core/hw/nrfx/mdk
                      ${CMAKE_SOURCE_DIR}/core/hw/cmsis-core/src/ext)
ENDMACRO()

#------------------------------------------------------------------------------
# Select nrf52840 target
#------------------------------------------------------------------------------
MACRO (use_nrf52840)
ENDMACRO()

#------------------------------------------------------------------------------
# Build configuration
#------------------------------------------------------------------------------

use_sdk_headers (
  core/encoding/base64
  core/kernel/os
  core/hw/bsp/nordic_pca10040
  core/hw/hal
  core/hw/mcu
  core/hw/mcu/nrf52xxx
  core/sys/config
  core/sys/defs
  core/sys/log/common
  core/sys/log/modlog
  core/sys/log/stub
  core/sys/stats
  core/sys/sys
  core/sys/sysdown
  core/sys/sysinit
  core/sys/console/stub
  core/util/mem
  nimble/common
  nimble/drivers/nrf52
  nimble/controller
  nimble/host
  porting/npl/mynewt
  ext/tinycrypt)

use_nrf52832 ()


ADD_DEFINITIONS(-DMYNEWT=1 -DFORCE_MYNEWT=1)

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
