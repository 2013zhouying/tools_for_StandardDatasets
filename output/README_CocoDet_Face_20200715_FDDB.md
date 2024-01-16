
## 人脸检测数据集
飞书文档链接：[人脸检测数据集 ](https://arashivision.feishu.cn/wiki/wikcnLjIk5gLqb4zWWZuuKoCExg)  


创建目的: 把适合产品场景的公开数据集（WIDER FACE, IJB-A, IJB-C, FDDB）转换为mmdetection可使用的COCO格式，并进行模块化管理。

数据存储规范: 本数据集包含多个子数据集模块，各子集分别占一个子文件夹，且统一按COCO格式存储。所有人脸检测子数据集文件夹命名格式为：CocoDet_Face_<日期>_<备注>。

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
        <th> face </th>  
        <th> 2845 </th> 
        <th> FDDB一共包含了2845张图片，包含彩色以及灰度图，其中的人脸总数达到5171个。这些人脸所呈现的状态多样，包括遮挡、罕见姿态、低分辨率以及失焦的情况 </th> 
        <th> val </th> 
        <th> FDDBToCoco.json </th>  
        <th> 2845 </th> 
        <th> 5171 </th> 
        <th> 测试样本 </th>   
    </tr>
</table>
