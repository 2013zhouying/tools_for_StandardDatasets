
## 普通人像数据集
飞书文档链接：[普通人像数据集 ](https://arashivision.feishu.cn/wiki/wikcn5KfTTDsiBBeAbvE7xSdLzg)  


创建目的: 为公司社区人像场景标注的视频分割VOS数据集，多为完整人像。

数据存储规范: 本数据集包含多个子数据集模块，各子集分别占一个子文件夹，且统一按Davis2017定义的格式存储。所有子数据集文件夹命名格式为：DavisVOS_<类别>_<日期>_<备注>。数据集内部划分多个细分场景，以支持多种训练/测试目的。为方便检索，细分场景都提供了对应的split文本文件，它列出了该细分场景包含的所有的视频帧文件夹。同一个视频帧文件夹可以对应多个细分场景。split文件存放于数据集的ImageSets子文件夹。测试数据集的来源图片/视频和训练数据集相关性小，以保证测试结果有泛化意义。
 数据集文件结构如下所示：
├── Insta360VOS
│ ├── DavisVOS_<object-cls>_<date-1>_<aaa>
│ │ ├── JPEGImages/
│ │ │ ├── 480p
│ │ │ │ ├── xxx.jpg
│ │ │ │ ├── yyy.jpg
│ │ │ │ ├── zzz.jpg
│ │ │ ├── ori
│ │ ├── Annotations
│ │ │ ├── 480p
│ │ │ │ ├── xxx.png
│ │ │ │ ├── yyy.png
│ │ │ │ ├── zzz.png
│ │ │ ├── ori
│ │ ├── ImageSets/ (optional)
│ │ │ ├── <split-1>.txt
│ │ │ ├── <split-2>.txt
│ ├── DavisVOS_<object-cls>_ <date-2>_<bbb>

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
        <th> 未定义 </th>  
        <th> 5480 </th> 
        <th> 来自社区视频，涵盖街拍、跑步、玩滑板等场景。标注了人物和关联的物品（例如手机、滑板），但未标注类别。 </th> 
        <th> train </th> 
        <th> None </th>  
        <th> None </th> 
        <th> None </th> 
        <th> None </th>   
    </tr>
    <tr> 
        <th> 未定义 </th>  
        <th> 369 </th> 
        <th> 来自社区视频，特别挑选了有代表性的场景。标注了人物和关联的物品（例如手机、滑板），但未标注类别。 </th> 
        <th> val </th> 
        <th> None </th>  
        <th> None </th> 
        <th> None </th> 
        <th> None </th>   
    </tr>
</table>
