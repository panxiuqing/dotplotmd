## HOWTO
--------
现在如何试用这个扩展

在repl下试用:
   
```.python   
import markdown 
markdown.markdown(textstring, ['Plot'])
```
   
终端下由*markdown_py*调用:

```.sh
$ ln -s /path/to/mdx_Plot.py /usr/.../markdown/extensions/mdx_plot.py 
$ markdown -x mdx_plot test.md
```

## VERSION HISEORY
------------------
#### 0.0.4 加入图片保存路径的配置选项
如要将产生的图片保存于 `./img/` 目录下：

	configs = {('img_path', './img/')}
	
-------------------------------------------------
#### 0.0.3 真正的块执行，之前那个是假的，可以使用如下语法

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
