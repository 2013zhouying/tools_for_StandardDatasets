
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
        <th>   head  </th>  
        <th> 1265 </th> 
        <th>   数据来自标注组同事采集与标注，全部数据仅4个主角 用于验证安霸人头检测 用于手持云台相机人头检测验证  </th> 
        <th> None </th> 
        <th> all.json  </th>  
        <th> 1265 </th> 
        <th> 1810 </th> 
        <th> 所有场景的汇总  </th>   
    </tr>
    <tr> 
        <th>   head  </th>  
        <th> 1265 </th> 
        <th>   数据来自标注组同事采集与标注，全部数据仅4个主角 用于验证安霸人头检测 用于手持云台相机人头检测验证  </th> 
        <th> None </th> 
        <th> back_down_frames.json  </th>  
        <th> 116 </th> 
        <th> 137 </th> 
        <th> None </th>   
    </tr>
    <tr> 
        <th>   head  </th>  
        <th> 1265 </th> 
        <th>   数据来自标注组同事采集与标注，全部数据仅4个主角 用于验证安霸人头检测 用于手持云台相机人头检测验证  </th> 
        <th> None </th> 
        <th> background_person_frames.json  </th>  
        <th> 207 </th> 
        <th> 433 </th> 
        <th> None </th>   
    </tr>
    <tr> 
        <th>   head  </th>  
        <th> 1265 </th> 
        <th>   数据来自标注组同事采集与标注，全部数据仅4个主角 用于验证安霸人头检测 用于手持云台相机人头检测验证  </th> 
        <th> None </th> 
        <th> complex_background_frames.json  </th>  
        <th> 201 </th> 
        <th> 355 </th> 
        <th> None </th>   
    </tr>
    <tr> 
        <th>   head  </th>  
        <th> 1265 </th> 
        <th>   数据来自标注组同事采集与标注，全部数据仅4个主角 用于验证安霸人头检测 用于手持云台相机人头检测验证  </th> 
        <th> None </th> 
        <th> scale_change_frames.json  </th>  
        <th> 276 </th> 
        <th> 325 </th> 
        <th> None </th>   
    </tr>
    <tr> 
        <th>   head  </th>  
        <th> 1265 </th> 
        <th>   数据来自标注组同事采集与标注，全部数据仅4个主角 用于验证安霸人头检测 用于手持云台相机人头检测验证  </th> 
        <th> None </th> 
        <th> typical_head_frames.json  </th>  
        <th> 479 </th> 
        <th> 560 </th> 
        <th> None </th>   
    </tr>
</table>
