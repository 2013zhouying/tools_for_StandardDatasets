
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
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> total  </th> 
        <th> total.txt  </th>  
        <th> 6003 </th> 
        <th> None </th> 
        <th> 子数据集全部训练样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> city single-person  </th> 
        <th> city.txt  </th>  
        <th> 252 </th> 
        <th> None </th> 
        <th> 城市单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> city multi-person  </th> 
        <th> city_muiltiperson.txt  </th>  
        <th> 2 </th> 
        <th> None </th> 
        <th> 城市多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> indoor single-person  </th> 
        <th> indoor.txt  </th>  
        <th> 206 </th> 
        <th> None </th> 
        <th> 室内单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> indoor multi-person  </th> 
        <th> indoor_muiltiperson.txt  </th>  
        <th> 27 </th> 
        <th> None </th> 
        <th> 室内多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> mountain motor single-person  </th> 
        <th> mountain_motor.txt  </th>  
        <th> 258 </th> 
        <th> None </th> 
        <th> 户外摩托单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> mountain motor multi-person  </th> 
        <th> mountain_motor_muiltiperson.txt  </th>  
        <th> 12 </th> 
        <th> None </th> 
        <th> 户外摩托多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> ski single-person  </th> 
        <th> ski.txt  </th>  
        <th> 905 </th> 
        <th> None </th> 
        <th> 滑雪单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> ski multi-person  </th> 
        <th> ski_muiltiperson.txt  </th>  
        <th> 381 </th> 
        <th> None </th> 
        <th> 滑雪多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> volleyball single-person  </th> 
        <th> volleyball.txt  </th>  
        <th> 429 </th> 
        <th> None </th> 
        <th> 排球单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> volleyball multi-person  </th> 
        <th> volleyball_muiltiperson.txt  </th>  
        <th> 31 </th> 
        <th> None </th> 
        <th> 排球多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> basketball single-person  </th> 
        <th> basketball.txt  </th>  
        <th> 93 </th> 
        <th> None </th> 
        <th> 篮球单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> basketball multi-person  </th> 
        <th> basketball_muiltiperson.txt  </th>  
        <th> 89 </th> 
        <th> None </th> 
        <th> 篮球多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> football single-person  </th> 
        <th> football.txt  </th>  
        <th> 155 </th> 
        <th> None </th> 
        <th> 足球单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> football multi-person  </th> 
        <th> football_muiltiperson.txt  </th>  
        <th> 61 </th> 
        <th> None </th> 
        <th> 足球多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> nature single-person  </th> 
        <th> natural.txt  </th>  
        <th> 135 </th> 
        <th> None </th> 
        <th> 自然风光单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> nature multi-person  </th> 
        <th> natural_muiltiperson.txt  </th>  
        <th> 2 </th> 
        <th> None </th> 
        <th> 自然风光多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> sea single-person  </th> 
        <th> sea.txt  </th>  
        <th> 139 </th> 
        <th> None </th> 
        <th> 大海单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> sea multi-person  </th> 
        <th> sea_muiltiperson.txt  </th>  
        <th> 1 </th> 
        <th> None </th> 
        <th> 大海多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> surfing single-person  </th> 
        <th> surfing.txt  </th>  
        <th> 465 </th> 
        <th> None </th> 
        <th> 冲浪单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> surfing multi-person  </th> 
        <th> surfing_muiltiperson.txt  </th>  
        <th> 128 </th> 
        <th> None </th> 
        <th> 冲浪多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> bike single-person  </th> 
        <th> bike.txt  </th>  
        <th> 462 </th> 
        <th> None </th> 
        <th> 自行车单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> bike multi-person  </th> 
        <th> bike_muiltiperson.txt  </th>  
        <th> 32 </th> 
        <th> None </th> 
        <th> 自行车多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> kid park single-person  </th> 
        <th> kid_park.txt  </th>  
        <th> 209 </th> 
        <th> None </th> 
        <th> 小孩公园单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> kid park multi-person  </th> 
        <th> kid_park_muiltiperson.txt  </th>  
        <th> 114 </th> 
        <th> None </th> 
        <th> 小孩公园多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> skateboard single-person  </th> 
        <th> skateboard.txt  </th>  
        <th> 200 </th> 
        <th> None </th> 
        <th> 滑板单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> skateboard multi-person  </th> 
        <th> skateboard_muiltiperson.txt  </th>  
        <th> 13 </th> 
        <th> None </th> 
        <th> 滑板多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> high jump single-person  </th> 
        <th> high_jump.txt  </th>  
        <th> 710 </th> 
        <th> None </th> 
        <th> 跳跃单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> high jump multi-person  </th> 
        <th> high_jump_muiltiperson.txt  </th>  
        <th> 51 </th> 
        <th> None </th> 
        <th> 跳跃多人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> urban nightscape single-person  </th> 
        <th> night_city.txt  </th>  
        <th> 441 </th> 
        <th> None </th> 
        <th> 夜晚城市单人  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 6003 </th> 
        <th> 主要来自网络爬虫; 图片颜色平均值和方差： R_mean= 0.5119742866785237 G_mean= 0.5409617252115138 R_mean= 0.5439563893740744 stdR = 0.14096362465034448 stdG = 0.14367774246897544 stdB = 0.18139418508939323  </th> 
        <th> urban nightscape multi-person  </th> 
        <th> night_city_muiltiperson.txt  </th>  
        <th> 4 </th> 
        <th> None </th> 
        <th> 夜晚城市多人  </th>   
    </tr>
</table>
