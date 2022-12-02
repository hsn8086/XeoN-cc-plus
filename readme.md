# XeoN-cc+

XeoN-cc+是一个fork自[XeoN-cc](https://github.com/XeoNK10/XeoN-cc)的项目,可用于对服务器进行压力测试.

## 使用

### 下载构建好的可执行文件

在[Releases](https://github.com/hsn8086/XeoN-cc-plus/releases)里下载打包好的文件(
以pyz结尾的需要自行安装[python](https://www.python.org/downloads/))

### 使用源码运行

注:如果你下载了构建好的可执行文件,那就不要进行这一步

提供两种方法下载:

- 使用git获取
    ```shell
    git clone https://github.com/hsn8086/XeoN-cc-plus.git
    ```
- 或是直接[下载源码](https://github.com/hsn8086/XeoN-cc-plus/archive/refs/heads/main.zip)

### 运行

使用打包好的`exe`文件:

```shell
XeoN-cc+.exe -url <url>
```

使用打包好的`pyz`包:

```shell
python XeoN-cc+.pyz -url <url>
```

使用源码:

```shell
python __main__.py -url <url>
```

## 参数

| 参数名     | 作用                                             |
|---------|------------------------------------------------|
| -h/help | 查看help(帮助)的内容                                  |
| -url    | 设置目标网址                                         |
| -m/mode | 攻击方式(默认是CC攻击,所以不用调试了)                          |
| -v      | 设置代理类型                                         |
| -t      | 设置线程 (默认是800)  温馨提示(如果是手机或者配置一般的设备建议最大线程为1000) |
| -f      | 指定代理文件 (默认代理文件:proxy.txt)                      |
| -s      | 设置攻击时间(默认攻击60秒)                                |
| -down   | 下载代理                                           |
| -check  | 检查代理                                           |

## 免责声明

此软件仅用于<strong>个人</strong>服务器的压力测试.请勿攻击他人服务器!!!请勿用于<strong>任何</strong>非法用途!!!
若造成任何损失,本软件一概不负责.