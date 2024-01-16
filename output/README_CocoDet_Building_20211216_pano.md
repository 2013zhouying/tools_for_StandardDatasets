
## 建筑检测数据集
飞书文档链接：[建筑检测数据集 ](https://arashivision.feishu.cn/wiki/wikcncQxN01GHT4D5v1T7QItrHf)  


创建目的: 开源数据集多为平面图，且对于建筑的标注与实际项目需求存在明显差异，如所有室内的场景，全部被标为office buiding。通过在公司采集的10w张全景图中，筛选出包含建筑的全景图，然后对其进行标注。

数据存储规范: 本数据集包含多个子数据集模块，各子集分别占一个子文件夹，且统一按COCO格式存储。所有全景目标检测-建筑类别子数据集文件夹命名格式为：CocoDet_Building_<日期>_<备注>；

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
        <th> None </th>  
        <th> 47947 </th> 
        <th> 第一批全景图像标注建筑物训练集   </th> 
        <th> train   </th> 
        <th> train_1600x800.json   </th>  
        <th> 47947 </th> 
        <th> 169031 </th> 
        <th> 包含以下目录：2k_padding，five_building one_photo_18971，oner_photo_57786_buliding onex2_photo_1611_building_padding outdoor_building，panorama_6w_padding pcd_batch_01_building_padding photo_from_202105-08_building 类别合并：   </th>   
    </tr>
    <tr> 
        <th> None </th>  
        <th> 3528 </th> 
        <th> 第一批全景图像标注建筑物验证集   </th> 
        <th> val   </th> 
        <th> val_1600x800.json   </th>  
        <th> 3528 </th> 
        <th> 26585 </th> 
        <th> 第一批全景图像标注建筑物验证集 包含目录为：photo_from_202101-04_building 类别合并：   </th>   
    </tr>
</table>
