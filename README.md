# cloud-text-clipboard

用于在不同网络的机器之间通过一个公网机器临时拷贝个文本，没做任何安全方面考虑，用时启动，用完必须关闭。

```
pip3 install web.py
python3 cloud-text-clipboard-web.py
```

使用/copy?text=xxxx 得到paste的url，使用url访问，得到结果

可以使用postman之类的工具简单完成

在命令行粘贴：

```
wget http://localhost:8080/paste/0 -qO-
```

