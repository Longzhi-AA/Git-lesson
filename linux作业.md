#Linux

1.以容易理解的格式列出/home 目录中所有以”d”开头的文件目录的大小

![alt text](https://github.com/Longzhi-AA/Git-lesson/blob/master/github_Git-lesson/linuxpng/1.png)

2.列出/home 目录中所有以”s”开头的目录。

![alt text](https://github.com/Longzhi-AA/Git-lesson/blob/master/github_Git-lesson/linuxpng/2.png)

3.删除后缀名为.log 的所有，删除前逐一询问

```
rm -i *.log
```
4. cp 命令 —n 和 -u的区别

```
cp -u:只复制目标文件夹中不存在的文件或者文件内容新于目标文件夹的文件

cp -n:不覆盖已存在的文件
```
5.找你的用户目录下面的所有py文件,ls -l 查看他们的属性,然后把这些结果输入到一个文件之中

![alt text](https://github.com/Longzhi-AA/Git-lesson/blob/master/github_Git-lesson/linuxpng/3.png)

6.使用ls查看根目录 并且每行显示3个信息

![alt text](https://github.com/Longzhi-AA/Git-lesson/blob/master/github_Git-lesson/linuxpng/4.png)

7.查看所有进程信息,只查看前3行

![alt text](https://github.com/Longzhi-AA/Git-lesson/blob/master/github_Git-lesson/linuxpng/5.png)

8.分析以下问题,并给出解决方案
```
Mount is denied because the NTFS volume is already exclusively opened.
The volume may be already mounted, or another software may use it which could be identified for example by the help of the 'fuser' command.

```
挂载已经被拒绝执行因为NTFS单元已经被打开并占用或者另外一个程序正在使用这个单元; 可以用'fuser'这个命令查看被谁占用.
可以查看相应进程并kill以执行下一步操作.
```
9.ssh 服务端口是多少,ssh免密登录方式的原理是什么

```
通过ssh-copy-id 交换公钥，生成私钥对，公钥加密，私钥解密，从而实现免密登陆
```

10.权限755代表什么权限,如果我想把所有的w权限去除应该使用什么命令

```
755= rwxr-xr-x, 用户具有所有权限，用户组及其他用户具有读和执行权限。

chmod u-w xx文件名
```

