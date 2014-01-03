SUBDIRS = sequ

bin_SCRIPTS = sequ-cl3
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = sequ-cl3.in

do_substitution = sed -e 's,[@]pythondir[@],$(pythondir),g' \
	-e 's,[@]PACKAGE[@],$(PACKAGE),g' \
	-e 's,[@]VERSION[@],$(VERSION),g'

sequ-cl3: sequ-cl3.in Makefile
	$(do_substitution) < $(srcdir)/sequ-cl3.in > sequ-cl3
	chmod +x sequ-cl3
