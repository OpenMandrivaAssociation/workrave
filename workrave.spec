Summary:	Assists in recovery and prevention of Repetitive Strain Injury (RSI)
Name:		workrave
Version:	1.9.4
Release:	3
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
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(xmu)
Obsoletes:	%{name}-gnome-applet < 1.9.4-3
Obsoletes:	%{name}-applet < 1.9.4

%description
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

The program can be run distributed on one or more PCs. All connected
PCs share the same timing information. When you switch computers, you
will still be asked to pause on time.

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
	--disable-gnome \
	--disable-kde
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/sounds/%{name}
%{_datadir}/dbus-1/services/org.workrave.Workrave.service
%{_iconsdir}/hicolor/*/apps/%{name}*

