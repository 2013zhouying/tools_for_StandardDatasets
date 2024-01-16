
## 天空语义分割（鱼眼感知）数据集
飞书文档链接：[天空语义分割（鱼眼感知）数据集 ](https://arashivision.feishu.cn/wiki/wikcnfFXZZZDQnfNNBHrlj18EJh)  


创建目的: 需具备鱼眼天空分割能力，辅助飞行器等相关项目进行深度图估计。特制作此数据集。
大部分图像为公司全景相机拍摄的全景图，进行人工标注或使用阿里云高清天空分割sdk标注，经全景图转换得到鱼眼图及对应GT。
1.1.数据标注案例展示
1.2.1.全景图像二值图标注
原图：CustomSeg_Sky_City_00117.jpg
from CustomSeg_Sky_Mask_20210209_FiveScenarios4555_train
标注：CustomSeg_Sky_City_00117.png
from CustomSeg_Sky_Mask_20210209_FiveScenarios4555_train
原图：CustomSeg_Sky_City_00137_1.jpg
from CustomSeg_Sky_Mask_20210209_FiveScenarios4555_fish_train
原图：CustomSeg_Sky_City_00137_1.png
from CustomSeg_Sky_Mask_20210209_FiveScenarios4555_fish_train
1.2.数据创建过程及备忘
0代表背景，255代表天空。对全景图进行手工或模型标注。
1.2.2.全景图转鱼眼图
通过windows转换工具，将数据集中每张全景图映射为9张鱼眼图。
1.2.3 鱼眼图标注格式转换
为统一在mmseg下使用，方便后期算法维护优化，需统一保存成mmseg训练所需的数据格式。为了方便数据溯源，不对图片进行重命名操作。
  转换数据标注： cityscapes format-> mmseg format 

数据存储规范: 本数据集包含多个子数据集模块，各子集分别占一个子文件夹，经部门处理过的数据统一按mmsegmentation定义的Custom格式存储。所有人像分割子数据集文件夹命名格式为：CustomSeg_Sky_<日期>_<备注>。数据集内部划分多个细分场景，以支持多种训练/测试目的。为方便检索，细分场景都提供了对应的split文本文件，它列出了该细分场景包含的所有的图片。同一张图片可以对应多个细分场景。mmsegmentation可以根据split文件读取数据。split文件存放于数据集的split_dir子文件夹。测试数据集的来源图片/视频和训练数据集相关性小，以保证测试结果有泛化意义。
  数据集文件结构如下所示：
├── Insta360SemanticSeg
│ ├── CustomSeg_Sky_<date-1>_<aaa>
│ │ ├── img_dir
│ │ │ ├── train
│ │ │ │ ├── xxx.jpg
│ │ │ │ ├── yyy.jpg
│ │ │ │ ├── zzz.jpg
│ │ │ ├── val
│ │ ├── ann_dir
│ │ │ ├── train
│ │ │ │ ├── xxx.png
│ │ │ │ ├── yyy.png
│ │ │ │ ├── zzz.png
│ │ │ ├── val
│ │ ├── split_dir (optional)
│ │ │ ├── <split-1>.txt
│ │ │ ├── <split-2>.txt
│ ├── CustomSeg_Sky_<date-2>_<bbb>

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
        <th> sky  </th>  
        <th> 297 </th> 
        <th>  图像中只包含2个标签，  0：background, 255: sky;   </th> 
        <th> total  </th> 
        <th> total.txt  </th>  
        <th> None </th> 
        <th> 2880x2880  </th> 
        <th> 子数据集全部测试样本，来源为Insta360全景图像  </th>   
    </tr>
    <tr> 
        <th> sky  </th>  
        <th> 297 </th> 
        <th>  图像中只包含2个标签，  0：background, 255: sky;   </th> 
        <th> -  </th> 
        <th> -  </th>  
        <th> -  </th> 
        <th>  -  </th> 
        <th> 暂未作细分场景划分  </th>   
    </tr>
</table>
