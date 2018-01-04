
setwd()
getwd()

安装包
install.package()

加载包
library()

赋值
x1<-c(1,2,3,4,5,6)

自定义函数
fun_name<-function(x) {

}

使用函数

fun_name(a)


读csv
read.csv(filePath, sep=',')
读txt
read.table()
保存记录
write.


向量
c() 




### 数据类型
对象类型	创建一个对象	对象间不同类型转换
向量	vector		as.vector(x)
因子	factor		as.factor(x)
数组	array		as.array(x)
矩阵	matrix		as.matrix(x)
数据框	data.frame	as.data.frame(x)
时间序列	ts		as.ts(x)
列表	list		as.list(x)


对象类型	类型	元素是否必须同类
向量	数值型、字符型、复数型、逻辑型		是
因子	数值型、字符型		是
数组	数值型、字符型、复数型、逻辑型	是
矩阵	数值型、字符型、复数型、逻辑型	是
数据框 		数值型、字符型、复数型、逻辑型	否，必须等长
时间序列		数值型、字符型、复数型、逻辑型	是
列表		数值型、字符型、复数型、逻辑型	否，可以不等长



常见数据处理包
data.table
ggplot2
zoo
stringr
lubridate
reshape2
dplyr


