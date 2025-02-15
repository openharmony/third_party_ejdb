file(READ ${CMAKE_SOURCE_DIR}/src/bindings/ejdb2_jni/version.txt
     EJDB2_JNI_VERSION)
if(NOT EJDB2_JNI_VERSION)
  message(
    FATAL_ERROR
      "${CMAKE_SOURCE_DIR}/src/bindings/ejdb2_jni/version.txt is not exists")
endif()
set(EJDB2_JNI_VERSION "${PROJECT_VERSION}.${EJDB2_JNI_VERSION}")

set(CPACK_PACKAGE_NAME "${CMAKE_PROJECT_NAME}-java")
set(CPACK_PACKAGE_CONTACT "${PROJECT_MAINTAINER}")
set(CPACK_PACKAGE_VERSION ${EJDB2_JNI_VERSION})
set(CPACK_PACKAGE_VERSION_MAJOR ${ejdb2_VERSION_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR ${ejdb2_VERSION_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH ${ejdb2_VERSION_PATCH})
set(CPACK_PACKAGE_VENDOR ${PROJECT_VENDOR})
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY
    "${PROJECT_DESCRIPTION_SUMMARY} Java binding.")
set(CPACK_PACKAGE_DESCRIPTION "${PROJECT_DESCRIPTION} Java binding.")
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_SOURCE_DIR}/LICENSE")
set(CPACK_RESOURCE_FILE_README "${CMAKE_SOURCE_DIR}/README.md")
set(CPACK_RESOURCE_FILE_WELCOME "${CMAKE_SOURCE_DIR}/README.md")
set(CPACK_PACKAGE_FILE_NAME
    "${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}-${CMAKE_BUILD_TYPE}-${CMAKE_SYSTEM_NAME}-${PROJECT_ARCH}"
)
if(CMAKE_BUILD_TYPE STREQUAL "Release")
  set(CPACK_STRIP_FILES ON)
endif()

set(DEB_CMAKE_ARGS "-DBUILD_JNI_BINDING=ON")

if(PACKAGE_DEB)
  execute_process(
    COMMAND /usr/bin/dpkg --print-architecture
    OUTPUT_VARIABLE CPACK_DEBIAN_PACKAGE_ARCHITECTURE
    RESULT_VARIABLE EXECUTE_RESULT
    OUTPUT_STRIP_TRAILING_WHITESPACE ERROR_QUIET)
  if(EXECUTE_RESULT)
    message(FATAL_ERROR "dpkg not found: No package generation.")
  endif()
  set(CPACK_DEBIAN_PACKAGE_DESCRIPTION ${CPACK_PACKAGE_DESCRIPTION})
  set(CPACK_DEBIAN_PACKAGE_HOMEPAGE ${PROJECT_WEBSITE})
  set(CPACK_DEBIAN_PACKAGE_SECTION libs)
  set(CPACK_DEBIAN_PACKAGE_PRIORITY optional)
  # set(CPACK_DEBIAN_PACKAGE_DEPENDS zlib1g)
  set(CPACK_DEBIAN_PACKAGE_BUILD_DEPENDS pkg-config git devscripts dh-make
                                         openjdk-11-jdk libcurl4-openssl-dev)
  if(NOT PPA_DEBIAN_VERSION)
    set(PPA_DEBIAN_VERSION ppa1)
  endif()
  if(PROJECT_PPA)
    set(DPUT_HOST ${PROJECT_PPA})
  endif()
  # set(CPACK_DEBIAN_PACKAGE_ARCHITECTURE "any")
  set(CPACK_DEBIAN_RESOURCE_FILE_CHANGELOG ${CMAKE_SOURCE_DIR}/Changelog)
  set(CPACK_DEBIAN_UPDATE_CHANGELOG ON)
endif(PACKAGE_DEB)

if(PACKAGE_TGZ)
  set(CPACK_INCLUDE_TOPLEVEL_DIRECTORY OFF)
endif(PACKAGE_TGZ)

include(CPack)

if(ENABLE_PPA)
  if(NOT PROJECT_PPA_DISTRIB_TARGET)
    set(PROJECT_PPA_DISTRIB_TARGET focal)
  endif()
  set(DPUT_CONFIG_IN ${CMAKE_CURRENT_SOURCE_DIR}/../debian/dput.cf.in)
  include(UploadPPA)
endif()
