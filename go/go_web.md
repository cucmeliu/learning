
# Go Web编程

https://wizardforcel.gitbooks.io/build-web-application-with-golang

## Go基础

### 定义变量

var var1, var2, var3 type

var var4 type = value

/*
    定义三个类型都是"type"的变量,并且分别初始化为相应的值
    vname1为v1，vname2为v2，vname3为v3
*/

var vname1, vname2, vname3 type= v1, v2, v3

/*
    定义三个变量，它们分别初始化为相应的值
    vname1为v1，vname2为v2，vname3为v3
    然后Go会根据其相应值的类型来帮你初始化它们
*/

var vname1, vname2, vname3 = v1, v2, v3

/*
    定义三个变量，它们分别初始化为相应的值
    vname1为v1，vname2为v2，vname3为v3
    编译器会根据初始化的值自动推导出相应的类型
*/

vname1, vname2, vname3 := v1, v2, v3


### 常量
const constantName = value

### 内置数据类型
布尔值的类型为bool，值是true或false，默认为false

Go同时支持int和uint整形

定义好位数的类型：rune, int8, int16, int32, int64和byte, uint8, uint16, uint32, uint64。其中rune是int32的别称，byte是uint8的别称。

浮点数的类型有float32和float64两种（没有float类型），默认是float64。

复数默认类型是complex128（64位实数+64位虚数）


### 字符串
Go中字符串是不可变的

`  括起的字符串为Raw字符串
`

### 错误类型

error

err := errors.New("emit macho dwarf: elf header corrupted")

### 分组声明


const(
    i = 100
    pi = 3.1415
    prefix = "Go_"
)

var(
    i int
    pi float32
    prefix string
)


### iota枚举

默认开始值是0，const中每增加一行加1

const(
    x = iota  // x == 0
    y = iota  // y == 1
    z = iota  // z == 2
    w  // 常量声明省略值时，默认和之前一个值的字面相同。这里隐式地说w = iota，因此w == 3。其实上面y和z可同样不用"= iota"
)


### array

var arr [n]type

a := [3]int{1, 2, 3} // 声明了一个长度为3的int数组

b := [10]int{1, 2, 3} // 声明了一个长度为10的int数组，其中前三个元素初始化为1、2、3，其它默认为0

c := [...]int{4, 5, 6} // 可以省略长度而采用`...`的方式，Go会自动根据元素个数来计算长度




