
## 雕塑检测数据集
飞书文档链接：[雕塑检测数据集 ](https://arashivision.feishu.cn/wiki/wikcn7sPe5z1DX3EeJuqspNChCd)  


创建目的: 对平面、全景图像完成雕塑类目标的检测。

数据存储规范: 本数据集包含多个子数据集模块，各子集分别占一个子文件夹，且统一按COCO格式存储。所有子数据集文件夹命名格式为：CocoDet_Sculpture_<日期>_<备注>。主要包括全景图像雕塑、网络采集的平面图像雕塑。

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
        <th> sculpture  </th>  
        <th> 17752 </th> 
        <th> 平面图像-雕塑目标。从互联网采集的雕塑目标  </th> 
        <th> train  </th> 
        <th> 4_27_2d_sculpture.json  </th>  
        <th> 17288 </th> 
        <th> 28132 </th> 
        <th> 训练样本  </th>   
    </tr>
    <tr> 
        <th> sculpture  </th>  
        <th> 3755 </th> 
        <th> 平面图像-雕塑目标。从互联网采集的雕塑目标。改数据为远景图片（雕塑占图片比例小）  </th> 
        <th> train  </th> 
        <th> 4_28_2d_sculpture_far.json  </th>  
        <th> 3433 </th> 
        <th> 4237 </th> 
        <th> 训练样本  </th>   
    </tr>
</table>
