Web Administration Tools
Discover important web administration tools and how to set up a working web server.

Table of Contents
    1. Video: Introduction to nginx (it_lugsub_05_enus_01)

    2. Video: Introduction to MariaDB (it_lugsub_05_enus_02)

    3. Video: Configuring PHP (it_lugsub_05_enus_03)

    4. Video: Introduction to the Basic LEMP Stack (it_lugsub_05_enus_04)

    5. Video: Installing a Basic SSL/TLS Certificate in nginx (it_lugsub_05_enus_05)

    6. Video: Managing /etc/hosts for Web Development (it_lugsub_05_enus_06)

    7. Video: Exercise: Introduction to avconv (it_lugsub_05_enus_07)

1. Video: Introduction to nginx (it_lugsub_05_enus_01)

In this video, learn how to install and configure a simple nginx web server.
Objectives
install and configure a simple nginx webserver
Nginx is a fast, high-performance web server often used in place of Apache's HTTP server. In this video, I'll demonstrate how to get up and running with nginx in Ubuntu. So let's install nginx on the command line using apt, so sudo apt-get install nginx for nginx. And yes, and it will go through the install for us. It will only take a moment to download and set up. And now once we have it, we can test that it's installed and running correctly. So let's open up our web browser, in my case, Firefox. And I'll type in localhost and it tells me, Welcome to nginx! So it tells me it's successfully installed and working. If you don't see this page and you see something else, you may have another web server installed in your system, and you can remove it and use nginx instead, or you can modify nginx to run on a different port instead of the default 80, but we'll get to that. So let's minimize this or let's Close it for now and go back to the terminal. Now we might wonder where that file is being served from. Well, we can find it quite quickly, ls /usr/share/nginx/html.
The stevescott@ss-vb command prompt window is displayed in the Ubuntu desktop with the following command prompt:

stevescott@ss-vb:~$

The presenter runs the following command:

sudo apt-get install nginx

The window prompts the presenter with the following question:

Do you want to continue? [Y/n]

The presenter enters the text 'Y' and then presses the Enter key.

He then opens the Firefox browser window and enters the address 'localhost' in the address bar.

As a result, the Welcome to nginx page is displayed.

Next he navigates back to the command prompt window and runs the following command:

ls /usr/share/nginx/html

As a result, the following output is displayed:

50x.html index.html

So that's where the index.html file is located by default. So the default configuration is to serve this file, but we'd like to serve our own. What I typically do with...a more traditional location to put our HTML files, I go sudo mkdir. So I'm going to make this directory in /var/www. So this www folder I'm going to make, but if I look at it now that I've made it as sudo, ls -l /var/www, -la. So I'm going to see these permissions. So I see that it's owned by root, but I want to own it, and I want other people that have access to the web server to be able to modify it. So typically what we do is we do sudo adduser, put our username followed by the group, www-data. So it's a typical web user group that anyone who is part of this group has access to the files that are served by the web server.
The stevescott@ss-vb command prompt window is displayed with the following command prompt:

stevescott@ss-vb:~$

The presenter runs the following command:

sudo mkdir /var/www

Next he runs the following command:

ls -la /var/www

As a result, a list of files is displayed along with the details such as permissions, owner as root, and group as root.

Next he runs the following command:

sudo adduser stevescott www-data

As a result, the following is displayed:

Adding user stevescott to group www-data
Done.

Then I can do sudo chown for change ownership of using name and the group www-data. So username followed by colon, followed by the group on /var/www. Now if we look at it again, we see that the directory is changed to stevescott and www-data. So that's what we want. Now we want to place under that to serve the files from. So what I typically do is if I'm running multiple instances of a single server under that, I can do...let's go into that directory. I'll do mkdir default and check the permissions. So I've created this. We'll want to change this group to be www-data. And now if I go into my configuration for nginx, I can do...let's do it through vim /etc/nginx/sites-available. So this is where the configuration files are stored. The only one there now is default, so default.
The stevescott@ss-vb command prompt window is displayed with the following command prompt:

stevescott@ss-vb:~$

The presenter runs the following command:

sudo chown stevescott:www-data /var/www

He then runs the following command:

ls -la /var/www

As a result, the owner and group details of a file from the list changes as stevescott and www-data respectively.

Next he runs the following command:

cd /var/www

As a result, the command prompt changes to the following:

stevescott@ss-vb:/var/www$

Then he runs the following command:

mkdir default

He then runs the following command:

ls -la

As a result, a list of files is displayed along with the details such as permissions, owner, and group.

The presenter points at the file that includes the group as stevescott.

Next he runs the following command:

vim /etc/nginx/sites-available/default

As a result, the default file is open in vim in readonly mode.

Now I have some information here. If I go down to find this first server followed by the brace, this is where the server is being shared from. So the first thing I'd like to do is serve my files, not from this directory. It tells me I'm Changing a readonly file. I'm going to quit out of this and not save any changes I've made and run this again as root. So I need to modify this configuration file, the sudo. So sudo vim and we open it up again. Now I'm going to scroll down until I get to this root, so this is the root of our web server and it's listening on port 80. So if I remove this first part and I put /var/www, and I've also changed the directory, so the directory is /var/www/default. So it's going to serve this or the default area, and it has some other possibilities here that we're not going to get into too much detail now. We'd just like to get our initial server up and running. There are many examples of things you can do like PHP that you can uncomment, and there is also another port and/or an HTTPS server if you want to run it on port 443 with ssl, but these are all commented out for now and we're not going to worry about it. So let's write our changes and quit out of vim.
The default file is open in vim in the command prompt window.

The presenter points at the following that is displayed in the server function:

root /usr/share/nginx/html;

He quits the file and moves back to the
stevescott@ss-vb:/var/www command prompt and runs the following command:

sudo vim /etc/nginx/sites-available/default

As a result, the default file is open in vim.

Next he points at the following:

server {
listen 80 default_server;
listen [::]:80 default_server ipv6only=on;
root /usr/share/nginx/html;
index index.html index.htm;

Next he modifies the code statement root /usr/share/nginx/html; as follows:

root /var/www/default;

He then saves the changes and returns to the command prompt.

Now after we make these changes, one more thing before I restart the server, so we need to restart the service. So I suppose I can do that now, sudo service nginx restart, and then we'll restart it with our new configuration that we modified when we modified this file. So it's restarting. It tells me that it's OK. If we made a mistake, it will fail to restart. I'm going to go into default. I'm going to create a file called index.html file and I'll put some text in it, Hello, World!, the usual. And now if I open up the browser, it shouldn't show...it won't show me the welcome message anymore. It should show me Hello, World! And if you see the previous message like I did quite quickly, just do a Ctrl+R to force a Refresh in Firefox to make sure you don't get a cached version of the page and you can get the new version. So it's serving our new Hello, World! file out of the /var/www/default$ directory. And that's our basic setup and install of nginx. Now if you'd like to run it on a different port, like I mentioned earlier, if you're already running Apache or some other web server, let's go back in and edit this,
The stevescott@ss-vb command prompt window is displayed with the following command prompt:

stevescott@ss-vb:/var/www$

The presenter runs the following command:

sudo service nginx restart

As a result, the following output is displayed:

* Restarting nginx nginx [OK]

Next he runs the following command:

cd default

As a result, the command prompt changes to the following:

stevescott@ss-vb:/var/www/default$

Next he runs the following command:

vim index.html

As a result, the index.html file is open in vim.

Next he adds the following text in the index.html file:

Hello, World!

Then he saves the file and returns to the command prompt and runs the following command:

sudo vim /etc/nginx/sites-available/default

As a result, the default file is open in vim.

Next he modifies the code statement listen 80 default_server; as follows:

listen 8080 default_server;

Next he modifies the code statement listen [::]:80 default_server ipv6only=on; as follows:
listen [::]:8080 default_server ipv6only=on;

He then saves the changes and returns to the command prompt.

and here it's listening on port 80. We could change this to something else, let's say, port 8080, for example, and we'll change it here as well. And we'll write this again, then restart our service, saw this arrow up, sudo service nginx restart. Now if I go back to the web browser and Refresh it, add local, if I type in localhost, it will probably give me an error or a problem. It can't connect because it's no longer running on the default port. And the way we specify the new port is by typing our domain name or IP address, colon, the port number, and here it's as easy as that. So Hello, World! running on a web server on port 8080. And you can do this if you have multiple web servers running and you want to avoid any conflict over. If the two services are fighting over port 80, you'll have a problem and you can avoid it by changing the port. And that will conclude this introduction to getting up and running with nginx.
The stevescott@ss-vb command prompt window is displayed with the following command prompt:

stevescott@ss-vb:/var/www/default$

The presenter runs the following command:

sudo service nginx restart

As a result, the following output is displayed:

* Restarting nginx nginx [OK]

He then opens the Firefox browser window and enters the address 'localhost' in the address bar.

As a result, the web page displays the following text:

Unable to connect

He then enters the address 'localhost:8080' in the address bar.

As a result, the web page displays the following text:

Hello, World!

2. Video: Introduction to MariaDB (it_lugsub_05_enus_02)

During this video, you will learn how to install MariaDB to replace MySQL.
Objectives
install MariaDB as a drop-in replacement for MySQL
Since my SQL was acquired by Oracle, developers forked the original code and created MariaDB, a drop-in replacement for MySQL. Basically MariaDB is the free software, purest version of MySQL with a GNU GPL license. Software that works with MySQL also works with MariaDB. In this video, I'll demonstrate how to install and configure MariaDB in Ubuntu. So let's install both the client and server for MariaDB by sudo apt-get install mariadb-client mariadb-server. Put in our apt password for sudo. I did it wrong. Let's try to type that a little more slowly, there we go. So it gives me all of the packages it would like to install for installing MariaDB. Now I'll give it some password, pick something that's secure and you'll remember. I might pick a shorter one in my case just for this demonstration video, and then hit Ok. Repeat the password, very similar to the MySQL install. And it will go to install the packages and all of its dependencies.
The stevescott@ss-vb command prompt window is displayed in the Ubuntu desktop with the following command prompt:

stevescott@ss-vb:~$

The presenter runs the following command:

sudo apt-get install mariadb-client mariadb-server

The window prompts the presenter with the following question:

Do you want to continue? [Y/n]

The presenter enters the text 'Y' and then presses the Enter key.

The Configuring mariadb-server-5.5 dialog box is displayed with the New password for the MariaDB "root" user text field and the Ok button. He then enters the password and clicks the Ok button. As a result, another dialog box is displayed with the Repeat password for the MariaDB "root" user text field and the Ok button. The presenter enters the password again and then clicks the Ok button.

Now it starts the server and part way through the process, if you already have MySQL installed, you may have problems. It may give you an issue saying that MySQL is not working. Now if I type in mysql, or let's see, mysql --version, it tells me that it's MariaDB. So I am actually running the mysql command, but it's using the MariaDB base or code to do so. This is because, well, how I described it, a drop-in replacement. So a drop-in replacement means it uses the same binary file name, but it's using a different source engine. Now if I type mysql -u, give it root -p. Put in my password, it tells me here I am at MariaDB. I mean I can do whatever, create database some_database; and it will create the database, and this is all through MariaDB working exactly like MySQL. And as you'd seen, I even used mysql to connect to MariaDB. Now I can quit, so I type in quit, and I'm done. And that's all there is to getting up and running with MariaDB as a drop-in replacement for MySQL, and that will conclude this introduction.
The stevescott@ss-vb command prompt window is displayed. From the output displayed, the presenter highlights the following:

* Stopping MariaDB database server mysqld [OK]
chown: cannot access '/var/run/mysqld': No such file or directory
150789 23:28:59 [Note] /var/run/mysqld (mysqld 5.5.44-MariaDB-1ubuntu0.14.04.1) starting as process 12689 ...
* Starting MariaDB database server mysqld [OK]

At the stevescott@ss-vb:~$ command prompt, the presenter runs the following command:

mysql

As a result, the following is displayed:

ERROR 1045 (28000): Access denied for user 'stevescott'@'localhost' (using password: NO)

He then runs the following command:

mysql --version

As a result, the following is displayed:

mysql Ver 15.1 Distrib 5.5.44-MariaDB, for debian-linux-gnu (x86_64) using readline 5.2

Next he runs the following command:

mysql -u root -p

The window prompts the presenter for password. He then enters the password and presses the Enter key.

As a result, the Welcome to the MariaDB monitor message is displayed. Also the command prompt changes to MariaDB [(none)].

He then runs the following command:

create database some_database;

As a result, the following is displayed:

Query OK, 1 row affected (0.00 sec)

Next he runs the following command:

quit

As a result, the following is displayed:

Bye

Also, the command prompt changes back to stevescott@ss-vb:/$.

3. Video: Configuring PHP (it_lugsub_05_enus_03)

In this video, learn how to install and configure php5-fpm.
Objectives
install and configure php5-fpm
In this video, I'll demonstrate the install of the PHP5 FastCGI Process Manager or PHP5-FPM. This will prepare us to run PHP in FastCGI mode behind a web server, such as nginx or Apache. So this is a fresh install. So I'd like to install not just the PHP5-FPM, so install php5-fpm, but I also like to have the php5-cli, the command line interface. So we'll run this. We run our apt-get to install it. It should only take a moment to download and install, and then it also starts. So here at the end, it starts this process, this php5-fpm process. Now if we'd like to install other PHP5 modules, what you could do to figure out which modules do you want to install or what they're called, you could do apt-cache search php5. And it will list quite a long list of other possible modules you can install on top of PHP. Now if you install a new module, it will stop and restart our PHP5-FPM.
The stevescott@ss-vb command prompt window is displayed in the Ubuntu desktop with the following command prompt:

stevescott@ss-vb:~$

The presenter runs the following command:

sudo apt-get install php5-fpm php5-cli

The window prompts the presenter with the following question:

Do you want to continue? [Y/n]

The presenter enters the text 'Y' and then presses the Enter key.

From the output displayed, the presenter highlights the following:

php5-fpm start/running, process16306

Next he runs the following command:

apt-cache search php5

As a result, a list of php5 modules, which can be installed, is displayed.

Now a couple of modules that I install quite often is the php5-curl. So it uses the CURL that you can make external requests to HTTP sites and the GD graphics module here. So it provides us with some graphics functions. So if I scroll down, I can do sudo apt-get install php5-curl php5-gd. So we get this GD graphics library. It's quite handy when you're manipulating images. And you'll see after it installs, after apt installs, it restarts our php5-fpm for us and it starts it sometimes with a new process. Now before we attach this to a web server, which I won't do in this video, but before you attach it to yours, there is one configuration that I always go in and change right away. So we go into our configuration, I can go sudo vim /etc/php5/fpm/php.ini
The stevescott@ss-vb command prompt window with a list of php5 modules, which can be installed, is displayed. The presenter highlights the following:

php5-curl - CURL module for php5
php5-gd - GD module for php5

At the command prompt, stevescott@ss-vb:~$, the presenter then runs the following command:

sudo apt-get install php5-curl php5-gd

From the output displayed, the presenter highlights the following:

php5-fpm start/running, process16839

Next he runs the following command:

sudo vim /etc/php5/fpm/php.ini

As a result, the php.ini file is open in vim.

and I'm going to search for ?cgi-fix-pathinfo, it's cgi.fix-pathinfo, all one word. Now we go here and we uncomment that out, and we'll make sure it's set to 0. The default is 1, but it's a possible security risk because it describes the "behaviour" here, but basically PHP tries to process a file request as near as possible instead of exact only. So you don't want any near misses processing a file. This could open your system up to some security problems. So I recommend going in and changing this to fix_pathinfo=0. So it's the first thing you should do. And then we save it and we'll do sudo service php5-fpm restart. And that will restart the service with this change made in our INI file. And that will conclude this introduction to installing PHP5 FastCGI Process Manager or PHP5-FPM.
The php.ini file is open in vim. The presenter runs the following command:

?cgi.fix-pathinfo

As a result, the cursor points at the following code statement in the file:

;cgi.fix-pathinfo=1

The presenter modifies the code statement as follows:

cgi.fix-pathinfo=0

He then saves the file and returns to the stevescott@ss-vb:~$ command prompt.

Next he runs the following command:

sudo service php5-fpm restart

As a result, the following is displayed:

php5-fpm start/running, process16916

4. Video: Introduction to the Basic LEMP Stack (it_lugsub_05_enus_04)

In this video, you will learn how to configure a basic LEMP (Linux, nginx, MariaDB, PHP) stack.
Objectives
configure a basic LEMP (Linux, nginx, MariaDB, PHP) stack
In this video, I'm going to demonstrate how to set up a basic LEMP stack. So the initialism is L-E-M-P as opposed to the usual L-A-M-P for LAMP, where LAMP is Linux, Apache, MySql, and PHP. In our case LEMP stands for, well, L for Linux, in our case, Ubuntu; E for nginx; M for MariaDB; and P for PHP. So MariaDB is a drop-in replacement for MySQL. So to connect it to PHP, we can just use the PHP MySQL package. So we will install that now, sudo apt-get install php5-mysql. And once this installs, we'll edit the PHP5 FastCGI Process Manager, or FPM, configuration to make sure it's using our PHP5-FPM socket. So let's do sudo vim /etc/php5/fpm/pool.d/www.conf and we'll search for ?listen = ,
The Ubuntu desktop is displayed and includes the launcher with icons such as Files, Ubuntu Software Center, Firefox Web Browser, and System Settings. The stevescott@ss-vb:~ terminal window is displayed on the Ubuntu desktop. The stevescott@ss-vb:~ terminal window includes the following command prompt: stevescott@ss-vb:~$.

The presenter runs the following command at the stevescott@ss-vb: command prompt:

sudo apt-get install php5-mysql

As a result, the PHP MySQL package is installed.

He runs the following command at the stevescott@ss-vb: command prompt:

sudo vim /etc/php5/fpm/pool.d/www.conf

As a result, the following output is displayed:

; Start a new pool named 'www'.
; the variable Spool can we used in any directive and be replaced by the
; pool name ('www' here)
[www]
; Per pool prefix
; It only applies on the following directives:
; - 'slowlog'
; - 'listen' (unixsocket)
; - 'chroot'
; - 'chdir'
; - 'php values'
; - 'php admin values'

He then enters the following command at the stevescott@ss-vb: command prompt:

listen = /var/run/php5-fpm.sock

and we want to make sure that this is running exactly as it's shown here. So that's php5-fpm.sock. Now you can specify a particular IP address and port number to use to accept the FastCGI requests on, but in this case, we just want this Unix socket specified here. So this is a good value to check. I prefer to have it here as php5-fpm.sock. You can also change it to an IP address and port number. So now that we've verified this, let's verify our nginx configuration. Now we'll go to sudo vim /etc/nginx/sites-available and we'll edit the default configuration. So we'll go down and we want to leave a lot of this to the same. Our root for our web server is /var/www/default where since we're using PHP, this index, we want the default file. So if there is no file specified, when loading the site, we want the default to be index.php as opposed to index.html or index.htm.
The stevescott@ss-vb:~ terminal window is displayed on the Ubuntu desktop. The presenter explains the following command:

listen = /var/run/php5-fpm.sock

Then he runs the following command:

:q

He then runs the following command at the stevescott@ss-vb: command prompt:

sudo vim /etc/nginx/sites-available/default

As a result, the following partially visible configuration output is displayed:

server {
listen 80 default_server;
listen [::];80 default_server ipv6only-on;
root /var/www/default;
index index.html index.htm;

The presenter modifies the command index index.html index.htm; as follows:

index index.php index.html index.htm;

The server_name, we're just running it on localhost. We could change this to a different domain name if we're putting it somewhere like some website.com, but since we're just running from localhost, we'll leave that as is. We'll leave the location and all these other configurations the same until we get to the PHP section. So the current install of nginx has this location with the \.php$ designation. So this is saying that in all locations, anything that ends in .php, we want to put through this FastCGI process. So actually it's not that one, so there is fastcgi_pass. We want to keep that commented out. So this way, as I mentioned with the previous setting where you have an IP address and a port number, but in our case, we have a Unix sock, so we want to remove these comments all the way to the bottom.
The stevescott@ss-vb:~ terminal window is displayed on the Ubuntu desktop. The presenter scrolls down the terminal window to display the following local host configuration:

# Make site accessible from http://localhost/
server name localhost;
location / {
# First attempt to serve request as file, then
# as directory, then fall back to displaying a 404.
try_files $uri $uri/ =404;
# uncomment to enable naxsi on this location
# include /etc/nginx/naxsi.rules
}
# Only for nginx-naxsi used with nginx-naxsi-ui : process denied request
#location /RequestDenied {
# proxv_pass http://127.0.0.1:8080;
#}
#"error_page 404 /404.html;
# redirect server error pages to the static page /50x.html
#
#error page 500 502 503 504 /50x.html;
#location - /50x.html {
# root /usr/share/nginx/html;
#}

# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#
#location - \.php$ {
# fastcgi_split_path_info ^(.+\.php)(/.+)$;
# # NOTE: u should have "cgi.fix pathinfo = 0;" in php.ini

He scrolls further down the window and displays the following:

#
# # With php5-cgi alone:
# fastcgi_pass 127.0.0.1:9000;
# With php5-fpm:
# fastcgi_pass unix:/var/run/php5-fpm.sock;
# fastcgi_index index.php;
# include fastcgi_params;
#}

He then removes the comments '#' for the following commands:

location - \.php$ {
fastcgi_split_path_info ^(.+\.php)(/.+)$;
fastcgi_pass unix:/var/run/php5-fpm.sock;
fastcgi_index index.php;
include fastcgi_params;
}

So we have our fastcgi_pass, our fastcgi_index index.php; and we have our fastcgi_params. So these are the standard parameters or server parameters that are used by CGI, passed to it by the web server, in this case nginx. So this is all we need to uncomment to have nginx pass off any PHP files to the FastCGI, the SPHP5-FPM. Alright, now we can save this and quit out, and then we restart the service, so sudo service nginx restart. And now we need to connect MariaDB. So we'll do mysql to launch MariaDB because it's a drop-in replacement and I'm going to log in as root, which I've set up a password for. Now we're connected to MariaDB. I'm going to create a database, create database lemp_test;
The stevescott@ss-vb:~ terminal window is displayed on the Ubuntu desktop. The presenter runs the :wq command to quit the Terminal window. He then runs the following command at the stevescott@ss-vb:~ command prompt:

sudo service nginx restart

As a result, the following output is displayed:

* Restarting nginx nginx

He then runs the following command at the stevescott@ss-vb:~ command prompt:

mysql -u root -p

As a result, the presenter is prompted to enter the password:

Enter password:

He enters the password and as a result, a connection to the MariaDB is made. The following command prompt is displayed at the MariaDB screen:

MariaDB [(none)]>

The presenter runs the following command at the MariaDB [(none)] command prompt:

create database lemp_test;
As a result, the following message is displayed:

Query OK, 1 row affected (0.02 sec)

now I'll create user. I'm going to call this user 'phpuser' and it's a local host user, so I add 'localhost'. So this user can only connect from a local computer identified by some password. Now I can put in some random password, and I'm going to copy this text, so I can paste it into my PHP file. Copy, and now I need to give this user permission. So you can't just create a user and be done with it. It needs permissions on our lemp_test database that we've created. So I'm going to grant some selective permissions, select,insert,update,delete. So I'm going to leave things like or omit things like dropping, or writing privileges, or creating users, or creating or dropping databases. My recommendation is that your user connecting from PHP, since it's opened to the web, should have a somewhat more limited access to your database. And usually select,insert,update,delete will do.
The stevescott@ss-vb:~ terminal window is displayed on the Ubuntu desktop. The presenter runs the following command at the MariaDB [(none)] command prompt:

create user 'phpuser'@'localhost' identified by '3ubrobfd0h1324h'

As a result, the following message is displayed:

Query OK, 0 row affected (0.03 sec)

He then copies the text 3ubrobfd0h1324h from the create user 'phpuser'@'localhost' identified by '3ubrobfd0h1324h' command.

He then enters the following incomplete command at the MariaDB [(none)] command prompt:

grant select,insert,update,delete on

Or in some other cases, people recommend or tutorials recommend grant all privileges. I prefer not to do that, so select,insert,update,delete covers 99% of your cases from PHP. Okay, that diversion aside, let's finish this off. So grant select, insert, update, delete on the database named lemp_test.*, which means all tables, to 'phpuser'@'localhost'. Now we can flush privileges; and quit out. Now let's go into our index.php, which I have already created, so vim /var/www/default/index.php. So this is the file that's going to be served by nginx and processed by our PHP-FPM. So we're connecting mysqli, so we're connecting to the database on 'localhost' with 'phpuser',
The stevescott@ss-vb:~ terminal window is displayed on the Ubuntu desktop. The presenter completes the grant select,insert,update,delete command on the MariaDB [(none)] command prompt:

grant select,insert,update,delete on lemp_test.* to 'phpuser' @'localhost';

As a result, the following output is displayed:

Query OK, 0 row affected (0.01 sec)

He then runs the following command at the MariaDB [(none)] command prompt:

flush privileges;

As a result, the following output is displayed:

Query OK, 0 row affected (0.00 sec)

He then runs the quit command at the MariaDB prompt, and as a result, the message Bye is displayed.

As a result, the stevescott@ss-vb: command prompt is enabled.

He then runs the following command at the stevescott@ss-vb: command prompt:

vim /var/www/default/index.php

As a result, the presenter enters the index.php screen and the following output is displayed:

<?php
$dbo = new mysqli('localhost', 'phpuser', '');
echo 'select_db returned: '.$dbo->select_db('lemp_test');
$dbo->close();
?>

and I'm going to insert the password that I created for this user on this database server, and then I'm going to echo out the 'select_db returned: '. So this select_db call on our database object to 'lemp_test', so if it can connect, it will return true. If not, it will return false, or 1, or 0, and then at the end, it will close() the connection. So let me just write this and quit out. Now that's everything. We should be able to open up our Firefox Web Browser, browse to 'localhost', and it should process that index.php and make that connection to the Maria database; select_db returned: 1 for true. So the connection was fine, and we know now that everything has been configured correctly. And that concludes this introduction to setting up a basic LEMP stack.
The index.php window is open in the stevescott@ss-vb:~ terminal window displayed on the Ubuntu desktop. The presenter modifies the command $dbo = new mysqli('localhost', 'phpuser', ''); as follows:

$dbo = new mysqli('localhost', 'phpuser', '3ubrobfd0h1324h ');

He then explains the following command:

echo 'select_db returned: '.$dbo->select_db('lemp_test');
$dbo->close();

He then runs the :wq command to quit from the index.php window. As a result, the message Bye is displayed and the stevescott@ss-vb: command prompt is enabled.

Now he navigates to the Google Chrome browser window. In the address bar, he enters the following text: localhost. As a result, the following output is displayed:

select_db returned: 1

5. Video: Installing a Basic SSL/TLS Certificate in nginx (it_lugsub_05_enus_05)

In this video, you will learn how to create a certificate signing request and self-sign it using openssl.
Objectives
create a certificate signing request and self-sign it with openssl
If you need users to connect securely to your web site with an HTTPS connection, you need an SSL or TLS certificate. In this video, I'll demonstrate how to create the keys required with OpenSSL for an HTTPS connection in nginx. So we have our nginx web server installed and running, and we have OpenSSL installed, so we can proceed to use it. We'll do openssl genrsa. So we're going to create an RSA certificate using -des encryption or -des3 encryption. The 3 is very important. And we're going to write the file -out to something called myhostname.key. Now I'll just leave it as myhostname, in this case for this example, and then you pick the size of your certificate. It has to be a minimum 2048, but you can specify 2048 or 4096.
The Ubuntu desktop is displayed. It includes the Launcher displayed vertically on the left, which includes icons such as Dash Home, Firefox, Settings, and Recycle bin. On the Ubuntu desktop, the stevescott@ss-vb: ~ terminal window is displayed. It contains the following command prompt:

stevescott@ss-vb:~/$

At the stevescott@ss-vb:~/$ command prompt, the presenter enters the following command:

openssl genrsa -des3 -out myhostname.key 4096

So this is a 2k or 4k signature. I wouldn't go higher than 4096-bit. It's really unnecessary. So this is the maximum you should put for your key. We enter a pass phrase and we confirm it, pick something secure. And now we have a key called myhostname.key. Now we also need to make a signing request. So typically your certificate is signed by a signing authority, a certificate authority, or a CA, to verify your identity. We're not going to quite go that far in this example, but we still need the certificate signing request that we can sign ourselves. So we're going to create a new request, so req –new –key. We specify our myhostname.key, and then we output our certificate signing request, which we'll call .csr, so myhostname.csr. So we put in our pass phrase for myhostname.key that we set above. Then we specify our country code, whatever it may be. I am in Canada, I can put CA, our state or province, the city, the organization name, the organizational unit, if required, the common name. So this is our myhostname or, you know, something.com. We put here email address you can put in, and you can specify a password and a company name optionally.
The stevescott@ss-vb:~ terminal window is displayed. At the stevescott@ss-vb:~/$ command prompt, the presenter runs the following command:

openssl genrsa -des3 -out myhostname.key 4096

The following output is displayed:

Generating RSA private key, 4096 bit long modulus
e is 65537 (0x10001)
Enter pass phrase for myhostname.key:

Next he enters the pass phrase and the following text is displayed:

Verifying - Enter pass phrase for myhostname.key

Then he re-enters the pass phrase and confirms it. Now he runs the following command at the stevescott@ss-vb:~/$ command prompt:

ls

As a result, a list of files and directories in current working directory is displayed as output. He highlights the myhostname.key file.

Now he runs the following command at the stevescott@ss-vb:~/$ command prompt:

openssl req -new -key myhostname.key -out myhostname.csr

The following text is displayed:

Enter pass phrase for myhostname.key:

He then enters the pass phrase and the following text is displayed:

You are about to be asked to enter information that will be incorporated into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.

Country Name (2 letter code) [AU]:

He enters CA and the following fields are displayed as he presses the Enter key:

State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Common Name (e.g. server FQDN or YOUR name) []:

He enters myhostname and then presses the key. The following is displayed:

Email Address []:Please enter the following 'extra' attributes to be sent with your certificate request
A challenge password []:
An optional company name []:

Okay, so this should have created our CSR file, which we see here, myhostname.csr. I'm not too concerned about the information here because we're going to self-sign it in this video, but if you're using a Registrar for an SSL certificate or a TLS certificate, now I use and most people use SSL and TLS interchangeably, where at the moment the SSL is somewhat outdated and TLS is the technology we're using now. But if I use them interchangeably like most people, just assume we're using TLS because that's what we're going to tell our server to use because SSL is no longer secure. Okay, that digression aside, let's continue on with creating our keys required for nginx. Okay, now the key file that I have is protected by a password.
The stevescott@ss-vb:~ terminal window is displayed. The presenter runs the following command at the stevescott@ss-vb:~/$ command prompt:

ls

As a result, a list of files and directories in current working directory is displayed as output. He highlights the myhostname.csr file.

If we are going to use this in nginx, every time the server starts or restarts, we need to specify the password for our key. Now we don't want to do that. So we're going to remove the password. So I'm going to make a copy of myhostname.key and I'm going to call this version myhostname.key.pw for password. So the password version is going to have a .pw extension after it. And then we can do openssl rsa because that's the type of key. The input is myhostname.key.pw and the output is myhostname.key, which will overwrite the previous one with this password-versionless one. But to do so, we need to enter the password. And now it writes the key, this new key file myhostname.key. Now it does not require a password, okay. Once we get to this point, we typically take this myhostname.key or the contents of it, which I can output myhostname.csr.
The stevescott@ss-vb:~ terminal window is displayed. The presenter runs the following command at the stevescott@ss-vb:~/$ at the command prompt:

cp myhostname.key myhostname.key.pw

Next he runs the following command at the stevescott@ss-vb:~/$ command prompt:

openssl rsa -in myhostname.key.pw -out myhostname.key

The following output is displayed:

Enter pass phrase for myhostname.key.pw:

Then he enters the pass phrase and the following is displayed:

writing RSA key

Then he runs the following command at the stevescott@ss-vb:~/$ command prompt:

ls

As a result, a list of files and directories in current working directory is displayed as output. He highlights the myhostname.csr file. He now runs the following command at the stevescott@ss-vb:~/$ command prompt:

cat myhostname.csr

As a result, the certificate request is displayed.

We could either upload or cut and paste this content to a certificate authority to sign it for us, which would give us a valid signed and authenticated key. In this video, we're not going to do that. We're going to do what the certificate authority would do for us, which is sign it. So we need to sign it using something called an x509 certificate or envelope. So this is the type of a certificate we're creating in x509. We're going to make...we're going to do request, -in is the certificate signing request. And it's signed with myhostname.key, our private key and we're going to output myhostname.crt for certificate. So this is the final certificate that we need. And I typed in something wrong here, openssl x509 -req -in myhostname.csr -signing myhostname.key –out myhostname.crt. So I typed in something wrong here. Let me go up and see what I typed in. My x509 requires -signkey, not -signing, -signkey. There we go.
The stevescott@ss-vb:~terminal window is displayed. The presenter runs the following command at the stevescott@ss-vb:~/$ command prompt:

openssl x509 -req -in myhostname.csr -signkey myhostname.key -out myhostname.crt

The following output is displayed:

Signature ok
subject=/C=CA/ST=Some-State/0=Internet Widgits Pty Ltd/CN=myhostname
Getting Private key

So openssl x509 is the type of certificate, our request is coming -in from myhostname.csr. We're signing it with myhostname.key and we're outputting myhostname.crt. So that should give us a key file and a CRT file, which we can use in nginx. Now I like the recommendation to store the SSL certificates under the nginx configuration directory. So we'll do sudo mkdir /etc/nginx/ssl to store the certificates, so they are not mixed up with the general certificates on our system. So make password, so [sudo] password, so we've made to the directory and now we can copy, sudo, copy myhostname.crt to /etc/nginx/ssl and we also want to copy myhostname.key. Now we can edit the configuration in nginx, so sudo vim/etc/nginx/sites-available and we're going to edit the default configuration. And we're going to go down in this default configuration all the way to the end right here for the HTTPS server. And we're going to uncomment this whole section here without breaking it, server, let's put that back where it was.
The stevescott@ss-vb:~terminal window is displayed. The presenter
runs the following command at the stevescott@ss-vb:~/$ command prompt:

sudo mkdir /etc/nginx/ssl

The following text is displayed:

[sudo] password for stevescott:

He enters the sudo password.

Now he runs the following commands at the stevescott@ss-vb:~/$ command prompt one after the other:

sudo cp myhostname.crt /etc/nginx/ssl
sudo cp myhostname.key /etc/nginx/ssl
sudo vim /etc/nginx/sites-available/default

The default configuration is displayed. The presenter scrolls down the output to view the below code segment:

# HTTPS server
#
# server {
# listen 443;
# server_name localhost;
#
# root html;
# index index.html index.htm;
#
# ssl on;
# ssl_certificate cert.pem;
# ssl_certificate_key cert.key;
#
# ssl_session_timeout 5m;
#
# ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;
# ssl_ciphers "HIGH: !aNULL: !MD5 or HIGH: !aNULL: !MD5: !3DES";
# ssl_prefer_server_ciphers on;
#
# location / {
# try_files $uri $uri/ =404;
# }
# }

He removes the # symbol to uncomment these code lines.

So we want ssl on; so ssl_certificate, in this case, it's specifying cert.pem. We want to go /etc/nginx. We'll specify the full path, /ssl/myhostname.crt. So often here this ssl_certificate will either be a CRT file or a PEM file, and then our key file that's /etc/nginx/ssl/myhostname.key. And we can go through, allow these protocols. Now at the moment, it's recommended to remove the SSLv3 protocol because it's insecure and just use the TLSv1, TLSv1.1, and TLSv1.2 and we want to make sure we don't use certificates with MD5, so it's giving us...making some instructions not to use insecure certificates or allowing secure signing. And we'll uncomment this.
The default configuration is displayed in the stevescott@ss-vb:~ terminal window. The presenter uncomments and modifies default configuration as follows:

# HTTPS server
#
server {
listen 443;
server_name localhost;
#
root html;
index index.html index.htm;
#
ssl on;
ssl_certificate /etc/nginx/ssl/myhostname.crt;
ssl_certificate_key /etc/nginx/ssl/myhostname.key;
#
ssl_session_timeout 5m;
#
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_ciphers "HIGH: !aNULL: !MD5 or HIGH: !aNULL: !MD5: !3DES";
ssl_prefer_server_ciphers on;
#
location / {
try_files $uri $uri/ =404;
}
}

So this will...we need to change our root location. Our web server, in this case, is at /var/www/default and it's going to serve the HTML file out of that location. Now we can add other things to this like PHP, but in this demo, we'll just leave the HTML file served through. So if we put in HTTPS localhost, it will serve the index.html. So let's write this and quit, and restart the nginx, so sudo service nginx restart and it performs OK. So we know our settings were correct. Now I'm just going to output the HTML file, /var/www/default/index.html, so we can see,
The default configuration is displayed in the stevescott@ss-vb:~terminal window. The presenter modifies the root web server location as follows:

root /var/www/default;

Next he enters :wq to save and exit the file.

The he runs the following command at the stevescott@ss-vb:~/$ command prompt:

sudo service nginx restart

The following output is displayed:

* Restarting nginx nginx

Now he runs the following command at the stevescott@ss-vb:~/$ command prompt:

cat /var/www/default/index.html

The following output is displayed:

Hello, World!

so the file it should serve over HTTPS is Hello, World! Now open up our Firefox Web Browser, https://localhost. Now it says, "This Connection is Untrusted" because we self-signed the certificates. Now if we had a certificate authority do it and Firefox had that certificate authority's root certificate already installed, then it wouldn't show this to us. But I Understand the Risks. I'll Add Exception for the certificate we created. We'll Confirm Security Exception and it serves Hello, World! And that's all there is to it. And that will conclude this demonstration of installing an SSL or a TLS certificate in nginx.
The stevescott@ss-vb:~terminal window is displayed. The presenter clicks the Firefox icon from the Launcher and the Firefox web browser window is displayed. In this window, in the address bar, he enters https://localhost. The following output is displayed:

This connection is Untrusted

In this window, at the bottom of the page, Technical Details and I Understand the Risks nodes are also displayed. He expands the I Understand the Risks node and scrolls down to display the Add Exception button. He then clicks the Add Exception button. As a result, the Add Security Exception dialog box is displayed.

This dialog box includes the Server Location text field with the default value https://localhost. It also include the Permanently store this exception checkbox, which is selected by default, and the Confirm Security Exception button. He clicks the Confirm Security Exception button. As a result, in the Mozilla Firefox browser window, the following text is displayed:

Hello, World!

6. Video: Managing /etc/hosts for Web Development (it_lugsub_05_enus_06)

In this video, find out how to modify the /etc/hosts file to point a domain to a local web server.
Objectives
modify the /etc/hosts file to point a domain to a local web server
In this video, we'll create a web development environment on our local server stack that simulates our production web environment. To do this, we'll modify our /etc/hosts file to redirect our domain locally. So the web server I have running is nginx. Now say we download a domain configuration from nginx from a production server. So from our web servers running on something, let's say example.com. So I have this vim example.ngx, for nginx, this configuration for nginx. So this tells it...it says that we're running the server on example.com and it's serving at root /var/www/example and it's running on port...it's listing on port 80 for this site. Now that we have that, let's say we've downloaded this from our server example.com and we want to run it locally and test and develop a new web site before we upload it to our production server. So we'll quit out of this, now we want to make sure that we have...we'll need sudo mkdir /var/www/example. And now we want to change the ownership, so change group to www-data var/www/example –
The Ubuntu desktop is displayed. The desktop includes a Launcher, which contains icons such as Mozilla Firefox, Amazon, Settings, and Search. In addition, the stevescott@ss-vb: ~terminal window is open on the Ubuntu desktop. It contains the following command prompt:

stevescott@ss-vb:~$

The presenter runs the following command at the stevescott@ss-vb:~$ command prompt:

vim example.ngx

As a result, the following output is displayed:

server {
listen 80;
listen [::]:80;
root /var/www/example;
index index.html;
server_name example.com;
location / {
try_files $uri $uri/ =404;
}
}

"example.ngx" 13L, 158C

He refers to the following lines of the above output:

server_name example.com;
root /var/www/example;
listen 80;
listen [::]:80;

The presenter then runs the command ':q' at the end of the file and returns to the stevescott@ss-vb: ~terminal window.

Then he runs the following command at the stevescott@ss-vb:~$ command prompt:

sudo mkdir var/www/example

Next he runs the following command at the stevescott@ss-vb:~$ command prompt:

sudo chgrp www-data /var/www/example

and now we can do the sudo vim /var/www/example. And this is where our index.html should reside. We could say, "Hello from example.com!" which is running locally. Now to do so we need to copy this configuration file into our nginx config locally, so we can do sudo cp example.ngx /etc/nginx/sites-avialable. Now this just puts it in the available sites. It's not in the enabled sites, where nginx will look to try and load the configuration when it's restarted. So to do that we'll create a symbolic link, sudo ln -s, our source file, which is now /etc/nginx/sites-available/example.ngx and we'll put this link in our destination, /sites-enabled/example.ngx. So that created our link. Now before we start our service, well, we need to modify our host files, so sudo vim /etc/hosts.
On the Ubuntu desktop, the stevescott@ss-vb:~terminal window is displayed. The presenter runs the following command at the stevescott@ss-vb:~$ command prompt:

sudo vim /var/www/example/index.html

As a result, the 'index.html' file is opened in the terminal window. He enters the text 'Hello from example.com!' in the index.html file.

Then he runs the ':wq' command at the end of the file and returns to the stevescott@ss-vb:~ window.

Next he runs the following command at the stevescott@ss-vb:~$ command prompt:

sudo cp example.ngx /etc/nginx/sites-available

Now he runs the following command at the stevescott@ss-vb:~$ command prompt:

sudo ln -s /etc/nginx/sites-available/example.ngx /etc/nginx/sites-enabled/example.ngx

Then he runs the following command at the stevescott@ss-vb:~$ command prompt:

sudo vim /etc/hosts

As a result, the following output is displayed:

127.0.0.1 localhost
127.0.1.1 ss-vb
# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
"/etc/hosts" 9L, 220C

And we want to tell our host file that when our computer sees example.com, instead of going out to the web and looking up the DNS entry for this, well, it's going to intercept it before it gets out far and redirect to "127.0.0.1" our local computer and our local version of nginx. So let's save this, and write it, and quit. Okay, so now that we've saved that, we can restart nginx because we put our new configuration for example.com in. So sudo service nginx restart, it's restarted okay. So now, if we go to our web browser...now, if we go to localhost, it returns whatever is running on localhost right now. So this is from some other example, from some other directory. So if I look in ls /var/www/default, it's serving this index.php.
On the Ubuntu desktop, the stevescott@ss-vb:~ terminal window is displayed with the following output:

127.0.0.1 localhost
127.0.1.1 ss-vb
# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
"/etc/hosts" 9L, 220C

The presenter modifies the line '127.0.0.1 localhost' as follows:

127.0.0.1 localhost example.com

He then runs the ':wq' command at the end of the file and returns to the stevescott@ss-vb:~ terminal window.

Then he executes the following command at the stevescott@ss-vb:~$ command prompt:

sudo service nginx restart

As a result, the following output is displayed:

* Restarting nginx nginx [ OK ]

He then selects the Firefox icon from the Launcher. As a result, the Firefox browser window is displayed. He enters the address 'localhost/' in the address bar. As a result, the http://localhost/ web page is displayed and it contains the following text:

select_db_returned: 1

He then navigates to the stevescott@ss-vb:~ terminal window and runs the following command at the stevescott@ss-vb:~$ command prompt:

ls /var/www/default

As a result, the following output is displayed:

index.html index.php

He refers to 'index.php' in the above output.

But if I go to "example.com", our host file will redirect it locally and it will be served from nginx out of ls /var/www/example and the file it's serving is /example/index.html. So this matches up what our very web browser is serving. So let's say we make changes to this...our web site here locally. We FTP it or copy it to some remote server, to the real example.com out there on some web server. So after we do that, we go back into our etc/ host file, remove this example.com from our localhost here. So we remove example.com from our host file.
On the Ubuntu desktop, the stevescott@ss-vb:~ terminal window is displayed. The presenter navigates to the http://localhost/ web page displayed in the Firefox browser window and modifies the address in the address bar as follows:

example.com

He then reloads the 'example.com' page. As a result, the following output is displayed:

Hello from example.com!

Next he navigates to the stevescott@ss-vb:~ terminal window and runs the following command at the stevescott@ss-vb:~$ command prompt:

ls /var/www/example

As a result, the following output is displayed:

index.html

Then he runs the following command at the stevescott@ss-vb:~$ command prompt:

cat /var/www/example/index.html

As a result, the following output is displayed:

Hello from example.com!

Next he runs the following command at the stevescott@ss-vb:~$ command prompt:

sudo vim /etc/hosts

As a result, the following output is displayed:

127.0.0.1 localhost example.com
127.0.1.1 ss-vb
# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
"/etc/hosts" 9L, 232C

He modifies the line '127.0.0.1 localhost example.com' as follows:

127.0.0.1 localhost

He then runs the ':wq' command at the end of the file and returns to the stevescott@ss-vb:~ terminal window.

And then if we type it in again, it will go to the actual web site, example.com. I might have to restart Firefox for that to take effect. And if I do example.com, still seeing the local...I might have to restart. But when you make that change, when you remove it from your host file, let me exit...I'll log out and log in again just to verify this. I'll Log Out. Now when we log back in, we'll load up our web browser. We'll type in "example.com" and it loads the actual contents of the example.com web site. And that concludes this demo on local domains through the /etc/hosts file and setting up a web site in nginx.
On the Ubuntu desktop, the stevescott@ss-vb:~ terminal command prompt window is displayed. The presenter navigates to the http://example.com/ web page displayed in the Firefox browser window. He reloads the web page.

As a result, the following output is displayed:

Hello from example.com!

He then closes the Firefox browser window and restarts it. He enters the address 'example.com/' in the address bar. As a result, the following output is displayed:

Hello from example.com!

He then closes the Firefox browser window and navigates to the stevescott@ss-vb:~ terminal window. He runs the following command at the stevescott@ss-vb:~$ command prompt:

sudo vim /etc/hosts

As a result, the following output is displayed:

127.0.0.1 localhost
127.0.1.1 ss-vb
# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
"/etc/hosts" 9L, 221C

He then runs the ':wq' command at the end of the file and returns to the stevescott@ss-vb:~$ terminal window. He runs the 'exit' command to close the terminal window and Logs out of the System and Logs in again.

He then selects the Firefox web browser icon from the Launcher and the Firefox browser window is displayed. He enters the address 'example.com/' in the address bar. As a result, the following output is displayed:

Example Domain
This domain is established to be used for illustrative examples in documents. You may use this domain in examples without prior coordination or asking for permission.

More information...

7. Video: Exercise: Introduction to avconv (it_lugsub_05_enus_07)

During this video, you will learn how to use avconv to convert video formats and extract audio from a video file.
Objectives
use avconv to format shift video formats and extract audio from a video file
Exercise Overview

Avconv is the audio video converter supported by Ubuntu. In this exercise, we'll perform a few basic format conversions of audio and video using avconv. So in this exercise, we'll first start by making sure we have it installed using apt or the Ubuntu Software Centre. Then we'll extract an audio track from a movie file and save it as an mp3. So we have a movie with sound that we want to just have the sound, so extract it to an audio file. Then we'd like to take a movie file in one format, say, ogg, or avi, or Windows Media format and convert it to an mp4. And finally, we'd like to extract a still image from a movie file at a particular point in time, for example, 10 seconds into the movie, extract the current frame. Now pause this video and perform the exercise, then you can come back and see how I did it.

Solution

So let's get started by opening up a Terminal. So here I want to run avconv. Now if I just type in the name, it tells me it's not installed, but I can install it by typing sudo apt-get install libav-tools. So if you try to do something like sudo apt-get install avconv, it wouldn't work. So it tells me I can't find the package because it comes under this package here, libav-tools. You could also find it by running apt-cache search avconv. And it shows libav-tools as the first result in this search. So I'll do sudo apt-get install libav-tools. Now it will do the install for me and once it's installed, I can now run avconv. Okay, so now I need a video file, so I can carry out the actions in this exercise. Luckily by default, there's one in /usr/share/example-content/ and in Ubuntu_Free_Culture_Showcase/.
The Ubuntu desktop is displayed and includes the Launcher with icons such as Dash Home, Ubuntu Software Center, Firefox Web Browser, and System Settings. The menu bar is displayed at the top of the desktop and contains the window management buttons, the app menus, and the status menus. The status menus include menus such as Input source, Sound, and System. The presenter opens the terminal window which contains the following command prompt:

stevescott@ss-vb:~

At the stevescott@ss-vb:~ command prompt, he runs the following command:

avconv

As a result, the following output is displayed:

The program 'avconv' is currently not installed. You can install it by typing:
sudo apt-get install libav-tools

Then he runs the following command at the stevescott@ss-vb:~ command prompt:

sudo apt-get install avconv

As a result, the following output is displayed:

[sudo] password for stevescott:

The cursor is at the end of the output. He then enters the password and presses the Enter key. As a result, the following output is displayed:

Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package avconv

Next he refers to libav-tools in the following output:

The program 'avconv' is currently not installed. You can install it by typing:
sudo apt-get install libav-tools

Then he runs the following command at the stevescott@ss-vb:~ command prompt:

apt-cache search avconv

As a result, the following output is displayed:

libav-tools - Multimedia player, server, encoder and transcoder
python3-audioread - Backend-agnostic audio decoding Python 3 package
vokoscreen - easy to use screencast creator
winff - graphical video and audio batch converter using ffmpeg or avconv
winff-dbg - winff debugging symbols
winff-doc - winff documentation
python-audioread - Backend-agnostic audio decoding Python package

He then refers to the text libav-tools in the following output line:

libav-tools - Multimedia player, server, encoder and transcoder

Next he runs the following command at the stevescott@ss-vb:~ command prompt:

sudo apt-get install libav-tools

As a result, the output is displayed that indicates that libav-tools is installed.

Then he runs the following command at the stevescott@ss-vb:~ command prompt:

avconv

As a result, the following output is displayed:

avconv version 9.18-6:9.18-0ubuntu0.14.04.1, Copyright (c) 2000-2014 the Libav developers
built on Mar 16 2015 13:19:10 with gcc 4.8 (Ubuntu 4.8.2-19ubuntu1)
Hyper fast Audio and Video encoder
usage: avconv [options] [[infile options] -i infile]... {[outfile options] outfile}...
Use -h to get full help or, even better, run 'man avconv'

Next he runs the following command at the stevescott@ss-vb:~ command prompt:

ls /usr/share/example-content/

As a result, the following output is displayed:

Ubuntu_Free_Culture_Showcase

He then runs the following command at the stevescott@ss-vb:~ command prompt:

ls /usr/share/example-content/Ubuntu_Free_Culture_Showcase/

As a result, the following output is displayed:

How fast.ogg Josh Woodward - Swansong.ogg

So this How fast.ogg is a video file. This other file is an audio file in ogg format. But I am going to copy the video file to my Videos folder, so I can do cp /usr/share/example-content/Ubuntu_Free_Culture_Showcase/How\ fast.ogg, and I'm going to copy that into my Videos folder. So if I cd Videos/ now, I can see I have this video file. Now the first thing was to extract the audio and it's as simple as avconv -i for input. So I specify this input file, and then I just specify the output file, how-fast.mp3. Now we'll see a bit of red here. It doesn't like something, so let's see how far it's going to get into this process, whether this is critical or not. I don't think it likes the video. Now if I want to suppress this, it looks like it may have converted it fine, so we have a file. There's also the exclude video, so disable video if I do -vn and try that again. I'll overwrite the file.
On the Ubuntu desktop, the terminal window is displayed. In this window, the presenter refers to the following output at the stevescott@ss-vb:~ command prompt:

How fast.ogg Josh Woodward - Swansong.ogg

Then he runs the following command at the stevescott@ss-vb:~ command prompt:

cp /usr/share/example-content/Ubuntu_Free_Culture_Showcase/How\ fast.ogg Videos

Next he runs the cd Videos/ command at the stevescott@ss-vb:~ command prompt. As a result, the command prompt changes as follows:

stevescott@ss-vb:~/Videos

He then runs the following command at the stevescott@ss-vb:~/Videos command prompt:

ls

As a result, the following output is displayed:

How fast.ogg

Next he runs the following command at the stevescott@ss-vb:~/Videos command prompt:

avconv -i How\ fast.ogg how-fast.mp3

As a result, the following partial output is displayed:

[mp3 @ 0X1351140] Application provided invalid, non monotonically increasing dts to muxer in stream 0: 2717718 >= 2621622
[mp3 @ 0x1351140] Application provided invalid, non monotonically increasing dts to muxer in stream 0: 2717718 >= 2633634
frame= 553 fps= 23 q=0.0 Lsize= 483kB time=30.23 bitrate= 130.8kbits/s
video:74148kB audio:477kB global headers:0kB muxing overhead -99.353037%

The following lines in the output are in red color:

[mp3 @ 0x1351140] Application provided invalid, non monotonically increasing dts to muxer in stream 0: 2717718 >= 2621622
[mp3 @ 0x1351140] Application provided invalid, non monotonically increasing dts to muxer in stream 0: 2717718 >= 2633634

Then he runs the following command at the stevescott@ss-vb:~/Videos command prompt:

ls

As a result, the following output is displayed:

how-fast.mp3 How fast.ogg

Next he runs the following command at the stevescott@ss-vb:~/Videos command prompt:

ls -la

As a result, the following output is displayed:

total 2364
drwxr-xr-x 2 stevescott stevescott 4096 Jul 24 12:13 .
drwxr-xr-x 22 stevescott stevescott 4096 Jul 24 11:47 ..
-rw-rw-r-- 1 stevescott stevescott 494385 Jul 24 12:14 how-fast.mp3
-rw-r--r-- 1 stevescott stevescott 1915873 Jul 24 12:13 How fast.ogg

He then refers to the following line in the output:

-rw-rw-r-- 1 stevescott stevescott 494385 Jul 24 12:14 how-fast.mp3

Then he runs the following command at the stevescott@ss-vb:~/Videos command prompt:

avconv -i How\ fast.ogg -vn how-fast.mp3

As a result, the following output is displayed:

avconv version 9.18-6:9.18-0ubuntu0.14.04.1, Copyright (c) 2006-2014 the Libav developers
built on Mar 16 2015 13:19:10 with gcc 4.8 (Ubuntu 4.8.2-19ubuntu1)
Input #0, ogg, from 'How fast.ogg':
Duration: 00:00:30.58, start: 0.000000, bitrate: 501 kb/s
Stream #0.0: Video: theora, yuv420p, 1280x720 [PAR 1:1 DAR 16:9], 6.25 fps, 29.97 tbn, 29.97 tbc
Stream #0.1: Audio: vorbis, 44100 Hz, stereo, fltp, 128 kb/s
Metadata:
ENCODER : VLC media player
File 'how-fast.mp3' already exists. Overwrite ? [y/N]

The cursor is at the end of the output. He then enters y and presses the Enter key. As a result, the following output is displayed:

Output #0, mp3, to 'how-fast.mp3':
Metadata:
TSSE : Lavf54.20.4
Stream #0.0: Audio: libmp3lame, 44100 Hz, stereo, fltp
Metadata:
ENCODER : VLC media player
Stream mapping:
Stream #0:1 -> #0:0 (vorbis -> libmp3lame)
Press ctrl-c to stop encoding
size= 479kB time=30.58 bitrate= 128.2kbits/s
video:0kB audio:477kB global headers:0kB muxing overhead 0.381215%

That works a little better. Yes, it didn't like the direct conversion from video to audio without specifying -vn, which is the disable video option. So that's the ideal way of doing it. So if I open up my file manager and go to Videos, I see how-fast.mp3 and if I want to play it, I'll just double-click and it plays it using Rhythmbox, which I can control from the upper corner here. So let me Pause that and go back to our console window or Terminal window here. And converting to an mp4, it's very similar. We can just do avconv -i How\ fast.ogg and our output, we'll call it how-fast.mp4. It gives me an error. It tells me if I want to use this encoder for mp4 for this 'aac' format for the audio format, the default audio format I need to use '-strict experimental'. Now it gives me a bit of a warning, but if I just use -strict experimental and run it again, it seems to work fine. And we'll test the result once it finishes encoding. So it encoded it as an mp4 and if I double-click it, it will open it up in the video player.
On the Ubuntu desktop, the terminal window is displayed. The output after the presenter overwrites how-fast.mp3 is displayed in the terminal window.

On the desktop, the presenter clicks the File Manager icon from the launcher. As a result, the File Manager window is displayed with the contents of the Home location displayed. The left pane of this window contains the following four nodes: Places, Devices, Bookmarks, and Network. The Places node contains subnodes such as Home, Desktop, Documents, Music, Videos, and Trash. The Home subnode is selected by default. The Devices node contains the Computer subnode. The Bookmarks node contains the backup subnode and the Network node contains the following subnodes: Browse Network and Connect to Server.

The right pane of the window contains the contents of Home such as Desktop, Downloads, Pictures, Videos, and Examples.

Next he clicks the Videos subnode in the left pane.

As a result, the right pane now contains the following files: How fast.ogg and how-fast.mp3.

He then double-clicks the how-fast.mp3 file and plays the 'how-fast.mp3' file using the Rhythmbox application.

Then he navigates to the menu bar of the Ubuntu desktop and clicks the Sound menu. As a result, a drop-down menu is displayed. The drop-down menu includes option to set the volume, configure sound settings, and control the Rhythmbox media player.

Next he pauses the how-fast.mp3 audio file from the drop-down menu. He then navigates to the terminal window and runs the following command at the stevescott@ss-vb:~/Videos command prompt:

avconc -i How\ fast.ogg how-fast.mp4

As a result, the following error is displayed in the output:

encoder 'acc' is experimental and might produce bad results.
Add '-strict experimental' if you want to use it.

The presenter refers to the error displayed. Then he runs the following command at the stevescott@ss-vb:~/Videos command prompt:

avconc -i How\ fast.ogg -strict experimental how-fast.mp4

As a result, the following output is displayed:

avconv version 9.18-6:9.18-0ubuntu0.14.04.1, Copyright (c) 2000-2014 the Libav developers
built on Mar 16 2015 13:19:10 with gcc 4.8 (Ubuntu 4.8.2-19ubuntu1)
Input #0, ogg, from 'How fast.ogg':
Duration: 00:00:30.58, start: 0.000000, bitrate: 561 kb/s
Stream #0.0: Video: theora, yuv420p, 1280x720 [PAR 1:1 DAR 16:9], 6.25 fps, 29.97 tbn, 29.97 tbc
Stream #0.1: Audio: vorbis, 44100 Hz, stereo, fltp, 128 kb/s
Metadata:
ENCODER : VLC media player
File 'how-fast.mp4' already exists. Overwrite ? [y/N]

The cursor is at the end of the output. He then enters y and presses the Enter key. As a result, the file is converted and following partial output is displayed:

Metadata:
ENCODER : VLC media player
Stream mapping:
Stream #0:0 -> #0:0 (theora -> libx264)
Stream #0:1 -> #0:1 (vorbis -> aac)
Press ctrl-c to stop encoding
frame= 45 fps= 0 q=0.0 size= 0kB time=7.01 bitrate= 0.1kbits/s

The following output value keeps changing as follows:

frame= 152 fps= 29 q=24.0 size= 887kB time=16.18 bitrate= 440.7kbits/s

Next he navigates to the File Manager window that now displays the contents of Videos as follows: How fast.ogg, how-fast.mp3, and how-fast.mp4.

He then double-clicks the how-fast.mp4 file and it opens in the video player. The Searching for multimedia plugins message box is displayed with the following message and the Cancel button:

Searching for multimedia plugins
Videos requires to install plugins to play files of the following types:
MPEG-4 ACC decoder
H.264 decoder

Now it tells me I need to install plugins to play this type, and luckily Ubuntu prompts me to Install, and I'll just click Install, which should allow it to play. So I can authenticate using my Password, install the required packages, so I can play this mp4. Now I'm not sure if it's still working or not. Let me Close it and reopen it after it installed those, and it works fine. So that's our mp4, so it's a very simple procedure to convert to both, an mp3 and an mp4. Now the final part of this exercise was to extract an image from a particular point in the file. I gave the example of 10 seconds,
The video player is open on the Ubuntu desktop. The Searching for multimedia plugins message box is displayed with the following message with the Cancel button:

Searching for multimedia plugins
Videos requires to install plugins to play files of the following types:
MPEG-4 ACC decoder
H.264 decoder

The message box also includes a progress bar. After the search for multimedia plugins is complete, the message box closes and the Install extra multimedia plugins? window is displayed. This window contains the Cancel and Install buttons and the table with three rows and the following columns: Install, Plugin Package, and Provides. Each row that corresponds to the Install column is associated with a checkbox. The table includes the following values:

For the Install checkbox selected by default, Plugin Package is gstreamer1.0-libav, and Provides is All.

For the Install checkbox that is clear by default, Plugin Package is gstreamer1.0-plugins-bad-faad, and Provides is partially displayed as MPEG.

For the Install checkbox that is clear by default, Plugin Package is gstreamer1.0-plugins-bad-videoparsers GStreamers videoparsers, and Provides is partially displayed as H.264 d.

The presenter selects the row with the Install checkbox selected by default and clicks the Install button in the window.

As a result, the Install extra multimedia plugins? window closes and the Authenticate dialog box is displayed with the following text:

To install or remove software, you need to authenticate.
An application is attempting to perform an action that requires privileges.
Authentication is required to perform this action.

It also contains the Password text box and the following two buttons: Cancel and Authenticate.

He then enters the password and clicks Authenticate. As a result, the Authenticate dialog box closes and the installation is completed.

Next he closes the video player displayed and double-clicks the how-fast.mp4 file. As a result, the file plays in the video player.

He then closes the video player and navigates to the terminal window.

so I'll do that now. So avconv, the same input, this How\ fast.ogg. I specify the time, -ss hours, minutes, and seconds, which is 10. And then -vframes 1, so I want to extract a single frame, and I'm going to call this f10.jpg, so for frame at 10 seconds. Now let's grab the frame. Now before I look at the frame, you could probably guess that it worked fine because you could see a little thumbnail image here. But I'm going to stop this video playing at 10 seconds into the video. So I Pause it, so we see this spinning logo and a little counter at the bottom. And if I open it up, I get pretty much the same thing, so that's what I expected. You may have done it slightly differently. That's okay as long as you got the same result or a similar result as I did. And that concludes this exercise on avconv.
On the Ubuntu desktop, the terminal window is displayed. In this window, the presenter runs the following command at the stevescott@ss-vb:~/Videos command prompt:

avconv -i How\ fast.ogg -ss 00:00:10 -vframes 1 f10.jpg

As a result, the following partial output is displayed:

Output #0, image2, to 'f10.jpg':
Metadata:
encoder : Lavf54.20.4
Stream #0.0: Video: mjpeg, yuvj420p, 1280x720 [PAR 1:1 DAR 16:9], q=2-31, 200 kb/s, 90k tbn, 29.97 tbc
Stream mapping:
Stream #0:0 -> #0:0 (theora -> mjpeg)
Press ctrl-c to stop encoding
frame= 0 fps= 0 q=0.0 size= 0kB time=10000000000.00 bitrate= 0.0kbits/s
frame= 1 fps= 1 q=3.3 Lsize= 0kB time=0.03 bitrate= 0.0kbits/s
video:23kB audio:0kB global headers:0kB muxing overhead -100.000000%

Next he navigates to the File Manager window that displays the contents of Videos. It now displays the following files: How fast.ogg, how-fast.mp3, how-fast.mp4, and f10.jpg.

He then double-clicks the How fast.ogg file and the file plays in the video player. Then he pauses the video at 10 seconds and points to the animated theme and time counter displayed in the video player.

Then he double-clicks the f10.jpg file and the image of the same animated theme as in the video player is displayed in the f10.jpg window. He then closes the window.

© 2022 Skillsoft Ireland Limited - All rights reserved.