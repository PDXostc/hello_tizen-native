############
This is source code for the for the bp Crosswalk extension.

bp works with the HelloTizen application, receiving title and description data as each item is added
in the application, and sending back a modified title string. This demonstrates how to
use the JavaScript to extension interfaces, and also provides a simple example of
a Crosswalk extension that can be used as an example.

For a tutorial on how Crosswalk extensions work, JSON, and another example extension,
go to: https://crosswalk-project.org/#documentation/tizen_ivi_extensions/write_an_extension_in_c%252b%252b

To build the bp  extension into it's RPM package, ready to install: 
sudo gbs build --include-all --spec BoilerPlate.spec -A i586

To install the built bp RPM package:  rpm -ivh BoilerPlate-0.0.1-1.i686.rpm





