#
# Require environment variable BOOST_REGEX_STATIC_LIB,
# as full path to static library 'libboost_regex.a'
#

CPP                 = g++
CPP_FLAG            = -Wextra -Wall -Wno-long-long -pedantic -O2
CPP_INCLUDE         = -I/usr/include
CPP_LIBS            = -L/usr/lib
BOOST_REGEX_STATIC  = $(BOOST_REGEX_STATIC_LIB)

UDEV_DIR_CONF       = /etc/udev
UDEV_DIR_RULES      = /lib/udev/rules.d

UDEV_NAMER          = mlnx-udev-namer
UDEV_NAMER_BIN      = /opt/mellanox/bin
UDEV_NAMER_CONF     = $(UDEV_NAMER).conf
UDEV_NAMER_RULES    = 80-$(UDEV_NAMER).rules

all:
	$(CPP) $(CPP_FLAG) $(CPP_INCLUDE) $(CPP_LIBS) $(UDEV_NAMER).cpp $(BOOST_REGEX_STATIC) -o $(UDEV_NAMER)
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
