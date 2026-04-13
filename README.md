# V3.00

> [!INFO] 
> 推荐的 linux 软件

- [x] termux-desktop nvim
- [x] texlive-bin
- [x] nvim-plugins
- [x] application 
- [x] pkg-extra 🎏
- [ ] Todo 2026-04-13

<!-- mtoc-start -->

* [Termux restore](#termux-restore)
* [Pkg](#pkg)
* [Web](#web)
* [Git 添加子模块](#git-添加子模块)

<!-- mtoc-end -->
## Termux restore
**备份**
```bash
tar -zcvf /sdcard/v3.00_termux.tar.gz -C /data/data/com.termux/files ./home ./usr
```

**恢复备份**
```bash
tar -zxvf /sdcard/v3.00_termux.tar.gz -C /data/data/com.termux/files --recursive-unlink --preserve-permissions
```

## Pkg
1. [qbittorrent]()
```bash

pkg install qbittorrent qbittorrent-nox

```

**打开**
```bash
qbittorrent-nox
```

**密码设置**
![Screenshot_20260408_101755](/data/data/com.termux/files/home/Yu/db/screenShots/Screenshot_20260408_101755.jpg)

2. [blender4]()
```bash
pkg install blender4
```

3. [gimp]()
```bash
pkg install gimp
```

4. [kdenlive]()
```bash
pkg install kdenlive kdenlive-static
```

5. [octave]()
```bash
pkg install octave 
```
```bash
pkg install octave-x
```
```bash
pkg install octave-static
```
```bash
pkg install octave-x-static
```

**命令行运行**
```bash
octave --no-gui octave.m
```

6. [matplotlib]()
```bash
pkg install matplotlib
```

7. [iproute2]()
```bash
pkg install iproute2
```
```bash
ss -ta
```

8. [nmap]()
```bash
pkg install nmap
```
```bash
nmap 127.0.0.1
```

9. [apache2]()
```bash
pkg install apache2 
```
```bash
pkg install php-apache
```
```bash
acpachectl start
apcachectl stop
acpachectl restart
```

**配置修改**
```bash
nvim /data/data/com.termux/files/usr/etc/apache2/httpd.conf
```
```markdown
LoadModule php_module libexec/apache2/libphp.so 
```
*注释*
```makrown
LoadModule mpm_worker_module libexec/apache2/mod_mpm_worker.so
```
*取消注释*
```markdown
LoadModule mpm_prefork_module libexec/apache2/mod_mpm_prefork.so
```

*添加*
```markdown
<FilesMatch \.php$>
  SetHandler application/x-httpd-php
</FilesMatch> 
```
```markdown
<IfModule dir_module>
  DirectoryIndex index.php index.html
</IfModule>
```

*测试*
```bash
echo '<?php phpinfo(); ?>' > $PREFIX/share/apache2/default-site/htdocs/index.php
```

*打开*
```bash
http://localhost:8080
```

10. [openjdk-25-x]()
```bash
pkg install openjdk-25-x
```

11. [mariadb]()
```bash
pkg install mariadb
```
**文件目录初始化**
```bash
mariadb-install-db --user=$(whoami) --datadir="$HOME/Yu/db/mariadb"
```

**启动**
```bash
mariadbd-safe --datadir="$HOME/Yu/db/mariadb" &
```

**打开**
```bash
mariadb -u u0_a122
```

**dadbod 打开**
```bash
mariadb://root@localhost:3306//yuoek
```
```bash
sqlite:///$HOME/Yu/db/sqlite
```

**修改密码**
```bash
usr mysql;
```
```bash
set password for 'u0_a122'@'localhost' = password('123456');
```
```bash
flush privileges;
```

12. [nginx]()
```bash
pkg install nginx
```

**检查配置文件**
```bash
nginx -t
```

**修改配置文件, 端口改为:8081**
```bash
nvim $PREFIX/etc/nginx/nginx.conf
```

**启动/重加载/停止**
```bash
nginx
```
```bash
nginx -s reload
```
```bash
ngins -s stop
```

**php-fpm**
```bash
pkg install php-fpm
```

*配置 php-fpm*
```bash
nvim $PREFIX/etc/php-fpm.d/www.conf
```

*修改*  
将
```markdown
listen = /data/data/com.termux/files/usr/var/run/php-fpm.sock
```
改为
```markdown
listen = 127.0.0.1:9000
```

*配置 nginx.conf*
```bash
nvim $PREFIX/etc/nginx/nginx.conf
```
```markdown
worker_processes  1;
events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;

    server {
        listen       8081;
        server_name  localhost;
        location / {
            root   /data/data/com.termux/files/usr/share/nginx/html;
            index  index.html index.htm index.php;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /data/data/com.termux/files/usr/share/nginx/html;
        }

        location ~ \.php$ {
            root           html;
            fastcgi_pass   127.0.0.1:9000;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME  /data/data/com.termux/files/usr/share/nginx/html$fastcgi_script_name;
            include        fastcgi_params;
        }
    }
}
```

*测试*
```bash
echo '<?php phpinfo(); ?>' > $PREFIX/share/nginx/html/info.php
```

*启动*
```bash
php-fpm
```
```bash
nginx -s reload
```
```bash
http://127.0.0.1:8081/info.php
```

13. [http-server]()
```bash
npm install http-server
```
14. [php]()
```bash
pkg install php
```
**创建 index.php 文件**
```bash
echo '<?php phpinfo();?>' > www/index.php
```

**启动**
```bash
php -S 127.0.0.1:8088
```

15. [dvwa]()
```bash
wget https://github.com/ethicalhack3r/DVWA/archive/master.zip
```
```bash
unzip master.zip -d $PREFIX/share/nginx/html/
```
```bash
cd $PREFIX/share/nginx/html/
```
```bash
mv DVWA-master dvwa
```

**dvwa 配置**
```bash
cd $PREFIX/share/nginx/html/dvwa/config
```
```bash
mv config.inc.php.dist config.inc.php
```
```bash
nvim config.inc.php
```

**创建 dvwa 数据库**
```bash
mysql -uu0_a122 -p123456 -e"create database dvwa;show databases;"
```

**php.ini 配置**
```bash
php --ini
```
```bash
echo 'allow_url_include = On' > $PREFIX/etc/php/php.ini
```

**启动**
```bash
php-fpm
```
```bash
nginx
```

**登陆**
```bash
http://127.0.0.1:8081/dvwa/setup.php
```

用户名
```bash
admin/gordonb/1337/pablo/smithy
```

密码
```bash
admin/abc123/charley/letmein/password

```

16. [aria2]()
```bash
pkg install aria2
```
```bash
aria2c -v
```
```bash
aria2c --enable-rpc --rpc-listen-all
```

17. [you-get]()
```bash
pip3 install you-get  -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```
```bash
pip3 install --upgrade you-get
```
```bash
you-get --format=dash-flv720 https://www.bilibili.com/video/BV1mE411L7Rg
```
```bash
you-get 'http://music.163.com/playlist?id=489221140'
```

## Web
1. [qwerty](https://github.com/RealKai42/qwerty-learner)

**依赖**
```bash
pkg install git yarn nodejs 
```

**下载**
```bash
git clone https://github.com/RealKai42/qwerty-learner.git
```

**启动**
```bash
cd ./qwerty-learner
```
```bash
yarn install
```
```bash
yarn start
```

2. [typepad]()

## Git 添加子模块
**克隆主项目**
```bash
git@github.com:Yuoek/Yuoek.git
```

**添加子模块**
```bash
git submodule add git@github.com:Yuoek/typepad.git
```
```bash
git submodule add git@github.com:Yuoek/qwerty-learner.git
```

**主项目初始化并更新子模块**
```bash
git init
```
```bash
git update
```

或
```bash
git clone --recurse-submodules git@github.com/Yuoek/Yuoek.git
```

**更新子模块**
```bash
git submodule update --remote <子模块路径>
```


