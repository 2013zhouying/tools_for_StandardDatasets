
## 行人重识别
飞书文档链接：[部门数据集 ](https://arashivision.feishu.cn/wiki/wikcnvfg2d2WR18tijZ1vWBwESe)  


创建目的:  本数据集由部门自行采集标注，用于行人重识别模型，并进行模块化管理。

数据存储规范:  本数据集包含多个子数据集模块，各子集分别占一个子文件夹，且统一按MSMT17格式存储。所有行人重识别的子数据集文件夹命名格式为：msmtReID_Person_<日期>_<备注>。

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
        <th> person  </th>  
        <th> 17051 </th> 
        <th>  该数据集在Insta360社区数据上标注,旨在评估ReID模型性能。该数据集场景丰富，存在光照、遮挡等问题，还对每一帧标注了多种属性，包括遮挡情况，运动姿态以及拍摄角度，帮助从不同反面评估模型性能。  </th> 
        <th> 全部  </th> 
        <th> list_query.txt  </th>  
        <th> 24461 </th> 
        <th> None </th> 
        <th> 测试样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 17051 </th> 
        <th>  该数据集在Insta360社区数据上标注,旨在评估ReID模型性能。该数据集场景丰富，存在光照、遮挡等问题，还对每一帧标注了多种属性，包括遮挡情况，运动姿态以及拍摄角度，帮助从不同反面评估模型性能。  </th> 
        <th> 全部  </th> 
        <th> list_gallery.txt  </th>  
        <th> 99116 </th> 
        <th> None </th> 
        <th> 测试样本  </th>   
    </tr>
</table>
