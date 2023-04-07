* [官方文档](https://docs.anaconda.com)
    * [Installing on macOS](https://docs.anaconda.com/anaconda/install/mac-os/)
    * [Uninstalling Anaconda Distribution](https://docs.anaconda.com/anaconda/install/uninstall/)



* [Anaconda Navigator](https://docs.anaconda.com/navigator/)

    * [Installing Anaconda  Navigator](https://docs.anaconda.com/navigator/install/#id2)

        Navigator is automatically installed when you install [Anaconda Distribution](https://docs.anaconda.com/anaconda/install/) version 4.0.0 or higher.

    * Uninstalling Anaconda Navigator

        ```bash
        $ conda remove anaconda-navigator
        ```

        

# Anaconda

Anaconda是包管理器和环境管理器。

`Anaconda Distribution` 包含 `Conda` 和 `Anaconda Navigator`，以及Python和数百个科学包。安装Anaconda时，您也安装了所有这些。

尝试使用 `Navigator` 和 `命令行` 的简单编程练习，以帮助您确定哪种方法适合您。



# Anaconda自带Python

安装完Anaconda已经自带安装好了Python，不需要你再安装Python了。

* Anaconda3 will now be installed into this location: `/Users/qiyeyun/anaconda3`

```bash
$ which python
/Users/linxiang/anaconda3/bin/python

$ which python3
/Users/linxiang/anaconda3/bin/python3
```



# Anaconda环境变量

conda initialize 变量是安装时，自动添加的

![](images/环境变量.png)



打开mac终端，输入：

```bash
➜ ~ conda --version

zsh: command not found: conda
```

添加命令：

```bash
$ echo 'export PATH="/Users/qiyeyun/anaconda3/bin:$PATH"' >> ~/.zshrc
```

解释说明：echo是返回字符串的命令，~/目录是家目录，即/Users/<个人用户名>。两个>(英文半角下的大于号)表示不改变后面文件中的原有内容，添加引号中的内容，有这个文件会自动新建。为什么是.zshrc文件呢，因为我的终端打开用的是-zsh工具。

总之就是，将单引号中的内容写到~/目录下的.zshrc文件中。

激活命令：

```bash
$ source ~/.zshrc
```



# 无端的在终端前部分出现了（base）字样

凭感觉打开了   ～/.bashrc 文件， 发现如下：

可以发现我们找到了问题的源头，那就是aconda自动加入了命令到 .bashrc中，  在我们打开终端的时候自动 执行了   conda  activate base 命令，

于是乎就有了前面所说的问题。
