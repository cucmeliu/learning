## 表1-2 R中的帮助函数
函 数 功 能
help.start() 打开帮助文档首页
help("foo")或?foo 查看函数foo的帮助（引号可以省略）
help.search("foo")或??foo 以foo为关键词搜索本地帮助文档
example("foo") 函数foo的使用示例（引号可以省略）
RSiteSearch("foo") 以foo为关键词搜索在线文档和邮件列表存档
apropos("foo", mode="function") 列出名称中含有foo的所有可用函数
data() 列出当前已加载包中所含的所有可用示例数据集
vignette() 列出当前已安装包中所有可用的vignette文档
vignette("foo") 为主题foo显示指定的vignette文档

## 表1-3 用于管理R工作空间的函数
函 数 功 能
getwd() 显示当前的工作目录
setwd("mydirectory") 修改当前的工作目录为mydirectory
ls() 列出当前工作空间中的对象
rm(objectlist) 移除（删除）一个或多个对象
help(options) 显示可用选项的说明
options() 显示或设置当前选项
history(#) 显示最近使用过的#个命令（默认值为25）
savehistory("myfile") 保存命令历史到文件myfile中（默认值为.Rhistory）
loadhistory("myfile") 载入一个命令历史文件（默认值为.Rhistory）
save.image("myfile") 保存工作空间到文件myfile中（默认值为.RData）
save(objectlist, file="myfile") 保存指定对象到一个文件中
load("myfile") 读取一个工作空间到当前会话中（默认值为.RData）
q() 退出R。将会询问你是否保存工作空间


## 输入输出
source("filename")可在当前会话中执行一个脚本
sink("filename")将输出重定向到文件filename中

## 表1-4 用于保存图形输出的函数
函 数 输 出
pdf("filename.pdf") PDF文件
win.metafile("filename.wmf") Windows图元文件
png("filename.png") PBG文件
jpeg("filename.jpg") JPEG文件
bmp("filename.bmp") BMP文件
postscript("filename.ps") PostScript文件





