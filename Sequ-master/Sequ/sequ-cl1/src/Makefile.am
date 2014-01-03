SUBDIRS = sequ

bin_SCRIPTS = sequ-cl1
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = sequ-cl1.in

do_substitution = sed -e 's,[@]pythondir[@],$(pythondir),g' \
	-e 's,[@]PACKAGE[@],$(PACKAGE),g' \
	-e 's,[@]VERSION[@],$(VERSION),g'

sequ-cl1: sequ-cl1.in Makefile
	$(do_substitution) < $(srcdir)/sequ-cl1.in > sequ-cl1
	chmod +x sequ-cl1
