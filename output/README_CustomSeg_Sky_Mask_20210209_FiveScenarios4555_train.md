
## 天空语义分割数据集
飞书文档链接：[天空语义分割数据集 ](https://arashivision.feishu.cn/wiki/wikcnEOGg7nmMPFrfPaH0yiOEee)  


创建目的: 1.1.数据标注案例展示
原图：000000002309.jpg
from CustomSeg_Sky_20201204_COCO
标注：000000002309.png
from CustomSeg_Sky_20201204_COCO
原图：ADE_train_00019885.jpg
from CustomSeg_Sky_20201204_ADE20K
标注：ADE_train_00019885.png
from CustomSeg_Sky_20201204_ADE20K

1.2.数据创建过程及备忘
1.2.1.现有天空分割数据集标注形式备注
 数据集采用cityscapes形式进行保存，BiSeNet算法训练采用格式；
  数据集原图保存地址：\\10.0.62.3:/media/sdc/jiapy/datasets/cityscapes/data/cityscapes_sky_sem_seg/
  数据集标注gt保存地址：\\10.0.62.3:/media/sdc/jiapy/datasets/cityscapes/data/cityscapes_sky_sem_seg_gt/annotations/
1.2.2.数据格式转换
由于bisenet算法code存在一些缺陷，为统一在mmseg下使用，全部按照规范进行统一命名转换。方便后期天空分割算法维护优化，需统一保存成mmseg训练所需的数据格式。
  转换数据标注： cityscapes format-> mmseg format 的脚本为：
  转换后的数据保存地址：\\10.0.62.3:/media/sdc/datasets/Insta360SkySemSeg

数据存储规范: 本数据集包含多个子数据集模块，各子集分别占一个子文件夹，经部门处理过的数据统一按mmsegmentation定义的Custom格式存储。所有人像分割子数据集文件夹命名格式为：CustomSeg_Sky_<日期>_<备注>。
数据集内部划分多个细分场景，以支持多种训练/测试目的。为方便检索，细分场景都提供了对应的split文本文件，它列出了该细分场景包含的所有的图片。同一张图片可以对应多个细分场景。mmsegmentation可以根据split文件读取数据。split文件存放于数据集的split_dir子文件夹。测试数据集的来源图片/视频和训练数据集相关性小，以保证测试结果有泛化意义。
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
        <th> 4555 </th> 
        <th> 分辨率大小： 小边大于500，长边尽量不超过1500 标注细节：  (1)保留8bit单通道二值图； （2）天空255像素，背景0； 分为5个大类场景，每个场景1000张左右，合计5k张左右  </th> 
        <th> total  </th> 
        <th> total.txt  </th>  
        <th> 4555 </th> 
        <th> None </th> 
        <th> 包含5中场景的训练图像，主要包含城市、高速、户外、大海、滑雪等  </th>   
    </tr>
    <tr> 
        <th> sky  </th>  
        <th> 4555 </th> 
        <th> 分辨率大小： 小边大于500，长边尽量不超过1500 标注细节：  (1)保留8bit单通道二值图； （2）天空255像素，背景0； 分为5个大类场景，每个场景1000张左右，合计5k张左右  </th> 
        <th> city  </th> 
        <th> city.txt  </th>  
        <th> 894 </th> 
        <th> None </th> 
        <th> 城市： 含骑行、驾驶、步行等；  </th>   
    </tr>
    <tr> 
        <th> sky  </th>  
        <th> 4555 </th> 
        <th> 分辨率大小： 小边大于500，长边尽量不超过1500 标注细节：  (1)保留8bit单通道二值图； （2）天空255像素，背景0； 分为5个大类场景，每个场景1000张左右，合计5k张左右  </th> 
        <th> highway  </th> 
        <th> highway.txt  </th>  
        <th> 947 </th> 
        <th> None </th> 
        <th> 高速道路：骑行、驾驶等  </th>   
    </tr>
    <tr> 
        <th> sky  </th>  
        <th> 4555 </th> 
        <th> 分辨率大小： 小边大于500，长边尽量不超过1500 标注细节：  (1)保留8bit单通道二值图； （2）天空255像素，背景0； 分为5个大类场景，每个场景1000张左右，合计5k张左右  </th> 
        <th> outdoor  </th> 
        <th> outdoor.txt  </th>  
        <th> 916 </th> 
        <th> None </th> 
        <th> 户外：骑行、驾驶、步行等；  </th>   
    </tr>
    <tr> 
        <th> sky  </th>  
        <th> 4555 </th> 
        <th> 分辨率大小： 小边大于500，长边尽量不超过1500 标注细节：  (1)保留8bit单通道二值图； （2）天空255像素，背景0； 分为5个大类场景，每个场景1000张左右，合计5k张左右  </th> 
        <th> sea  </th> 
        <th> sea.txt  </th>  
        <th> 899 </th> 
        <th> None </th> 
        <th> 河上/海上/湖上, 开船、冲浪等 ；  </th>   
    </tr>
    <tr> 
        <th> sky  </th>  
        <th> 4555 </th> 
        <th> 分辨率大小： 小边大于500，长边尽量不超过1500 标注细节：  (1)保留8bit单通道二值图； （2）天空255像素，背景0； 分为5个大类场景，每个场景1000张左右，合计5k张左右  </th> 
        <th> ski  </th> 
        <th> ski.txt  </th>  
        <th> 901 </th> 
        <th> None </th> 
        <th>  滑雪等，地面有雪景与天空白色颜色相近等难例场景；  </th>   
    </tr>
</table>
