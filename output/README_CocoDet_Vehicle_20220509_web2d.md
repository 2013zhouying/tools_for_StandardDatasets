
## 交通工具检测数据集
飞书文档链接：[交通工具检测数据集 ](https://arashivision.feishu.cn/wiki/wikcncD6siBndMliMJh3O8yl6UJ)  


创建目的: 全景目标检测需要能够实现对交通工具类别具备更好的效果，基于openimages 100个类别训练的模型，效果较差，无法满足全景自动剪辑项目的需求。故考虑对主要类别进行拆分，然后进行单独类别的训练实验，此为针对交通工具类别的数据拆分。

数据存储规范: 本数据集包含多个子数据集模块，各子集分别占一个子文件夹，且统一按COCO格式存储。所有全景目标检测-建筑类别子数据集文件夹命名格式为：CocoDet_Vehicle_<日期>_<备注>；

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
        <th> aircraft  </th>  
        <th> 5994 </th> 
        <th> 平面图-网络采集  </th> 
        <th> train  </th> 
        <th> aircraft_train.json  </th>  
        <th> 5994 </th> 
        <th> 9859 </th> 
        <th> 训练样本  </th>   
    </tr>
    <tr> 
        <th> airplane  </th>  
        <th> 5860 </th> 
        <th> 平面图-网络采集  </th> 
        <th> train  </th> 
        <th> airplane_train.json  </th>  
        <th> 5860 </th> 
        <th> 13744 </th> 
        <th> 训练样本  </th>   
    </tr>
    <tr> 
        <th> boat  </th>  
        <th> 9157 </th> 
        <th> 平面图-网络采集  </th> 
        <th> train  </th> 
        <th> boat_train.json  </th>  
        <th> 9157 </th> 
        <th> 20844 </th> 
        <th> 训练样本  </th>   
    </tr>
    <tr> 
        <th> snowmobile  </th>  
        <th> 5891 </th> 
        <th> 平面图-网络采集  </th> 
        <th> train  </th> 
        <th> snowmobile_train.json  </th>  
        <th> 5891 </th> 
        <th> 9268 </th> 
        <th> 训练样本  </th>   
    </tr>
    <tr> 
        <th> aircraft  </th>  
        <th> 1495 </th> 
        <th> 平面图-网络采集  </th> 
        <th> val  </th> 
        <th> aircraft_val.json  </th>  
        <th> 1495 </th> 
        <th> 2406 </th> 
        <th> 测试样本  </th>   
    </tr>
    <tr> 
        <th> airplane  </th>  
        <th> 1483 </th> 
        <th> 平面图-网络采集  </th> 
        <th> val  </th> 
        <th> airplane_train.json  </th>  
        <th> 1483 </th> 
        <th> 3222 </th> 
        <th> 测试样本  </th>   
    </tr>
    <tr> 
        <th> boat  </th>  
        <th> 1936 </th> 
        <th> 平面图-网络采集  </th> 
        <th> val  </th> 
        <th> boat_val.json  </th>  
        <th> 4472 </th> 
        <th> 4472 </th> 
        <th> 测试样本  </th>   
    </tr>
    <tr> 
        <th> snowmobile  </th>  
        <th> 1481 </th> 
        <th> 平面图-网络采集  </th> 
        <th> val  </th> 
        <th> snowmobile_val.json  </th>  
        <th> 1481 </th> 
        <th> 2370 </th> 
        <th> 测试样本  </th>   
    </tr>
</table>
