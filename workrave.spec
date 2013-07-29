%define api 1.0
%define major 0
%define libname %mklibname workrave-private %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define devname %mklibname -d workrave-private

Summary:	Assists in recovery and prevention of Repetitive Strain Injury (RSI)
Name:		workrave
Version:	1.10.1
Release:	1
License:	GPLv3+
Group:		Accessibility
Url:		http://www.workrave.org/
Source0:	http://prdownloads.sourceforge.net/workrave/%{name}-%{version}.tar.gz
Patch0:		workrave-1.10.1-desktop.patch
BuildRequires:	doxygen
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	python-cheetah
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gdkmm-2.4)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(gnet-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(libpanelapplet-4.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xtst)
Obsoletes:	%{name}-applet < 1.9.4

%description
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

The program can be run distributed on one or more PCs. All connected
PCs share the same timing information. When you switch computers, you
will still be asked to pause on time.

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/sounds/%{name}
%{_datadir}/dbus-1/services/org.workrave.Workrave.service
%{_iconsdir}/hicolor/*/apps/%{name}*
%{_iconsdir}/hicolor/scalable/workrave-sheep.svg

#----------------------------------------------------------------------------

%package gnome-applet
Summary:	Workrave GNOME applet
Group:		Accessibility
Requires:	%{name} = %{version}-%{release}

%description gnome-applet
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

The program can be run distributed on one or more PCs. All connected
PCs share the same timing information. When you switch computers, you
will still be asked to pause on time.

This package contains applet specific for GNOME desktop environment.
It is not necessary for basic functionality, but %{name} can cooperate
more with GNOME environment, such as embedding in GNOME panel.

%files gnome-applet
%{_libexecdir}/workrave-applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.WorkraveAppletFactory.service
%{_datadir}/gnome-panel/4.0/applets/org.workrave.WorkraveApplet.panel-applet
%{_datadir}/gnome-panel/ui/workrave-gnome-applet-menu.xml

#----------------------------------------------------------------------------

%package -n gnome-shell-%{name}-extension
Summary:	Workrave GNOME Shell extension
Group:		Accessibility
Requires:	%{name} = %{version}-%{release}

%description -n gnome-shell-%{name}-extension
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

The program can be run distributed on one or more PCs. All connected
PCs share the same timing information. When you switch computers, you
will still be asked to pause on time.

This package contains GNOME Shell extension.

%files -n gnome-shell-%{name}-extension
%{_datadir}/gnome-shell/extensions/workrave@workrave.org


#----------------------------------------------------------------------------

%package -n %{libname}
Group:		System/Libraries
Summary:	Shared library for %{name}

%description -n %{libname}
Sahred library for %{name}.

%files -n %{libname}
%{_libdir}/libworkrave-private-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface library for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/Workrave-%{api}.typelib

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development libraries, header files and utilities for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

The program can be run distributed on one or more PCs. All connected
PCs share the same timing information. When you switch computers, you
will still be asked to pause on time.

This package contains the files necessary to develop applications with
%{name}.

%files -n %{devname}
%{_libdir}/libworkrave-private-%{api}.so
%{_datadir}/gir-1.0/Workrave-%{api}.gir

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
	--enable-app-text=no \
	--enable-distribution=yes \
	--enable-gconf=yes \
	--enable-dbus=yes \
	--disable-static \
	--disable-rpath \
	--disable-xml \
	--disable-gnome2 \
	--disable-indicator \
	--disable-schemas-compile \
	--enable-gnome3

%make

%install
%makeinstall_std

%find_lang %{name}

