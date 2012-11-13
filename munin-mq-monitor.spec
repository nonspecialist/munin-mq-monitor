Name:		munin-mq-monitor 
Version:	0.1
Release:	1%{?dist}
Summary:	Monitoring scripts for various message brokers

Group:		Applications/System
License:	GPL
URL:		https://github.com/nonspecialist/munin-mq-monitor
Source0:	munin-mq-monitor.tar.gz

BuildArch:	noarch
Requires:	stomppy, munin-node

%description
Provides various monitoring scripts for Munin to query broker and 
queue statistics from a local ActiveMQ node which has the Statistics
Plugin enabled (see http://activemq.apache.org/statisticsplugin.html)

%prep
%setup -q -n src

%build
/bin/true

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/munin/plugins \
	 $RPM_BUILD_ROOT/etc/munin/plugins

cp broker_stats queue_stats $RPM_BUILD_ROOT/usr/share/munin/plugins
cd $RPM_BUILD_ROOT/etc/munin/plugins
	ln -s /usr/share/munin/plugins/broker_stats .
	ln -s /usr/share/munin/plugins/queue_stats .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(0755,root,root)	/usr/share/munin/plugins/broker_stats
%attr(0755,root,root)	/usr/share/munin/plugins/queue_stats
			/etc/munin/plugins/broker_stats
			/etc/munin/plugins/queue_stats

%changelog
* Tue Nov 13 2012 Colin Panisset <nonspecialist@clabber.com>
- initial version of spec file
- initial, nasty version of horribly hacky python scripts
