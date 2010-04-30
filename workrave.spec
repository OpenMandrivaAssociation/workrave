%define version 1.9.0
%define release %mkrel 2

Summary:	longtitle Assists in recovery and prevention of Repetitive Strain Injury (RSI)
Name:		workrave
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Accessibility
URL:		http://www.workrave.org/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	http://prdownloads.sourceforge.net/workrave/%{name}-%{version}.tar.bz2
Patch1:		workrave-1.9.1-compile.patch
Patch2:		workrave-1.9.0-gcc44.patch
BuildRequires:	doxygen
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libGConf2-devel
BuildRequires:	libgnet2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libxmu-devel
BuildRequires:  gstreamer0.10-devel
BuildRequires:  intltool
BuildRequires:	libgnomeuimm2.6-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	libtool

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

%prep
%setup -q
%patch1 -p1
%patch2 -p0
touch ChangeLog

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--enable-app-text=no	\
	--enable-distribution=yes \
	--enable-gconf=yes	\
	--enable-dbus=yes	\
	--disable-rpath		\
	--disable-xml \
	--enable-gnome \
	--disable-kde
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

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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

%files gnome-applet
%defattr(-,root,root)
%doc COPYING
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/workrave-applet
%{_datadir}/gnome-2.0/ui/*.xml
