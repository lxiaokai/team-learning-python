---
title: 开发必备之Git常用基础命令
date: 2018-08-29 11:40:56
tags: [Git]
---

![Git图标][page_img_url]

### 前言

这个Git常用命令的文章，之前在[掘金][juejin_git_url]和[SegmentFault][sf_git_url]都有发不过，现在想整理到个人博客中，分享给大家，所以，才在这里重新发布。如有问题，请给我留言沟通，谢谢！

### Git是什么？

Git是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个免费、开源的版本控制软件，用于敏捷高效地处理任何或小或大的项目，可以有效、高速的处理从不同的项目版本管理。夸一下说：Git是目前世界上最先进的分布式版本控制系统（PS：Git不是GitHub哦）。

<!-- more -->

### 为什么要说Git命令行？

在我们日常工作中，经常会用到Git操作。但是对于新人来讲，刚上来对Git很陌生，操作起来也很懵逼。本篇文章主要针对刚开始接触Git的新人，掌握常用的一些命令，足够日常开发使用。

### Git命令：

\# 首先，需要远程克隆一个项目

$ git clone [project-url]

\# 配置开发者的提交信息，包括用户名和邮箱

$ git config --global user.name [your-name]

$ git config --global user.email [your-email]

\# 提交文件到版本控制，两个命令配合使用

$ git add [file-dir]

$ git commit -m [comment]

\# 如果本地没有配置公钥，那么你是不是每次pull或者或者push等操作时，是不是都得需要输入Git账号密码？下面的这组命令，将能够快速的解决这个烦恼

$ git config --global credential.helper store

\# 拉取远程仓库的代码到本地工作区，一说到要拉取代码，很多人都会想到，git pull，但是我个人非常不喜欢这个命令，使用git fetch也可以，我如下两条命令拉取代码

$ git rempote update

$git rebase origin:[branch-name]

\# 拉取代码，肯定会遇到有冲突的情况，这个时候，该怎么办呢？不要慌，有冲突就解决嘛，解决我就不说了，我就说，解决冲突代码后的操作，本地代码冲突解决完毕后，执行以下命令即可，即提交解决冲突文件到工作区，继续rebase

$ git add [file-dir] 

$ git rebase --continue

\# 当然了，如果你拉取远程代码到本地遇到冲突了，你不想拉取了，想先退回到冲突前，该怎么办？执行下面的命令即可，即取消rebase

$ git rebase --abort

\# 还有一个操作，也许偶尔能用得上，也就是，你rebase错了分支或者你rebase了对的分支，但是也想要会退到rebase之前，该怎么操作呢？下面这条命令很有用，

$ git reset --hard ORIG_HEAD

\# 当然了，除了上面这条命令回退之外，下面的这条命令也可以，显示当前版本最近的几次提交，然后选择回退到某节点

$ git reflog [param]

\# 推送本地修改的代码到远程仓库，推送成功的前提是你本地的版本必须是最新的，即要与远程仓库的一直才会push成功，否则，请先拉取代码，再执行push操作

$ git push origin HEAD:[branch-name]

### 结束语

如有说的不正确的地方，请指出，相互交流、学习。

[page_img_url]: https://images.pexels.com/photos/1181253/pexels-photo-1181253.jpeg
[juejin_git_url]: https://juejin.im/post/5b136e31e51d4506a81b4952
[sf_git_url]: https://segmentfault.com/a/1190000015150907