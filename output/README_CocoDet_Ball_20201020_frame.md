
## 球类检测数据集
飞书文档链接：[球类检测数据集 ](https://arashivision.feishu.cn/wiki/wikcnJnqjOfW894XaogpXa3wnKc)  


创建目的: 球类的公开数据集可利用的数据太少。例如COCO数据集sports ball类别的图片只有2986张，而且里面很多的网球/棒球等不符合公司场景的球类。object365的球类可用类别有basketball和volleyball，一共只有3327张。针对球类的公开数据集场景和数据量也都很有限。这些公开数据不足以用在产品上。本数据集由部门自行采集标注，用于球类的检测跟踪任务。

数据存储规范: 本数据集包含多个子数据集模块，各子集分别占一个子文件夹，且统一按COCO格式存储。所有子数据集文件夹命名格式为：CocoDet_Ball_<日期>_<备注>。产品数据主要场景包括足球，篮球，排球等球体较大的球类的运动，但不包括羽毛球，网球等小球。

## 数据集介绍

<table>
    <tr>
        <th rowspan="2"> 类别 </th> 
        <th rowspan="2"> 图片数量 </th> 
        <th rowspan="2"> 整体描述 </th> 
        <th colspan="5"> 划分(split) </th>  
    </tr>
    <tr> 
        <td> 细分场景 </td>
        <td> 标注文件 </td>
        <td> 图片数量 </td>
        <td> 检测框数量 </td>
        <td> 细分描述 </td>
    </tr>
    <tr> 
        <th> ball  </th>  
        <th> 12851 </th> 
        <th> 补充的网络视频抽帧  </th> 
        <th> train  </th> 
        <th> instances_train2020.json  </th>  
        <th> 12851 </th> 
        <th> None </th> 
        <th> 训练样本  </th>   
    </tr>
</table>
