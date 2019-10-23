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

ADD_DEFINITIONS (-DOS_MAIN_TASK_PRIO=127)
ADD_DEFINITIONS (-DOS_MAIN_STACK_SIZE=1024)
ADD_DEFINITIONS (-DOS_CLI=0)
ADD_DEFINITIONS (-DOS_COREDUMP=0)
ADD_DEFINITIONS (-DOS_CRASH_RESTORE_REGS=0)
ADD_DEFINITIONS (-DOS_CRASH_LOG=0)
ADD_DEFINITIONS (-DOS_WATCHDOG_MONITOR=0)
ADD_DEFINITIONS (-DOS_EVENTQ_MONITOR=0)
ADD_DEFINITIONS (-DOS_SYSVIEW=0)
ADD_DEFINITIONS (-DOS_SCHEDULING=1)
ADD_DEFINITIONS (-DOS_CTX_SW_STACK_GUARD=4)
ADD_DEFINITIONS (-DOS_MEMPOOL_GUARD=0)
ADD_DEFINITIONS (-DOS_CPUTIME_FREQ=1000000)
ADD_DEFINITIONS (-DOS_CPUTIME_TIMER_NUM=0)
ADD_DEFINITIONS (-DSANITY_INTERVAL=15000)
ADD_DEFINITIONS (-DWATCHDOG_INTERVAL=30000)
ADD_DEFINITIONS (-DMSYS_1_BLOCK_COUNT=12)
ADD_DEFINITIONS (-DMSYS_1_BLOCK_SIZE=292)
ADD_DEFINITIONS (-DMSYS_1_SANITY_MIN_COUNT=0)
ADD_DEFINITIONS (-DMSYS_2_BLOCK_COUNT=0)
ADD_DEFINITIONS (-DMSYS_2_BLOCK_SIZE=0)
ADD_DEFINITIONS (-DMSYS_2_SANITY_MIN_COUNT=0)
ADD_DEFINITIONS (-DMSYS_SANITY_TIMEOUT=60000)
ADD_DEFINITIONS (-DFLOAT_USER=0)
ADD_DEFINITIONS (-DOS_SYSVIEW_TRACE_CALLOUT=0)
ADD_DEFINITIONS (-DOS_SYSVIEW_TRACE_EVENTQ=0)
ADD_DEFINITIONS (-DOS_SYSVIEW_TRACE_MBUF=0)
ADD_DEFINITIONS (-DOS_SYSVIEW_TRACE_MEMPOOL=0)
ADD_DEFINITIONS (-DOS_SYSVIEW_TRACE_MUTEX=0)
ADD_DEFINITIONS (-DOS_SYSVIEW_TRACE_SEM=0)
ADD_DEFINITIONS (-DOS_DEBUG_MODE=0)
ADD_DEFINITIONS (-DOS_IDLE_TICKLESS_MS_MIN=100)
ADD_DEFINITIONS (-DOS_IDLE_TICKLESS_MS_MAX=600000)
ADD_DEFINITIONS (-DOS_CRASH_FILE_LINE=0)
ADD_DEFINITIONS (-DOS_SYSINIT_STAGE=0)
ADD_DEFINITIONS (-DOS_ASSERT_CB=0)
ADD_DEFINITIONS (-DOS_MAIN_TASK_SANITY_ITVL_MS=0)

IF (CMAKE_BUILD_TYPE STREQUAL "DEBUG")
  ADD_DEFINITIONS (-DOS_CRASH_STACKTRACE=1)
  ADD_DEFINITIONS (-DOS_CTX_SW_STACK_CHECK=1)
  ADD_DEFINITIONS (-DOS_MEMPOOL_CHECK=1)
  ADD_DEFINITIONS (-DOS_MEMPOOL_POISON=1)
  ADD_DEFINITIONS (-DOS_TIME_DEBUG=1)
  ADD_DEFINITIONS (-DOS_EVENTQ_DEBUG=1)
ELSE ()
  ADD_DEFINITIONS (-DOS_CRASH_STACKTRACE=0)
  ADD_DEFINITIONS (-DOS_CTX_SW_STACK_CHECK=0)
  ADD_DEFINITIONS (-DOS_MEMPOOL_CHECK=0)
  ADD_DEFINITIONS (-DOS_MEMPOOL_POISON=0)
  ADD_DEFINITIONS (-DOS_TIME_DEBUG=0)
  ADD_DEFINITIONS (-DOS_EVENTQ_DEBUG=0)
ENDIF ()

ADD_DEFINITIONS (-DBLE_CONTROLLER=1)
ADD_DEFINITIONS (-DBLE_HW_WHITELIST_ENABLE=1)
ADD_DEFINITIONS (-DBLE_LL_SYSVIEW=0)
ADD_DEFINITIONS (-DBLE_LL_PRIO=0)
ADD_DEFINITIONS (-DBLE_LL_OUR_SCA=60)
ADD_DEFINITIONS (-DBLE_LL_MASTER_SCA=4)
ADD_DEFINITIONS (-DBLE_LL_TX_PWR_DBM=0)
ADD_DEFINITIONS (-DBLE_NUM_COMP_PKT_RATE="\(2 * OS_TICKS_PER_SEC\)")
ADD_DEFINITIONS (-DBLE_LL_MFRG_ID=0xFFFF)
ADD_DEFINITIONS (-DBLE_LL_NUM_SCAN_DUP_ADVS=8)
ADD_DEFINITIONS (-DBLE_LL_NUM_SCAN_RSP_ADVS=8)
ADD_DEFINITIONS (-DBLE_LL_WHITELIST_SIZE=8)
ADD_DEFINITIONS (-DBLE_LL_RESOLV_LIST_SIZE=4)
ADD_DEFINITIONS (-DBLE_LL_MAX_PKT_SIZE=251)
ADD_DEFINITIONS (-DBLE_LL_SUPP_MAX_RX_BYTES=BLE_LL_MAX_PKT_SIZE)
ADD_DEFINITIONS (-DBLE_LL_SUPP_MAX_TX_BYTES=BLE_LL_MAX_PKT_SIZE)
ADD_DEFINITIONS (-DBLE_LL_CONN_INIT_MAX_TX_BYTES=27)
ADD_DEFINITIONS (-DBLE_LL_CONN_INIT_SLOTS=4)
ADD_DEFINITIONS (-DBLE_LL_CONN_INIT_MIN_WIN_OFFSET=0)
ADD_DEFINITIONS (-DBLE_LL_STRICT_CONN_SCHEDULING=0)
ADD_DEFINITIONS (-DBLE_LL_ADD_STRICT_SCHED_PERIODS=0)
ADD_DEFINITIONS (-DBLE_LL_USECS_PER_PERIOD=3250)
ADD_DEFINITIONS (-DBLE_LL_RNG_BUFSIZE=32)
ADD_DEFINITIONS (-DBLE_XTAL_SETTLE_TIME=0)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_LE_ENCRYPTION=1)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_CONN_PARAM_REQ=1)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_SLAVE_INIT_FEAT_XCHG=1)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_LE_PING=BLE_LL_CFG_FEAT_LE_ENCRYPTION)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_DATA_LEN_EXT=1)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_LL_PRIVACY=1)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_EXT_SCAN_FILT=0)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_LE_CSA2=0)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_LE_2M_PHY=0)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_LE_CODED_PHY=0)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_LL_EXT_ADV=BLE_EXT_ADV)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_LL_PERIODIC_ADV=BLE_PERIODIC_ADV)
ADD_DEFINITIONS (-DBLE_LL_CFG_FEAT_LL_PERIODIC_ADV_SYNC_CNT=BLE_MAX_PERIODIC_SYNCS)
ADD_DEFINITIONS (-DBLE_LL_EXT_ADV_AUX_PTR_CNT=0)
ADD_DEFINITIONS (-DBLE_PUBLIC_DEV_ADDR="\(uint8_t[6]\){0x00, 0x00, 0x00, 0x00, 0x00, 0x00}")
ADD_DEFINITIONS (-DBLE_LL_DTM=BLE_LL_DIRECT_TEST_MODE)
ADD_DEFINITIONS (-DBLE_LL_DTM_EXTENSIONS=0)
ADD_DEFINITIONS (-DBLE_LL_VND_EVENT_ON_ASSERT=0)
ADD_DEFINITIONS (-DBLE_LL_SYSINIT_STAGE=250)
ADD_DEFINITIONS (-DBLE_LL_DBG_HCI_CMD_PIN=-1)
ADD_DEFINITIONS (-DBLE_LL_DBG_HCI_EV_PIN=-1)
ADD_DEFINITIONS (-DBLE_LL_DIRECT_TEST_MODE=0)
ADD_DEFINITIONS (-DBLE_DEVICE=1)
ADD_DEFINITIONS (-DBLE_LP_CLOCK=1)

ADD_DEFINITIONS (-DBLE_STORE_CONFIG_PERSIST=0)
ADD_DEFINITIONS (-DBLE_STORE_SYSINIT_STAGE=500)
ADD_DEFINITIONS (-DBLE_STORE_RAM_SYSINIT_STAGE=500)

#------------------------------------------------------------------------------
# Disable many warnings while building Newt code
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

ADD_DEFINITIONS (-DMYNEWT=1 -DFORCE_MYNEWT=1)

SET (NIMBLE_SYSLIBS)
LIST (APPEND NIMBLE_SYSLIBS
  ans
  bas
  base64
  bleuart
  bsp
  cmsis-core
  common
  controller
  dis
  drivers
  gap
  gatt
  hal
  host
  ias
  ipss
  lls
  mcu
  nrf52
  nrfx
  os
  ram
  store
  sys
  tinycrypt
  tps
  util)

find_subprojects (SUBPROJECTS docs porting)

# build all projects
FOREACH (project ${SUBPROJECTS})
  ADD_SUBDIRECTORY (${project} ${project})
ENDFOREACH ()
