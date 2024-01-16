
## 人像语义分割数据集
飞书文档链接：[人像语义分割数据集 ](https://arashivision.feishu.cn/wiki/wikcnPx3plkKzBfP2PJdrFGZ0Ef)  


创建目的: 目前的人像分割相关公开数据集（例如COCO）存在数据量不足、标注精度不够精细、场景和公司产品有明显差异等问题，基于它们训练的模型在产品上效果不佳。因此，本数据集面向产品挑选场景，且标注比公开数据集更精细，使得基于本数据集训练的算法效果更符合产品期望。

人像留色数据集
  人像留色数据集主要为app人像留色功能专门搜集整理，需要自研适应性更广的人像分割模型。
  人像留色与第3节介绍的人像分割V1数据集存在细微差别。特做以下说明：
人像分割V1数据集:
1. 标注图像为经过人体检测框外扩得到的单人图像，通过检测器如yolov3等提前获取人体bbox位置，并crop成包含人体的子图；
2. 原则上只包含单人，不存在多人标注的场景; 用于抽取人像子图的原图，存在多人时要求人和人之间彼此分开，不存在重合等；
人像留色数据集：
1. 直接在原图上进行人像标注，要求人体在画面中占主体位置；
2. 每种场景区分单人和多人情况；

数据存储规范: 本数据集包含多个子数据集模块，各子集分别占一个子文件夹，且统一按mmsegmentation定义的Custom格式存储。所有人像分割子数据集文件夹命名格式为：CustomSeg_Person_<日期>_<备注>。数据集内部划分多个细分场景，以支持多种训练/测试目的。为方便检索，细分场景都提供了对应的split文本文件，它列出了该细分场景包含的所有的图片。同一张图片可以对应多个细分场景。mmsegmentation可以根据split文件读取数据。split文件存放于数据集的split_dir子文件夹。测试数据集的来源图片/视频和训练数据集相关性小，以保证测试结果有泛化意义。
 数据集文件结构如下所示：
├── Insta360SemanticSeg
│ ├── CustomSeg_Person_<date-1>_<aaa>
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
│ ├── CustomSeg_Person_<date-2>_<bbb>

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
        <th> 2290 </th> 
        <th> 主要来自网络爬虫等图像，此为网络图像第二批标注  </th> 
        <th> total  </th> 
        <th> total.txt  </th>  
        <th> 2290 </th> 
        <th> None </th> 
        <th> 子数据集全部训练样本 </th>   
    </tr>
</table>
