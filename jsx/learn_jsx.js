// wrong <div>
<div/>
<div></div>

// ���԰�JSX��ǩ����һ���������������κ�λ��ʹ�ú�ʹ�ñ���װ������
var div = <div>ddd</div>
ReactDOM.render(div);

// JSXһ����ǩ����һ����������������������ͬһ���ǣ�����ʹ��һ����ǩ��������������������Ǵ����д��
// <div></div>
// <div></div>

// ��ȷд��

<span>
    <div></div>
    <div></div>
</span>

// �Զ������ʹ���Ǳ�������ĸ��д������ĸ����дֱ�ӽ���Ϊͬ��html��ǩ��
<Test />//�Զ���
<div></div>//ֱ�ӽ���Ϊ<div></div>
<test />//ֱ�ӽ���Ϊ<test></test>,��������ǲ�ʶ��ģ��޷���ʾ

// ������������� JSX �Ļ����﷨�������� HTML ��ǩ���� < ��ͷ�������� HTML �����������������飨�� { ��ͷ�������� JavaScript ���������


// ��JSX��ʹ�ñ���

var name = "test";
<div>{name + "666"}</div>

// ��JSX��ʹ��Array������ı�����
var arr = [
  <h1>Hello world!</h1>,
    <h2>React is awesome</h2>,
    ];
    ReactDOM.render(
      <div>{arr}</div>,
        document.getElementById('example')
);

// ��JSX��ʹ�ú���
var names = ['Alice', 'Emily', 'Kate'];
<div>
    { 
           names.map(function (name) { 
	                return <div>Hello, {name}!</div>
        }) 
    }
</div>

