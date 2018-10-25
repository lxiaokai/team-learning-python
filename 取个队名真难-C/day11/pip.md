### 安装pip

具体的安装方法可以查看官网的安装说明

官方安装说明地址：[https://pip.pypa.io/en/latest/installing/#id7](https://pip.pypa.io/en/latest/installing/#id7)

Windows的用户，需要先到官网下载get-pip.py安装包，然后执行`python get-pip.py`进行安装

而如果需要在Linux上安装的话，则比较方便和快捷的，直接可以通过yum或者apt-get安装即可

yum安装
```
sudo yum install python-pip
```
apt-get安装
```
sudo apt-get install python-pip
```

更多安装方法请安装文档：[https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers](https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers)

### 利用pip安装模块

```
pip install [module_name]
```

### 查看所有已安装的模块

```
pip list
```

如果需要搜索指定的模块的话，可以使用下面的命令

```
pip list | grep requests
```

还可以使用下面的方法

```
pip search [model_name]
```

### 利用pip查看已安装的某个模块的详细信息

```
pip show --files [module_name]
```

### 检查哪些模块需要更新

```
pip list \--outdated
```

### 升级指定的模块

```
 pip install --upgrade [module_name]
```

### 卸载已经安装的模块

```
pip uninstall [module_name]
```

### 需要查看更多pip的用法

```
pip --help
```

### 更新pip本身

Windows的用户执行下面的命令

```
python -m pip install -U pip
```

Linux或者Mac OS的用户执行下面的命令

```
pip install -U pip
``
