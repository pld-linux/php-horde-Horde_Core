# TODO
# - system locale dir
%define		status		stable
%define		pearname	Horde_Core
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Core Framework libraries
Name:		php-horde-Horde_Core
Version:	1.9.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	8cfaf520903fdbd2aac7eb9054029df7
URL:		https://github.com/horde/horde/tree/master/framework/Core/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-horde-Horde_Role
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_ActiveSync < 2.0.0
Requires:	php-horde-Horde_Alarm < 2.0.0
Requires:	php-horde-Horde_Auth < 2.0.0
Requires:	php-horde-Horde_Autoloader < 2.0.0
Requires:	php-horde-Horde_Browser < 2.0.0
Requires:	php-horde-Horde_Cache < 2.0.0
Requires:	php-horde-Horde_Cli < 2.0.0
Requires:	php-horde-Horde_Compress < 2.0.0
Requires:	php-horde-Horde_Controller < 2.0.0
Requires:	php-horde-Horde_Data < 2.0.0
Requires:	php-horde-Horde_Date < 2.0.0
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Group < 2.0.0
Requires:	php-horde-Horde_History < 2.0.0
Requires:	php-horde-Horde_Injector < 2.0.0
Requires:	php-horde-Horde_Lock < 2.0.0
Requires:	php-horde-Horde_Log < 2.0.0
Requires:	php-horde-Horde_LoginTasks < 2.0.0
Requires:	php-horde-Horde_Mime < 2.0.0
Requires:	php-horde-Horde_Mime_Viewer < 2.0.0
Requires:	php-horde-Horde_Notification < 2.0.0
Requires:	php-horde-Horde_Perms < 2.0.0
Requires:	php-horde-Horde_Prefs < 2.0.0
Requires:	php-horde-Horde_Secret < 2.0.0
Requires:	php-horde-Horde_Serialize < 2.0.0
Requires:	php-horde-Horde_SessionHandler < 2.0.0
Requires:	php-horde-Horde_Share < 2.0.0
Requires:	php-horde-Horde_Support < 2.0.0
Requires:	php-horde-Horde_Template < 2.0.0
Requires:	php-horde-Horde_Text_Filter < 2.0.0
Requires:	php-horde-Horde_Text_Filter_Csstidy < 2.0.0
Requires:	php-horde-Horde_Token < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-horde-Horde_Url < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-horde-Horde_View < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Requires:	php-session
Suggests:	php-dom
Suggests:	php-hash
Suggests:	php-horde-Horde_Crypt
Suggests:	php-horde-Horde_Db
Suggests:	php-horde-Horde_Editor
Suggests:	php-horde-Horde_Form
Suggests:	php-horde-Horde_Http
Suggests:	php-horde-Horde_Icalendar
Suggests:	php-horde-Horde_Image
Suggests:	php-horde-Horde_Imap_Client
Suggests:	php-horde-Horde_Kolab_Server
Suggests:	php-horde-Horde_Kolab_Session
Suggests:	php-horde-Horde_Kolab_Storage
Suggests:	php-horde-Horde_Ldap
Suggests:	php-horde-Horde_Mail
Suggests:	php-horde-Horde_Nls
Suggests:	php-horde-Horde_Oauth
Suggests:	php-horde-Horde_Routes
Suggests:	php-horde-Horde_Service_Twitter
Suggests:	php-horde-Horde_SpellChecker
Suggests:	php-horde-Horde_Text_Filter
Suggests:	php-horde-Horde_Tree
Suggests:	php-horde-Horde_Vfs
Suggests:	php-pear-Net_DNS2
Suggests:	php-pear-Text_CAPTCHA
Suggests:	php-pear-Text_Figlet
Suggests:	php-pecl-lzf
Suggests:	php-simplexml
Suggests:	php-sockets
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		hordedir	/usr/share/horde

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Crypt.*) pear(Horde/Db.*) pear(Horde/Editor.*) pear(Horde/Form.*) pear(Horde/Http.*) pear(Horde/Icalendar.*) pear(Horde/Image.*) pear(Horde/Imap/Client.*) pear(Horde/Kolab/Server.*) pear(Horde/Kolab/Session.*) pear(Horde/Kolab/Storage.*) pear(Horde/Ldap.*) pear(Horde/Mail.*) pear(Horde/Nls.*) pear(Horde/Oauth.*) pear(Horde/Routes.*) pear(Horde/Service/Twitter.*) pear(Horde/SpellChecker.*) pear(Horde/Text/Filter.*) pear(Horde/Tree.*) pear(Horde/Vfs.*) pear(Net/DNS2.*) pear(Text/CAPTCHA.*) pear(Text/Figlet.*) pear(lzf.*)

%description
These classes provide the core functionality of the Horde Application
Framework.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv ./%{php_pear_dir}/www/horde .

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{hordedir}}
%pear_package_install

cp -a horde/* $RPM_BUILD_ROOT%{hordedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde.php
%{php_pear_dir}/Horde/Config.php
%{php_pear_dir}/Horde/ErrorHandler.php
%{php_pear_dir}/Horde/Help.php
%{php_pear_dir}/Horde/Menu.php
%{php_pear_dir}/Horde/Registry.php
%{php_pear_dir}/Horde/Session.php
%{php_pear_dir}/Horde/Themes.php
%{php_pear_dir}/Horde/Config
%{php_pear_dir}/Horde/Core
%{php_pear_dir}/Horde/Exception/*.php
%{php_pear_dir}/Horde/Registry
%{php_pear_dir}/Horde/Script
%{php_pear_dir}/Horde/Themes
%{php_pear_dir}/data/Horde_Core

%dir %{hordedir}
%dir %{hordedir}/js
%{hordedir}/js/*.js
