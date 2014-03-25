%bcond_without bootstrap
%global packname  lavaan
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.5.16
Release:          1
Summary:          Latent Variable Analysis
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/lavaan_0.5-16.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-methods 
Requires:         R-stats4
Requires:         R-stats
Requires:         R-graphics 
%if %{with bootstrap}
Requires:         R-quadprog
Requires:         R-boot 
%else
Requires:         R-psych
Requires:         R-qgraph
Requires:         R-quadprog
Requires:         R-boot 
%endif
BuildRequires:    R-devel
BuildRequires: R-lavaan
Requires: R-lavaan
BuildRequires: R-pbivnorm
Requires: R-pbivnorm
BuildRequires: R-mnormt
Requires: R-mnormt
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex
BuildRequires:    R-methods
BuildRequires:    R-stats4
BuildRequires:    R-stats
BuildRequires:    R-graphics 
%if %{with bootstrap}
BuildRequires:    R-quadprog R-boot 
%else
BuildRequires:    R-psych
BuildRequires:    R-qgraph
BuildRequires:    R-quadprog
BuildRequires:    R-boot 
%endif
BuildRequires:    pkgconfig(lapack)

%description
Fit a variety of latent variable models, including confirmatory factor
analysis, structural equation modeling and latent growth curve models.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help


%changelog
* Wed Feb 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4_12-2
+ Revision: 778904
- Rebuild with proper dependencies

* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4_12-1
+ Revision: 777831
- Import R-lavaan
- Import R-lavaan


