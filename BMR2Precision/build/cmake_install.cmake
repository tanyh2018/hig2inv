# Install script for directory: /cefs/higgs/tanyuhang/BMR2Precision

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/cefs/higgs/tanyuhang/BMR2Precision")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "0")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  IF(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/BMR2Precision" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/BMR2Precision")
    FILE(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/BMR2Precision"
         RPATH "/cefs/higgs/tanyuhang/BMR2Precision/lib:/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/Marlin/v01-05/lib:/home/bes/lig/higgs/ilcsoft/v01-17-05_slc6/lcio/v02-04-03/lib:/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/gsl/1.14/lib:/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/mysql/usr/lib64:/home/bes/lig/higgs/ilcsoft/v01-17-05_slc6/gear/v01-04/lib:/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/CLHEP/2.1.3.1/lib:/home/bes/lig/higgs/ilcsoft/v01-17-05_slc6/ilcutil/v01-01/lib")
  ENDIF()
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/cefs/higgs/tanyuhang/BMR2Precision/build/bin/BMR2Precision")
  IF(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/BMR2Precision" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/BMR2Precision")
    FILE(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/BMR2Precision"
         OLD_RPATH "/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/Marlin/v01-05/lib:/home/bes/lig/higgs/ilcsoft/v01-17-05_slc6/lcio/v02-04-03/lib:/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/gsl/1.14/lib:/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/mysql/usr/lib64:/home/bes/lig/higgs/ilcsoft/v01-17-05_slc6/gear/v01-04/lib:/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/CLHEP/2.1.3.1/lib:/home/bes/lig/higgs/ilcsoft/v01-17-05_slc6/ilcutil/v01-01/lib::::::::::::::::::::::::::::::::::::::::"
         NEW_RPATH "/cefs/higgs/tanyuhang/BMR2Precision/lib:/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/Marlin/v01-05/lib:/home/bes/lig/higgs/ilcsoft/v01-17-05_slc6/lcio/v02-04-03/lib:/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/gsl/1.14/lib:/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/mysql/usr/lib64:/home/bes/lig/higgs/ilcsoft/v01-17-05_slc6/gear/v01-04/lib:/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/CLHEP/2.1.3.1/lib:/home/bes/lig/higgs/ilcsoft/v01-17-05_slc6/ilcutil/v01-01/lib")
    IF(CMAKE_INSTALL_DO_STRIP)
      EXECUTE_PROCESS(COMMAND "/afs/ihep.ac.cn/soft/common/gcc/v01-17-05/mysql/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/BMR2Precision")
    ENDIF(CMAKE_INSTALL_DO_STRIP)
  ENDIF()
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(CMAKE_INSTALL_COMPONENT)
  SET(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
ELSE(CMAKE_INSTALL_COMPONENT)
  SET(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
ENDIF(CMAKE_INSTALL_COMPONENT)

FILE(WRITE "/cefs/higgs/tanyuhang/BMR2Precision/build/${CMAKE_INSTALL_MANIFEST}" "")
FOREACH(file ${CMAKE_INSTALL_MANIFEST_FILES})
  FILE(APPEND "/cefs/higgs/tanyuhang/BMR2Precision/build/${CMAKE_INSTALL_MANIFEST}" "${file}\n")
ENDFOREACH(file)
