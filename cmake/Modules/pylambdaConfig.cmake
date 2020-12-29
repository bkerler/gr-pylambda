INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_PYLAMBDA pylambda)

FIND_PATH(
    PYLAMBDA_INCLUDE_DIRS
    NAMES pylambda/api.h
    HINTS $ENV{PYLAMBDA_DIR}/include
        ${PC_PYLAMBDA_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    PYLAMBDA_LIBRARIES
    NAMES gnuradio-pylambda
    HINTS $ENV{PYLAMBDA_DIR}/lib
        ${PC_PYLAMBDA_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/pylambdaTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(PYLAMBDA DEFAULT_MSG PYLAMBDA_LIBRARIES PYLAMBDA_INCLUDE_DIRS)
MARK_AS_ADVANCED(PYLAMBDA_LIBRARIES PYLAMBDA_INCLUDE_DIRS)
