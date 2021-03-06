DISTCHECK_CONFIGURE_FLAGS = --with-systemd=$$dc_install_base/$(systemd)
SUBDIRS         = src docs man
doc_DATA        = README.md docs/HOWTO.md ChangeLog.md COPYING
EXTRA_DIST      = README.md docs/HOWTO.md ChangeLog.md

if SYSTEMD
systemd_DATA     = ntpclient.service
endif

## Larry's versioning scheme: YYYY_DOY, i.e. `date +"%Y_%j"`
version:
	@date +"%Y_%j"

## Generate MD5 checksum file
MD5 = md5sum
md5-dist:
	@for file in $(DIST_ARCHIVES); do	\
		$(MD5) $$file > ../$$file.md5;	\
		mv $$file ../;			\
	done

## Check if tagged in git
release-hook:
	if [ ! `git tag | grep $(PACKAGE_VERSION)` ]; then				\
		echo;									\
		printf "\e[1m\e[41mCannot find release tag $(PACKAGE_VERSION)\e[0m\n";	\
		printf "\e[1m\e[5mDo release anyway?\e[0m "; read yorn;			\
		if [ "$$yorn" != "y" -a "$$yorn" != "Y" ]; then				\
			printf "OK, aborting release.\n";				\
			exit 1;								\
		fi;									\
		echo;									\
	else										\
		echo;									\
		printf "\e[1m\e[42mFound GIT release tag $(PACKAGE_VERSION)\e[0m\n";	\
		printf "\e[1m\e[44m>>Remember to push tags!\e[0m\n";			\
		echo;									\
	fi

# lintian --profile debian -i -I --show-overrides ../$PKG.changes
package build-deb:
	dpkg-buildpackage -uc -us -B

## Target to run when building a release
release: distcheck release-hook md5-dist package
	@echo
	@echo "Resulting release files:"
	@echo "========================================================================="
	@for file in $(DIST_ARCHIVES); do						\
		printf "%-40s Distribution tarball\n" $$file;				\
		printf "%-40s " $$file.md5; cat ../$$file.md5 | cut -f1 -d' ';		\
	done
	@for file in `cd ..; ls $(PACKAGE)_$(subst _,.,$(VERSION))*`; do		\
		printf "%-40s Debian/Ubuntu package file\n" $$file;			\
	done
