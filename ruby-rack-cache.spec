%define rname	rack-cache

Name:		ruby-rack-cache
Summary:	Ruby component to enable HTTP caching for Rack-based applications
Version:	1.2
Release:	1
License:	MIT
Group:		Development/Ruby
URL:		http://rubygems.org/gems/rack-cache
Source0:	http://rubygems.org/downloads/rack-cache-1.2.gem
BuildArch:	noarch
BuildRequires:	ruby-RubyGems

%description
Rack::Cache is suitable as a quick drop-in component to enable HTTP caching
for Rack-based applications that produce freshness (Expires, Cache-Control)
and/or validation (Last-Modified, ETag) information.

%prep

%build

%install
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}
rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec
%doc %{ruby_gemdir}/doc/%{rname}-%{version}
