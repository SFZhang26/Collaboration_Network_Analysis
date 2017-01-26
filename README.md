# Centrality Analysis and Influence Maximization in Collaboration Network
## 2015年秋季"数据科学基础"课程项目<br>

通过度中心性、介数中心性、紧度中心性及Pagerank四种标准对作者进行排序 <br>
针对影响最大化问题, 基于中心性分析实验了几种算法 <br>
<br>
* 数据集来自: [aminer](https://cn.aminer.org/repuser) <br>
  总共包含了2007-2009年之间数据挖掘领域发表在SIGKDD、ICDM、CIKM三个主要会议上的论文作者合作关系，共计6394个作者、12454条合作关系 <br>
* 开源工具: [斯坦福SNAP](http://snap.stanford.edu/snap/download.html) <br>
  安装教程：[http://blog.csdn.net/kbawyg/article/details/8235755](http://blog.csdn.net/kbawyg/article/details/8235755) <br>
* 参考文献：<br>
  [1] W.Chen, Y.Wang, and S.Yang. Efﬁcientinﬂuence maximization in social networks. In Proceedings of the 15th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 2009. <br>
  [2] D.Kempe, J.M.Kleinberg, and É.Tardos. Maximizing the spread of inﬂuence through a social network. In Proceedings of the 9th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pages 137–146, 2003. <br>
  [3] J.Tang, J.Sun, C.Wang, and Z.Yang. Social inﬂuence analysis in large-scale networks. In Proceedings of the 15th ACM SIGKDD Conferenceon Knowledge Discovery and Data Mining,2009. <br>
<br>
### 简介
datamining_author_topics.dat  是作者信息 <br>
datamining_coauthor_info.dat  是合作关系信息<br>

————————————————————————————————————————<br>

Data_Processing.py  是数据预处理过程，需在其他程序执行前首先执行<br>

————————————————————————————————————————<br>

Centrality_Analysis.py  是中心性分析及Pagerank的分析<br>

————————————————————————————————————————<br>

Degree.py Betweenness.py Closeness.py Pagerank.py  是4种基于中心性分析的启发式算法(python) <br>
NewGreedy.py SingleDiscount.py DegreeDiscount.py  是[3]中提到的3种算法(python) <br>

———————————————————————————————————————— <br>

plot_Influence.m 是作图的代码(MATLAB) <br>

###实验结果
![](https://github.com/SFZhang26/Collaboration_Network_Analysis/raw/master/pic/pagerank.PNG)  
![](https://github.com/SFZhang26/Collaboration_Network_Analysis/raw/master/pic/degree.PNG)  
![](https://github.com/SFZhang26/Collaboration_Network_Analysis/raw/master/pic/betweenness.PNG)  
![](https://github.com/SFZhang26/Collaboration_Network_Analysis/raw/master/pic/closeness.PNG)  
![](https://github.com/SFZhang26/Collaboration_Network_Analysis/raw/master/pic/p0.1R1000.png)  
![](https://github.com/SFZhang26/Collaboration_Network_Analysis/raw/master/pic/p0.1.PNG)  
![](https://github.com/SFZhang26/Collaboration_Network_Analysis/raw/master/pic/p0.05R1000.png)  
![](https://github.com/SFZhang26/Collaboration_Network_Analysis/raw/master/pic/p0.05.PNG)  
