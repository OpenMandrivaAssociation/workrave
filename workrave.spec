Summary:	Assists in recovery and prevention of Repetitive Strain Injury (RSI)
Name:		workrave
Version:	1.9.4
Release:	%mkrel 2
License:	GPLv3+
Group:		Accessibility
URL:		http://www.workrave.org/
Source0:	http://prdownloads.sourceforge.net/workrave/%{name}-%{version}.tar.gz
Source1:	workwave-1.9.4-ru.po
BuildRequires:	doxygen
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	python-cheetah
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gdkmm-2.4)
BuildRequires:	pkgconfig(gnet-2.0)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(libgnomeuimm-2.6)
BuildRequires:	pkgconfig(libpanelapplet-2.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(xmu)

%description
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

The program can be run distributed on one or more PCs. All connected
PCs share the same timing information. When you switch computers, you
will still be asked to pause on time.

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
touch ChangeLog
rm -f po/ru.po
cp %{SOURCE1} po/ru.po

%build
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
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%config(noreplace) %{_sysconfdir}/sound/events/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/sounds/%{name}
%{_datadir}/dbus-1/services/org.workrave.Workrave.service
%{_iconsdir}/hicolor/*/apps/%{name}*

%files gnome-applet
%doc COPYING
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/workrave-applet
%{_datadir}/gnome-2.0/ui/*.xml
