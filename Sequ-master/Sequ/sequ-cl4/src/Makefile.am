SUBDIRS = sequ

bin_SCRIPTS = sequ-cl4
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = sequ-cl4.in

do_substitution = sed -e 's,[@]pythondir[@],$(pythondir),g' \
				  	-e 's,[@]PACKAGE[@],$(PACKAGE),g' \
						-e 's,[@]VERSION[@],$(VERSION),g'

sequ-cl4: sequ-cl4.in Makefile
		$(do_substitution) < $(srcdir)/sequ-cl4.in > sequ-cl4
			chmod +x sequ-cl4
