# Copyright 2015 Mellanox Technologies, Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

CPP                 = g++
CPP_FLAG            = -Wextra -Wall -Wno-long-long -pedantic -O2
CPP_INCLUDE         = -I/usr/include
CPP_LIBS            = -L/usr/lib
BOOST_REGEX_LIBS    = -lboost_regex

UDEV_DIR_CONF       = /etc/udev
UDEV_DIR_RULES      = /lib/udev/rules.d

UDEV_NAMER          = mlnx-udev-namer
UDEV_NAMER_BIN      = /opt/mellanox/bin
UDEV_NAMER_CONF     = $(UDEV_NAMER).conf
UDEV_NAMER_RULES    = 80-$(UDEV_NAMER).rules

all:
	$(CPP) $(CPP_FLAG) $(CPP_INCLUDE) $(CPP_LIBS) $(UDEV_NAMER).cpp $(BOOST_REGEX_LIBS) -o $(UDEV_NAMER)
	strip $(UDEV_NAMER)

clean:
	rm -fv $(UDEV_NAMER)

install:
	mkdir -pv $(DESTDIR)$(UDEV_NAMER_BIN) $(DESTDIR)$(UDEV_DIR_CONF) $(DESTDIR)$(UDEV_DIR_RULES)
	rm -fv $(DESTDIR)$(UDEV_NAMER_BIN)/$(UDEV_NAMER)
	[ -f $(UDEV_NAMER) ] && cp -fv $(UDEV_NAMER) $(DESTDIR)$(UDEV_NAMER_BIN)/$(UDEV_NAMER)
	[ -f $(DESTDIR)$(UDEV_DIR_CONF)/$(UDEV_NAMER_CONF) ] || { [ -f $(UDEV_NAMER_CONF) ] && cp -fv $(UDEV_NAMER_CONF) $(DESTDIR)$(UDEV_DIR_CONF)/$(UDEV_NAMER_CONF); }
	rm -fv $(DESTDIR)$(UDEV_DIR_RULES)/$(UDEV_NAMER_RULES)
	[ -f $(UDEV_NAMER_RULES) ] && cp -fv $(UDEV_NAMER_RULES) $(DESTDIR)$(UDEV_DIR_RULES)/$(UDEV_NAMER_RULES)

remove:
	rm -fv $(DESTDIR)$(UDEV_NAMER_BIN)/$(UDEV_NAMER)
	rm -fv $(DESTDIR)$(UDEV_DIR_CONF)/$(UDEV_NAMER_CONF)
	rm -fv $(DESTDIR)$(UDEV_DIR_RULES)/$(UDEV_NAMER_RULES)
