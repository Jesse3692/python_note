# git 的一些特殊操作

## 保留空的文件夹

git 默认是不提交空文件夹到版本库的，有的时候项目运行会依赖于某些路径（空文件夹），如果没有则会报错。

操作：在空文件夹中创建`.gitkeep`文件

## 忽略文件夹，但是提交某些文件/文件夹

```text
/tests/*
!/tests/utils/
!/tests/test1.txt
```

## 撤销远程仓库的提交

在日常开发中可能会提交一些错误的东西并且也push到远程仓库，这时想撤回远程仓库的提交就需要下面的操作了

```shell
# 1.撤销本地的提交
git rebase -i HEAD~2
# 2. 强制推送到远程仓库
git push origin -f
```

## 使用git large file storage

github免费仓库有限额，gitee只能企业用户使用

1. 安装git命令行扩展，下载[git-lfs](https://github.com/git-lfs/git-lfs/releases/download/v3.0.2/git-lfs-windows-v3.0.2.exe)windows版
2. 为账户设置git lfs `git lfs install`
3. 添加git lfs管理的文件类型`git lfs track "*.zip"`
4. 确保gitattributes被跟踪`git add .gitattributes`
5. 正常的提交推送就可以

## 拉取指定标签的代码

```shell
git clone -b v5.4 --depth=1 https://github.com/torvalds/linux.git
```

## 推送失败，提示shallow update not allowed

```shell
git remote add ubuntu git://kernel.ubuntu.com/ubuntu/ubuntu-focal.git
git fetch --unshallow ubuntu
```