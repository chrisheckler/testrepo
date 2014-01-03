SUBDIRS = sequ

bin_SCRIPTS = sequ-cl0
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = sequ-cl0.in

do_substitution = sed -e 's,[@]pythondir[@],$(pythondir),g' \
	-e 's,[@]PACKAGE[@],$(PACKAGE),g' \
	-e 's,[@]VERSION[@],$(VERSION),g' 

sequ-cl0: sequ-cl0.in Makefile
	$(do_substitution) < $(srcdir)/sequ-cl0.in > sequ-cl0
	chmod +x sequ-cl0
