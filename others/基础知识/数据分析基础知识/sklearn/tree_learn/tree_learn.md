## 机器学习决策树算法案例实战


```python
import pandas as pd
import numpy as np
```

### 构造数据

好坏比例7:3


```python
bad_df = pd.DataFrame(data={
    "sex":['男', '男', '女', '男', '女', '男'],
    "status":['单身', '已婚', '已婚', '单身', '已婚', '单身'],
    "age":[39, 25, 26, 26, 21, 27],
    "month":[15, 12, 12, 42, 30, 48],
    "amount":[1271, 1484, 609, 4370, 3441, 10961],
    "y":["bad"]*6,
})
```


```python
good_df = pd.DataFrame(data={
    "sex":['男','女','女','男','男','女','男','男','女','男','女','男','男','男'],
    "status":['单身','已婚','已婚','单身','单身','已婚','单身','单身','已婚','单身','已婚','单身','单身','单身'],
    "age":[29, 26, 26, 47, 32, 59, 56, 51, 31, 23, 28, 45, 36, 36],
    "month":[24, 12, 24, 15, 48, 15, 12, 6, 21, 13, 24, 6, 36, 12],
    "amount":[2333,763,2812,1213,7238,5045,618,1595,2782,882,1376,1750,2337,1542],
    "y":["good"]*14,
})
```


```python
df = pd.concat(objs=[bad_df,good_df],ignore_index=True)
```

### 数据预览

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sex</th>
      <th>status</th>
      <th>age</th>
      <th>month</th>
      <th>amount</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>男</td>
      <td>单身</td>
      <td>39</td>
      <td>15</td>
      <td>1271</td>
      <td>bad</td>
    </tr>
    <tr>
      <th>1</th>
      <td>男</td>
      <td>已婚</td>
      <td>25</td>
      <td>12</td>
      <td>1484</td>
      <td>bad</td>
    </tr>
    <tr>
      <th>2</th>
      <td>女</td>
      <td>已婚</td>
      <td>26</td>
      <td>12</td>
      <td>609</td>
      <td>bad</td>
    </tr>
    <tr>
      <th>3</th>
      <td>男</td>
      <td>单身</td>
      <td>26</td>
      <td>42</td>
      <td>4370</td>
      <td>bad</td>
    </tr>
    <tr>
      <th>4</th>
      <td>女</td>
      <td>已婚</td>
      <td>21</td>
      <td>30</td>
      <td>3441</td>
      <td>bad</td>
    </tr>
    <tr>
      <th>5</th>
      <td>男</td>
      <td>单身</td>
      <td>27</td>
      <td>48</td>
      <td>10961</td>
      <td>bad</td>
    </tr>
    <tr>
      <th>6</th>
      <td>男</td>
      <td>单身</td>
      <td>29</td>
      <td>24</td>
      <td>2333</td>
      <td>good</td>
    </tr>
    <tr>
      <th>7</th>
      <td>女</td>
      <td>已婚</td>
      <td>26</td>
      <td>12</td>
      <td>763</td>
      <td>good</td>
    </tr>
    <tr>
      <th>8</th>
      <td>女</td>
      <td>已婚</td>
      <td>26</td>
      <td>24</td>
      <td>2812</td>
      <td>good</td>
    </tr>
    <tr>
      <th>9</th>
      <td>男</td>
      <td>单身</td>
      <td>47</td>
      <td>15</td>
      <td>1213</td>
      <td>good</td>
    </tr>
    <tr>
      <th>10</th>
      <td>男</td>
      <td>单身</td>
      <td>32</td>
      <td>48</td>
      <td>7238</td>
      <td>good</td>
    </tr>
    <tr>
      <th>11</th>
      <td>女</td>
      <td>已婚</td>
      <td>59</td>
      <td>15</td>
      <td>5045</td>
      <td>good</td>
    </tr>
    <tr>
      <th>12</th>
      <td>男</td>
      <td>单身</td>
      <td>56</td>
      <td>12</td>
      <td>618</td>
      <td>good</td>
    </tr>
    <tr>
      <th>13</th>
      <td>男</td>
      <td>单身</td>
      <td>51</td>
      <td>6</td>
      <td>1595</td>
      <td>good</td>
    </tr>
    <tr>
      <th>14</th>
      <td>女</td>
      <td>已婚</td>
      <td>31</td>
      <td>21</td>
      <td>2782</td>
      <td>good</td>
    </tr>
    <tr>
      <th>15</th>
      <td>男</td>
      <td>单身</td>
      <td>23</td>
      <td>13</td>
      <td>882</td>
      <td>good</td>
    </tr>
    <tr>
      <th>16</th>
      <td>女</td>
      <td>已婚</td>
      <td>28</td>
      <td>24</td>
      <td>1376</td>
      <td>good</td>
    </tr>
    <tr>
      <th>17</th>
      <td>男</td>
      <td>单身</td>
      <td>45</td>
      <td>6</td>
      <td>1750</td>
      <td>good</td>
    </tr>
    <tr>
      <th>18</th>
      <td>男</td>
      <td>单身</td>
      <td>36</td>
      <td>36</td>
      <td>2337</td>
      <td>good</td>
    </tr>
    <tr>
      <th>19</th>
      <td>男</td>
      <td>单身</td>
      <td>36</td>
      <td>12</td>
      <td>1542</td>
      <td>good</td>
    </tr>
  </tbody>
</table>
解释：sex：性别，status：婚姻状况，age：年龄，month：贷款期限，amount：贷款金额，y：是否逾期，bad逾期；good未逾期

### 提出问题

**现在有一个人，sex=男，status=单身，age=24，month=12，amount=2000，根据上面的信息，判断y应该是good or bad？**

- 根据上面的信息，并没有直接的答案，比如：当age<20，y就是bad。找不到类似这样的结论。
- 可以选用决策树算法来判断，如下图。从上往下走，最后结果为1（bad）


![svg](output_8_0.png)

### 决策树解决

优点：通俗易懂，便于理解

缺点：随着样本的改变而出现不同的树

参考地址：https://www.cnblogs.com/keye/p/10564914.html  

sklearn地址：https://scikit-learn.org/stable/modules/tree.html

**简单了解一下CART（Classification And Regression Tree）**

- 最核心的一个概念，GINI系数。
$$
GINI_k=\frac{T_k}{T}*(2*\frac{T_{k0}}{T_{k}}*\frac{T_{k1}}{T_k})+\frac{S}{T}*(2*\frac{T_{s0}}{S}*\frac{T_{s1}}{S})
$$

$$
\begin{equation}\begin{split} 
&T:总样本数\\
&T_k:第k个分组的样本数\\
&T_{k0}:第k个分组的样本中y=0的样本数\\
&T_{k1}:第k个分组的样本中y=1的样本数\\
&S=T-T_k,去掉k个分组之后的所有样本数据\\
&T_{s0}:S中y=0的样本数\\
&T_{s1}:S中y=1的样本数\\
\end{split}\end{equation}
$$
- 步骤：（数值型数据，比如收入）
    1. 对收入数据去重排序后，相邻的数据取平均数，得到A1，A2，A3，...
    2. 以A1，A2，A3，...为分界线，计算每一个A对应的GINI系数，
    3. 选择最小的GINI系数为分割点，继续第1,2步，直到达到条件结束。
    4. 最小的GINI系数小于阈值，结束。
    5. 数的深度（划分的区间）大于指定的区间，结束。
-  步骤：（分类型数据，比如婚姻）
    1. 分类型数据，数据已经分好，比如分为单身（A1），已婚（A2），离婚（A3），其他（A4）
    2. 计算所有组合的GINI系数
    3. 选择最小的GINI系数为分割点，继续第1,2步，直到达到条件结束
    4. 最小的GINI系数小于阈值，结束。
    5. 数的深度（划分的区间）大于指定的区间，结束。
- 决策树步骤：
    1. 计算所有特征每一个分组的GINI系数，最小的GINI系数为根节点，划分好数据
    2. 继续计算每个划分好的GINI系数，找出最小的GINI系数，为根节点，继续重复
    3. 最小的GINI系数小于阈值，结束。
    4. 数的深度（划分的区间）大于指定的区间，结束。


```python
# 修改一下数据类型，
# sex：0（男），1（女）
# status：0（单身），1（已婚）
# y：0（good），1（bad）
df2["sex"] = df2["sex"].map(lambda x:0 if x=="男" else 1)
df2["status"] = df2["status"].map(lambda x:0 if x=="单身" else 1)
df2["y"] = df2["y"].map(lambda x:0 if x=="good" else 1)
```


```python
from sklearn import tree
X, y = df2.iloc[:,:-1],df2.iloc[:,-1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
```


```python
import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
# graph.render("tree") pdf
iris = load_iris()
dot_data = tree.export_graphviz(clf, out_file=None,proportion=True, 
                     feature_names=['sex', 'status', 'age', 'month', 'amount',],  
                     class_names=["0","1"],  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 
```


![svg](output_8_0.png)


```python
# 预测sex=男，status=单身，age=24，month=12，amount=2000，的结果
clf.predict(X=[[0,0,24,12,2000]])
# array([1])
```

预测结果为1,（bad），所以sex=男，status=单身，age=24，month=12，amount=2000的客户，可能为逾期用户。
