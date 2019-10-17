#-----------------------------------------------------------------------------
# Bluetooth shell application
#
#-----------------------------------------------------------------------------

SET (SW_VERSION "0.1.0")

#-----------------------------------------------------------------------------
# Build rules
#-----------------------------------------------------------------------------

GET_FILENAME_COMPONENT (COMPONENT ${CMAKE_CURRENT_SOURCE_DIR} NAME)

use_nrf52832()
use_newlib ()

tag_application (${COMPONENT} ${CMAKE_SOURCE_DIR})

INCLUDE_DIRECTORIES(include
                    ${CMAKE_CURRENT_BINARY_DIR})

ADD_DEFINITIONS (-DSW_VERSION="${SW_VERSION}")

IF (DEFINED XTCHECK)
  SET (CMAKE_C_CLANG_TIDY ${ctidy})
ENDIF ()

ADD_EXECUTABLE (${COMPONENT}
                ${CMAKE_CURRENT_BINARY_DIR}/${TAGFILE_SRC})
ADD_DEFINITIONS (-DAPP_NAME=${COMPONENT})
ADD_FILE_DEPENDENCIES (src/pa_main.c
                       ${CMAKE_CURRENT_BINARY_DIR}/${TAGFILE_HEADER})
ADD_FILE_DEPENDENCIES (src/pa_pwr.c
                       ${CMAKE_CURRENT_SOURCE_DIR}/src/pa_pwr.sm)

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
          LINK_SCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/ld/nrf52xxaa.ld
          LINK_SCRIPT_DIR ${CMAKE_SOURCE_DIR}/sdk/nrfx/mdk)

post_gen_app (${COMPONENT} ASM)

SET (elffile ${CMAKE_CURRENT_BINARY_DIR}/${COMPONENT}${CMAKE_EXECUTABLE_SUFFIX})
ADD_CUSTOM_COMMAND (TARGET ${COMPONENT} POST_BUILD
                    COMMAND ${nrfhex}
                        -s ${CMAKE_SOURCE_DIR}/sdk/${NIMBLE_SD}
                        -e ${elffile}
                        -o ${CMAKE_CURRENT_BINARY_DIR}
                    COMMENT "Generating HEX flash file" VERBATIM)
