#-----------------------------------------------------------------------------
# Bluetooth shell application
#
#-----------------------------------------------------------------------------

SET (SW_VERSION "0.1.0")

#-----------------------------------------------------------------------------
# Build rules
#-----------------------------------------------------------------------------

GET_FILENAME_COMPONENT (COMPONENT ${CMAKE_CURRENT_SOURCE_DIR} NAME)

use_newlib ()

use_sdk_headers (
  nimble/host/services/gap
  nimble/host/services/gatt
  core/sys/shell
  core/util/streamer
)

tag_application (${COMPONENT} ${CMAKE_SOURCE_DIR})

INCLUDE_DIRECTORIES(include
                    ${CMAKE_CURRENT_BINARY_DIR})

ADD_DEFINITIONS (-DSW_VERSION="${SW_VERSION}")

IF (DEFINED XTCHECK)
  SET (CMAKE_C_CLANG_TIDY ${ctidy})
ENDIF ()

ADD_DEFINITIONS (-DBTSHELL_ANS=1)
ADD_DEFINITIONS (-DSHELL_TASK=1)
ADD_DEFINITIONS (-DLOG_LEVEL=1)
ADD_DEFINITIONS (-DBLE_SM_LEGACY=0)
ADD_DEFINITIONS (-DBLE_SM_SC=0)
ADD_DEFINITIONS (-DOS_MAIN_STACK_SIZE=512)
ADD_DEFINITIONS (-DSHELL_MGMT=0)
ADD_DEFINITIONS (-DMSYS_1_BLOCK_COUNT=16)
ADD_DEFINITIONS (-DMYNEWT_VAL_MSYS_1_BLOCK_SIZE=MSYS_1_BLOCK_SIZE)

ADD_EXECUTABLE (${COMPONENT}
                src/cmd.c
                src/cmd_gatt.c
                src/cmd_l2cap.c
                src/gatt_svr.c
                src/main.c
                src/misc.c
                src/parse.c
                ${CMAKE_CURRENT_BINARY_DIR}/${TAGFILE_SRC})
ADD_DEFINITIONS (-DAPP_NAME=${COMPONENT})
ADD_FILE_DEPENDENCIES (src/main.c
                       ${CMAKE_CURRENT_BINARY_DIR}/${TAGFILE_HEADER})

GET_TARGET_PROPERTY (sources ${COMPONENT} SOURCES)
FOREACH (src ${sources})
   GET_FILENAME_COMPONENT (basename ${src} NAME_WE)
   STRING (REGEX REPLACE "^.*_(.*)$" "\\1" radix ${basename})
   STRING (TOUPPER ${radix} uradix)
   STRING (TOLOWER ${radix} lradix)
   SET_SOURCE_FILES_PROPERTIES (${src}
                                PROPERTIES COMPILE_FLAGS
                                "-DPTM_SOURCE=PTM_${uradix} -DPTM_NAME=${lradix}")
ENDFOREACH ()

LIST (APPEND NIMBLE_LIBS ${NIMBLE_SYSLIBS})
MESSAGE (STATUS "Libraries: ${NIMBLE_LIBS}")
link_app (${COMPONENT}
          ${NIMBLE_LIBS}
          # LINK_SCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/ld/nrf52xxaa.ld
          LINK_SCRIPT ${CMAKE_SOURCE_DIR}/core/hw/bsp/nordic_pca10040/nordic_pca10040_no_boot.ld
          LINK_SCRIPT_DIR ${CMAKE_SOURCE_DIR}/sdk/nrfx/mdk)

post_gen_app (${COMPONENT} ASM)

SET (elffile ${CMAKE_CURRENT_BINARY_DIR}/${COMPONENT}${CMAKE_EXECUTABLE_SUFFIX})
ADD_CUSTOM_COMMAND (TARGET ${COMPONENT} POST_BUILD
                    COMMAND ${nrfhex}
                        -s ${CMAKE_SOURCE_DIR}/sdk/${NIMBLE_SD}
                        -e ${elffile}
                        -o ${CMAKE_CURRENT_BINARY_DIR}
                    COMMENT "Generating HEX flash file" VERBATIM)
