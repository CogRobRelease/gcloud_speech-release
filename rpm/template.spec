Name:           ros-lunar-gcloud-speech-utils
Version:        0.0.5
Release:        1%{?dist}
Summary:        ROS gcloud_speech_utils package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       gflags-devel
Requires:       glog-devel
Requires:       libportaudio-devel
Requires:       pyaudio
Requires:       ros-lunar-actionlib
Requires:       ros-lunar-actionlib-msgs
Requires:       ros-lunar-gcloud-speech-msgs
BuildRequires:  gflags-devel
BuildRequires:  glog-devel
BuildRequires:  libportaudio-devel
BuildRequires:  pyaudio
BuildRequires:  ros-lunar-actionlib
BuildRequires:  ros-lunar-actionlib-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-gcloud-speech-msgs

%description
Utilities and examples for gcloud_speech package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Apr 18 2018 Shengye Wang <shengye@ucsd.edu> - 0.0.5-1
- Autogenerated by Bloom

* Wed Apr 18 2018 Shengye Wang <shengye@ucsd.edu> - 0.0.5-0
- Autogenerated by Bloom

* Sat Oct 07 2017 Shengye Wang <shengye@ucsd.edu> - 0.0.4-0
- Autogenerated by Bloom

* Sat Oct 07 2017 Shengye Wang <shengye@ucsd.edu> - 0.0.3-1
- Autogenerated by Bloom

* Fri Oct 06 2017 Shengye Wang <shengye@ucsd.edu> - 0.0.3-0
- Autogenerated by Bloom

* Fri Oct 06 2017 Shengye Wang <shengye@ucsd.edu> - 0.0.2-0
- Autogenerated by Bloom

