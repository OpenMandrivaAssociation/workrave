%define version 1.9.0
%define release %mkrel 1
%define kdeversion 3
#
# support of docking in GNOME panel. Not very useful since
# it can already embed in notification area.
#
%define enable_gnome 1
%{?_without_gnome: %global enable_gnome 0}

#
# support for KDE
#
%define enable_kde 1
%{?_without_kde: %global enable_kde 0}

#
# save config as XML file. GConf is preferred for GNOME desktop
#
%define enable_xml 0
%{?_with_xml: %global enable_xml 1}

%define longtitle Assists in recovery and prevention of Repetitive Strain Injury (RSI)

Summary:	%{longtitle}
Name:		workrave
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Accessibility
URL:		http://www.workrave.org/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Source0:	http://prdownloads.sourceforge.net/workrave/%{name}-%{version}.tar.bz2

BuildRequires:	doxygen
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libGConf2-devel
BuildRequires:	libgnet2-devel
BuildRequires:	dbus-devel
BuildRequires:  gstreamer0.10-devel
BuildRequires:  intltool
%if %enable_xml
BuildRequires:	gdome2-devel
%endif
%if %enable_gnome
BuildRequires:	libgnomeuimm2.6-devel
BuildRequires:	gnome-panel-devel
%endif
%if %enable_kde
BuildRequires:	kdelibs-devel
%endif

%description
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

The program can be run distributed on one or more PCs. All connected
PCs share the same timing information. When you switch computers, you
will still be asked to pause on time.

Build Options:
--with xml          Store configuration as XML file
--without gnome     Don't build applet that docks in GNOME panel
--without kde       Don't build applet that docks in KDE panel

%package	gnome-applet
Summary:	Workrave GNOME applet
Group:		Accessibility
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-applet <= 1.6.2

%description	gnome-applet
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

The program can be run distributed on one or more PCs. All connected
PCs share the same timing information. When you switch computers, you
will still be asked to pause on time.

This package contains applet specific for GNOME desktop environment.
It is not necessary for basic functionality, but %{name} can cooperate
more with GNOME environment, such as embedding in GNOME panel.

%package	kde-applet
Summary:	Workrave KDE applet
Group:		Accessibility
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-applet <= 1.6.2

%description	kde-applet
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

The program can be run distributed on one or more PCs. All connected
PCs share the same timing information. When you switch computers, you
will still be asked to pause on time.

This package contains applet specific for KDE desktop environment.
It is not necessary for basic functionality, but %{name} can cooperate
more with KDE environment, such as embedding in KDE panel.

%prep
%setup -q

%build
%configure2_5x \
	--enable-app-text=no	\
	--enable-distribution=yes \
	--enable-gconf=yes	\
	--enable-dbus=yes	\
	--disable-rpath		\
%if %enable_xml
	--enable-xml \
%else
	--disable-xml \
%endif
%if %enable_gnome
	--enable-gnome \
%else
	--disable-gnome \
%endif
%if %enable_kde
%if "%{_lib}" != "lib"
    --enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
    --with-qt-includes="/opt/%{kdeversion}/include/"
%endif
	--enable-kde
%else
	--disable-kde
%endif


%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

#
# icons
#
install -m0644 -D frontend/common/share/images/workrave-icon-huge.png %{buildroot}%{_liconsdir}/%{name}.png
install -m0644 -D frontend/common/share/images/workrave-icon-large.png %{buildroot}%{_iconsdir}/%{name}.png
install -m0644 -D frontend/common/share/images/workrave-icon-small.png %{buildroot}%{_miconsdir}/%{name}.png

#
# menu entry
#

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Workrave
Comment=%{longtitle}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=GNOME;GTK;X-MandrivaLinux-MoreApplications-Accessibility;
StartupNotify=true
EOF

#
# remove undesired files
#
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/workrave.po

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%config(noreplace) %{_sysconfdir}/sound/events/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/sounds/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/dbus-1/services/org.workrave.Workrave.service

%if %enable_gnome
%files gnome-applet
%defattr(-,root,root)
%doc COPYING
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/workrave-applet
%{_datadir}/gnome-2.0/ui/*.xml
%endif

%if %enable_kde
%files kde-applet
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libkworkraveapplet.so
%{_datadir}/apps/kicker/applets/*.desktop
%{_datadir}/apps/kworkrave
%_libdir/libkworkraveapplet.a
%_libdir/libkworkraveapplet.la
%endif
