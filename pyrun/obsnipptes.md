用 python 将当前目录下的所有 md 内容转为 js 内容：
md 下的三级标题转为 trigger 内容，三级标题的内容转为 replacement 的内容，如下：

### cpp 
```cpp
#include <stdio.h>
int main() {

    return 0;
}

```
### python
```python 
def pr():
    print("Hello")
pr()

```


[
    // Math mode
	{trigger: "cpp", replacement: "#include <stdio.h>\nint main() {\n\n    return 0;\n}", options: "cA"},
	{trigger: "python", replacement: "def pr():\n    print("Hello")\npr()", options: "cA"},

]

将转换好的内容保存在当前文件夹下的 snipptes 下，并且文件名与原来文件名相同为md 
