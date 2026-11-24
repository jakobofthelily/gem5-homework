# The build environment of gem5 v25.0.0.1: the gem5 project's own image for
# that release (Ubuntu 24.04, GCC 13, Python 3.12, SCons, and every library
# gem5 can use). The digest pins the exact image this repository was tested
# with.
FROM ghcr.io/gem5/ubuntu-24.04_all-dependencies:v25-0@sha256:3dfea5a12b82705f894b389afd86547be3231492f34e0e56ad61dc96087ccd33

# `gem5` runs the gem5 built in this repository, like the alias used in the
# bootcamp. Set GEM5_BUILD to use a build other than ALL.
COPY docker/gem5 /usr/local/bin/gem5

WORKDIR /workshop
