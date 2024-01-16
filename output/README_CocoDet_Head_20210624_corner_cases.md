
## 人头检测数据集
飞书文档链接：[人头检测数据集 ](https://arashivision.feishu.cn/wiki/wikcnRcL7fX8aC58UKWJrW6Idwd)  


创建目的: 相机的拍摄主体往往是人，人头是重要的检测目标。人头作为目标解决了人脸背面无法定义的问题，应用将会更加广泛。因此有必要创建人头检测数据集，以备用在可能用到的产品中。

数据存储规范: 人头数据集由多个子集组成，每个子集占用一个文件夹,且统一按COCO格式存储。子集文件夹的命名格式为CocoDet_Head_<日期>_<备注>。

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
        <th> head  </th>  
        <th> 19128 </th> 
        <th> 本数据集主要是为了解决安霸人头检测器的corner cases而简历，主要场景 [侧脸、戴口罩、后脑勺、帽子、墨镜、头盔]  </th> 
        <th> None </th> 
        <th> all_20210624.json  </th>  
        <th> 19128 </th> 
        <th> 26863 </th> 
        <th> 训练样本  </th>   
    </tr>
    <tr> 
        <th> head  </th>  
        <th> 19128 </th> 
        <th> 本数据集主要是为了解决安霸人头检测器的corner cases而简历，主要场景 [侧脸、戴口罩、后脑勺、帽子、墨镜、头盔]  </th> 
        <th> None </th> 
        <th> optim_hand.json  </th>  
        <th> 1028 </th> 
        <th> 1212 </th> 
        <th> 添加人手背景以减少人手误检成人头  </th>   
    </tr>
</table>
