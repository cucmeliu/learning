// wrong <div>
<div/>
<div></div>

// 可以把JSX标签当做一个变量，可以在任何位置使用和使用变量装起来。
var div = <div>ddd</div>
ReactDOM.render(div);

// JSX一个标签就是一个组件，当存在两个组件在同一级是，必须使用一个标签（组件）包起来。下面是错误的写法
// <div></div>
// <div></div>

// 正确写法

<span>
    <div></div>
    <div></div>
</span>

// 自定义组件使用是必须首字母大写，数字母不大写直接解析为同名html标签。
<Test />//自定义
<div></div>//直接解析为<div></div>
<test />//直接解析为<test></test>,在浏览器是不识别的，无法显示

// 上面代码体现了 JSX 的基本语法规则：遇到 HTML 标签（以 < 开头），就用 HTML 规则解析；遇到代码块（以 { 开头），就用 JavaScript 规则解析。


// 在JSX中使用变量

var name = "test";
<div>{name + "666"}</div>

// 在JSX中使用Array（特殊的变量）
var arr = [
  <h1>Hello world!</h1>,
    <h2>React is awesome</h2>,
    ];
    ReactDOM.render(
      <div>{arr}</div>,
        document.getElementById('example')
);

// 在JSX中使用函数
var names = ['Alice', 'Emily', 'Kate'];
<div>
    { 
           names.map(function (name) { 
	                return <div>Hello, {name}!</div>
        }) 
    }
</div>

