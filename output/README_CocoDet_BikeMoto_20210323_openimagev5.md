
## 单车摩托检测数据集
飞书文档链接：[单车摩托检测数据集 ](https://arashivision.feishu.cn/wiki/wikcnmYFBRPSB5x9EvatktimG3c)  


创建目的: 本数据集由部门从公开数据集抽取整理或自行采集标注，用于单车和摩托车的检测，以辅助自动剪辑任务。

数据存储规范: 本数据集包含多个子数据集模块，各子集分别占一个子文件夹，且统一按COCO格式存储。所有子数据集文件夹命名格式为：CocoDet_BikeMoto_<日期>_<备注>。产品数据主要场景包括骑摩托车等室内外活动。

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
        <th> bicycle, motorcycle  </th>  
        <th> 24367 </th> 
        <th> 从openimagev5抽取的包含单车和摩托车的标注数据  </th> 
        <th> train  </th> 
        <th> instances_train2021.json  </th>  
        <th> 24367 </th> 
        <th> 53543 </th> 
        <th> 全部训练样本  </th>   
    </tr>
</table>
