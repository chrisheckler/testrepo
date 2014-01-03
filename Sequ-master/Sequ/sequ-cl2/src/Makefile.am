SUBDIRS = sequ

bin_SCRIPTS = sequ-cl2
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = sequ-cl2.in

do_substitution = sed -e 's,[@]pythondir[@],$(pythondir),g' \
	-e 's,[@]PACKAGE[@],$(PACKAGE),g' \
	-e 's,[@]VERSION[@],$(VERSION),g'

sequ-cl2: sequ-cl2.in Makefile
	$(do_substitution) < $(srcdir)/sequ-cl2.in > sequ-cl2
	chmod +x sequ-cl2
