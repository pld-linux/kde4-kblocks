%define		_state		stable
%define		orgname		kblocks
%define		qtver		4.8.0

Summary:	KDE Blocks
Name:		kde4-kblocks
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	0ded6841be5be06fea1f292fd5618777
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-kblocks
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kblocks.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
touch $RPM_BUILD_ROOT/var/games/kbounce.scores
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang kblocks	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files -f kblocks.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblocks
%{_desktopdir}/kde4/kblocks.desktop
%{_datadir}/apps/kblocks
%{_datadir}/config.kcfg/kblocks.kcfg
%{_datadir}/config/kblocks.knsrc
%{_iconsdir}/*/*/apps/kblocks.png
