## VERSION HISEORY
------------------
#### 0.0.3 正真的块执行，之前那个是假的，可以使用语法

#### test3.md

	这是一幅图
	
	{[matplot]}
	import matplotlib.pyplot as plt
	if True:
		a = [1,2,3,4]
	plt.plot(a)
	plt.savefig('img.png')
	{[/matplot]}

---------------------------------------
#### 0.0.2 改变了输入形式，改为块输入如下示例

##### test2.md
	
	这是一幅图
	
	{[matplot]}
	import matplotlib.pyplot as plt
	plt.plot([1,2,3,4])
	plt.savefig('img.png')
	{[/matplot]}

-----------------------------
#### 0.0.1 现在有试验性的简单支持
##### test1.md

	这是一幅图

	>>> import matplotlib.pyplot as plt
	>>> plt.plot([1,2,3,4])
	>>> plt.savefig('img.png')
