cmake_minimum_required(VERSION 3.5)

project(cam LANGUAGES CXX)

find_package(OpenCV REQUIRED)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(cam /home/pi/Desktop/multiwebcam/main.cpp
)

target_include_directories(cam PRIVATE ${OpenCV_INCLUDE_DIRS})

target_link_libraries(cam PRIVATE ${OpenCV_LIBS})

include(GNUInstallDirs)
install(TARGETS cam
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
