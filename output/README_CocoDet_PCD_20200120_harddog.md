
## 人车狗检测数据集
飞书文档链接：[人车狗检测数据集 ](https://arashivision.feishu.cn/wiki/wikcnt58KHrWlJ3Ig5HnCaCkSzc)  


创建目的: 我司产品的主要场景在公开数据集（COCO, object365）没有足够的复现。例如贴近镜头时的畸变，数据低分辨率转码的噪声，离镜头较远的宠物狗，以及滑雪，跳伞等运动场景。本数据集面向产品挑选场景和标注要求，使得算法指标AP/AR的提升与产品体验相符。

数据存储规范: 本数据集包含多个子数据集模块，各子集分别占一个子文件夹，且统一按COCO格式存储。所有人车狗检测子数据集文件夹命名格式为：CocoDet_PCD_<日期>_<备注>；所有车检测子数据集文件夹命名格式为：CocoDet_Car_<日期>_<备注>。产品数据主要场景包括travel, sport, reunion, party, play, etc，涵盖了下游VOT/MOT任务的各种测试场景。

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
        <th> person, car, dog  </th>  
        <th> 30034 </th> 
        <th>  用网上下载图片补充标注的狗，这批是难识别的  </th> 
        <th> train  </th> 
        <th> instances_train2020.json  </th>  
        <th> 30034 </th> 
        <th> 57367 </th> 
        <th> 训练样本  </th>   
    </tr>
</table>
