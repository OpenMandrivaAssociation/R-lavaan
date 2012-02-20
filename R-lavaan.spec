%bcond_without bootstrap
%global packname  lavaan
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.4_12
Release:          1
Summary:          Latent Variable Analysis
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-12.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-methods 
Requires:         R-stats4 R-stats R-graphics 
%if %{with bootstrap}
Requires:         R-quadprog R-boot 
%else
Requires:         R-psych R-qgraph R-quadprog R-boot 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-stats4 R-stats R-graphics 
%if %{with bootstrap}
BuildRequires:    R-quadprog R-boot 
%else
BuildRequires:    R-psych R-qgraph R-quadprog R-boot 
%endif

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
