package basic

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


const constantName = value
//如果需要，也可以明确指定常量的类型：
const Pi float32 = 3.1415926



bool

rune, int8, int16, int32, int64和byte, uint8, uint16, uint32, uint64
rune是int32的别称，byte是uint8的别称

complex128（64位实数+64位虚数）
complex64(32位实数+32位虚数)


分组声明
import(
	"fmt"
	"os"
)

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


每次 const 出现时，都会让 iota 初始化为0.
const a = iota // a=0 
const ( 
  b = iota     //b=0 
  c            //c=1 
)






