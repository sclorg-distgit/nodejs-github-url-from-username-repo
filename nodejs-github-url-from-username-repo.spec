%{?scl:%scl_package nodejs-github-url-from-username-repo}
%{!?scl:%global pkg_name %{name}}

%global npm_name github-url-from-username-repo
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-github-url-from-username-repo
Version:        1.0.0
Release:        1%{?dist}
Summary:        Create urls from username/repo

Url:            https://github.com/robertkowalski/github-url-from-username-repo
Source0:        http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:        BSD-2-Clause
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n) 

%description
Create urls from username/repo

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{nodejs_sitelib}/github-url-from-username-repo
cp -pr index.js package.json %{buildroot}/%{nodejs_sitelib}/github-url-from-username-repo

%check
%nodejs_symlink_deps --check --no-devdeps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/github-url-from-username-repo
%doc README.md LICENSE

%changelog
* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-1
- New upstream release 1.0.0

* Thu Jan 23 2014 Tomas Hrcka <thrcka@redhat.com> - 0.0.2-1
- Package import
