# Document

* [Getting started with Anaconda](https://docs.anaconda.com/anaconda/user-guide/getting-started/)

### Using Navigator

- [Getting started with Navigator (10 minutes)](https://docs.anaconda.com/navigator/getting-started)
- [Navigator user guide](https://docs.anaconda.com/navigator/)

### Using conda

- [Getting started with conda (20 minutes)](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
- [Conda cheat sheet](https://conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- [Conda user guide](https://conda.io/projects/conda/en/latest/user-guide/index.html)



# Conda功能一览

- [Starting conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#starting-conda) on Windows, macOS, or Linux. 2 MINUTES
- [Managing conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-conda). Verify that Anaconda is installed and check that conda is updated to the current version. 3 MINUTES
- [Managing environments](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-envs). Create [environments](https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) and move easily between them. 5 MINUTES
- [Managing Python](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-python). Create an environment that has a different version of Python. 5 MINUTES
- [Managing packages](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-pkgs). Find packages available for you to install. Install packages. 5 MINUTES



# 一、Managing Conda

```bash
$ conda --version

conda 23.1.0
```



Update conda to the current version. 

```bash
$ conda update conda
```





# 二、Managing environments

1、创建一个新的环境并在其中安装包裹。

我们将命名环境 `snowflakes`，并安装包装`biopython` ：

```bash
$ conda create --name snowflakes biopython

# 创建名为your_env_name的环境
$ conda create --name your_env_name
# 创建制定python版本的环境
$ conda create --name your_env_name python=2.7
$ conda create --name your_env_name python=3.6
# 创建包含某些包（如numpy，scipy）的环境
$ conda create --name your_env_name numpy scipy
# 创建指定python版本下包含某些包的环境
$ conda create --name your_env_name python=3.6 numpy scipy
```



2、要使用或“激活”新环境，请键入以下内容：(`conda activate` only works on conda 4.6 and later versions.)

```bash
$ conda activate snowflakes
```



3、要查看所有环境的列表，请输入：

```bash
$ conda info --envs    or   conda info -e

# conda environments:
#
base                  *  /Users/qiyeyun/anaconda3
```



4、将当前环境更改为默认环境（base）：

```bash
$ conda activate
```



5、要停用活动环境，请使用：

```bash
$ conda deactivate
```



6、删除环境

```bash
$ conda remove -n your_env_name --all
$ conda remove --name your_env_name --all
```



7、复制某个环境

```bash
$ conda create --name new_env_name --clone old_env_name
```



# 三、Managing Python

1、创建一个名为“ Snakes”的新环境，其中包含Python 3.9：

```bash
$ conda create --name snakes python=3.9
```



2、激活新环境：

```bash
(base) ➜ ~ conda activate snakes
(snakes) ➜ ~
```



3、验证是否添加了 "snakes" 环境并活跃：

```bash
$ conda info --envs

# conda environments:
#
base                     /Users/qiyeyun/anaconda3
snakes                *  /Users/qiyeyun/anaconda3/envs/snakes
```



4、验证您当前的环境中哪个版本的Python：

```bash
(snakes) $ python --version

Python 3.9.16
```



5、更新python版本：

```bash
$ conda install python=2.7
```



6、要停用活动环境，请使用：

```bash
(snakes) ➜ ~ conda deactivate
(base) ➜ ~ conda deactivate
➜ ~
```



# 四、Managing packages

1、检查是否可以从Anaconda存储库中找到您尚未安装的软件包 "beautifulsoup4"（必须连接到Internet）：

```bash
(snakes) ➜ ~ conda search beautifulsoup4

Loading channels: done
# Name                       Version           Build  Channel
beautifulsoup4                 4.6.0          py27_1  pkgs/main
beautifulsoup4                 4.6.0  py27h9416283_1  pkgs/main
beautifulsoup4                 4.6.0  py35hb75f182_1  pkgs/main
beautifulsoup4                 4.6.0          py36_1  pkgs/main
beautifulsoup4                 4.6.0  py36h72d3c9f_1  pkgs/main
beautifulsoup4                 4.6.0          py37_1  pkgs/main
beautifulsoup4                 4.6.1          py27_0  pkgs/main
.......
```



2、将此软件包安装到当前环境中：

```bash
$ conda install beautifulsoup4
```



3、检查新安装程序是否在此环境中：

```bash
(snakes) ➜ ~ conda list

# packages in environment at /Users/qiyeyun/anaconda3/envs/snakes:
#
# Name                    Version                   Build  Channel
beautifulsoup4            4.12.0           py39hecd8cb5_0
ca-certificates           2023.01.10           hecd8cb5_0
certifi                   2022.12.7        py39hecd8cb5_0
libcxx                    14.0.6               h9765a3e_0
libffi                    3.4.2                hecd8cb5_6
ncurses                   6.4                  hcec6c5f_0
openssl                   1.1.1t               hca72f7f_0
pip                       23.0.1           py39hecd8cb5_0
python                    3.9.16               h218abb5_2
readline                  8.2                  hca72f7f_0
setuptools                65.6.3           py39hecd8cb5_0
...........
```























