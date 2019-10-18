#-----------------------------------------------------------------------------
# NimBLE porting layer
#
# @file CMakeLists.txt
#-----------------------------------------------------------------------------

ADD_DEFINITIONS (-DNIMBLE_CFG_CONTROLLER=1)

build_component_from (
  src/endian.c
  src/hal_timer.c
  src/mem.c
  src/nimble_port.c
  src/os_cputime.c
  src/os_cputime_pwr2.c
  src/os_mbuf.c
  src/os_mempool.c
  src/os_msys_init.c
)
