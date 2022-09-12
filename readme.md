# 1. describing your idea, 
  1 主要使用了pytrends库,用来读取Google trends的数据.
  
  2 给pytrends.get_historical_interest函数传入按要求的参数以后,会得到一个记录集,转后进行转换为按天和按周的数据,然后以JSON的格式保存入文本文件

# 2. the amount of time you spent on finishing the program code (or pseudo code), 
  2022-09-12 下午三点到四点半,一个半小时,主要时间用来研究pytrends库的用法
  
# 3. the different ways you have tried to approach the TECH ASSESSMENT, 
  原来以为数据会很大,GOOGLE会断开访问连接,后来程序写好运行一下,发现会在几秒内运行完成. 所以就没有打算再继续扩展下去.
  
  原本的打算,如果数据量太大,访问频率过高,造成连接断开的话,就需要把结果先暂时存放到REDIS里面,然后按月获得数据,并且标记每个月的状态,最后再做数据的汇总. 
  
  实际运行很快,所以复杂的方案没有实施,就是一个简单的写法就可以完成任务.
  
# 4. the reasons of settling on the current approach, and finally, 
  主要还是需要根据数据量的大小,采用不同的程序运行思路. 比如,如果想在区块链上面过滤所有的区块的交易记录,这个时候就会因为数据量巨大,需要把PYTHON写成一个后台程序,在服务器后台运行,每次运行  完成以后休息几秒,然后一直执行,这类场景适用于区块链浏览器或是用于链上监测大额交易记录等使用场景.
  
  当前项目数据量比较小,并且可以一次性执行完成,所以不用采用这种复杂的处理思路.
  
# 5. how to execute your program.
  1 首先要安装pytrends
```
  pip install pytrends
```
  2 命令行执行: 
```
  python3 bitcoin.py
```  
  
  3 然后就会在当前目录生成两个指定的文本文件
  


