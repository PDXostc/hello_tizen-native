Name:       BoilerPlate
Summary:    Example Crosswalk extension
Version:    0.0.1
Release:    1
Group:      Libraries/System
License:    ASL 2.0
URL:        http://www.tizen.org2
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  python
BuildRequires:  desktop-file-utils

BuildRequires:  pkgconfig(eina)
BuildRequires:  pkgconfig(eet)
BuildRequires:  pkgconfig(evas)
BuildRequires:  pkgconfig(ecore)
BuildRequires:  pkgconfig(ecore-evas)
BuildRequires:  pkgconfig(edje)
BuildRequires:  pkgconfig(efreet)
BuildRequires:  pkgconfig(eldbus)

Requires:       ibus
Requires:       ibus-hangul
Requires:       ibus-libpinyin


%global plugin_list extension_common BoilerPlateExtension 

%description
A collection of IVI software

%prep

%setup -q -n %{name}-%{version}

%build
for plugin in %{plugin_list}; do
    make -C ${plugin}
done

%install
for plugin in %{plugin_list}; do
    make -C ${plugin} install DESTDIR=%{buildroot} PREFIX=%{_prefix}
done


%files
%{_prefix}/lib/tizen-extensions-crosswalk/libbp.so
