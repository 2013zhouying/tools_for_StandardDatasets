
## 行人重识别
飞书文档链接：[部门数据集 ](https://arashivision.feishu.cn/wiki/wikcnvfg2d2WR18tijZ1vWBwESe)  


创建目的:  本数据集由部门自行采集标注，用于行人重识别模型，并进行模块化管理。

数据存储规范:  本数据集包含多个子数据集模块，各子集分别占一个子文件夹，且统一按MSMT17格式存储。所有行人重识别的子数据集文件夹命名格式为：msmtReID_Person_<日期>_<备注>。

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
        <th> 113676 </th> 
        <th>  该数据集由Insta360自主采集和标注，分为室内和室外两个场景；行人姿态包括行走、站立、坐下和骑车；每个行人收集充足且多样的图片，大部分图片为完整，少数为遮挡。另外，该数据集由两个摄像头捕获（现阶段不作区分）。  </th> 
        <th> 全部  </th> 
        <th>  list_train.txt   </th>  
        <th> 90627 </th> 
        <th> None </th> 
        <th>  训练样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 113676 </th> 
        <th>  该数据集由Insta360自主采集和标注，分为室内和室外两个场景；行人姿态包括行走、站立、坐下和骑车；每个行人收集充足且多样的图片，大部分图片为完整，少数为遮挡。另外，该数据集由两个摄像头捕获（现阶段不作区分）。  </th> 
        <th> complete  </th> 
        <th>  list_train.txt   </th>  
        <th> 82320 </th> 
        <th> None </th> 
        <th>  训练样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 113676 </th> 
        <th>  该数据集由Insta360自主采集和标注，分为室内和室外两个场景；行人姿态包括行走、站立、坐下和骑车；每个行人收集充足且多样的图片，大部分图片为完整，少数为遮挡。另外，该数据集由两个摄像头捕获（现阶段不作区分）。  </th> 
        <th> occlusion  </th> 
        <th>  list_train.txt   </th>  
        <th> 8307 </th> 
        <th> None </th> 
        <th>  训练样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 113676 </th> 
        <th>  该数据集由Insta360自主采集和标注，分为室内和室外两个场景；行人姿态包括行走、站立、坐下和骑车；每个行人收集充足且多样的图片，大部分图片为完整，少数为遮挡。另外，该数据集由两个摄像头捕获（现阶段不作区分）。  </th> 
        <th> 全部  </th> 
        <th>   list_val.txt  </th>  
        <th> 23049 </th> 
        <th> None </th> 
        <th>   验证样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 113676 </th> 
        <th>  该数据集由Insta360自主采集和标注，分为室内和室外两个场景；行人姿态包括行走、站立、坐下和骑车；每个行人收集充足且多样的图片，大部分图片为完整，少数为遮挡。另外，该数据集由两个摄像头捕获（现阶段不作区分）。  </th> 
        <th> complete  </th> 
        <th>   list_val.txt  </th>  
        <th> 20986 </th> 
        <th> None </th> 
        <th>   验证样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 113676 </th> 
        <th>  该数据集由Insta360自主采集和标注，分为室内和室外两个场景；行人姿态包括行走、站立、坐下和骑车；每个行人收集充足且多样的图片，大部分图片为完整，少数为遮挡。另外，该数据集由两个摄像头捕获（现阶段不作区分）。  </th> 
        <th> occlusion  </th> 
        <th>   list_val.txt  </th>  
        <th> 2063 </th> 
        <th> None </th> 
        <th>   验证样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 48505 </th> 
        <th>  该数据集由Insta360自主采集和标注，分为室内和室外两个场景；行人姿态包括行走、站立、坐下和骑车；每个行人收集充足且多样的图片，大部分图片为完整，少数为遮挡。另外，该数据集由两个摄像头捕获（现阶段不作区分）。  </th> 
        <th> 全部  </th> 
        <th>  list_query.txt  </th>  
        <th> 9550 </th> 
        <th> None </th> 
        <th>    测试样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 48505 </th> 
        <th>  该数据集由Insta360自主采集和标注，分为室内和室外两个场景；行人姿态包括行走、站立、坐下和骑车；每个行人收集充足且多样的图片，大部分图片为完整，少数为遮挡。另外，该数据集由两个摄像头捕获（现阶段不作区分）。  </th> 
        <th> complete  </th> 
        <th>  list_query.txt  </th>  
        <th> 8604 </th> 
        <th> None </th> 
        <th>    测试样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 48505 </th> 
        <th>  该数据集由Insta360自主采集和标注，分为室内和室外两个场景；行人姿态包括行走、站立、坐下和骑车；每个行人收集充足且多样的图片，大部分图片为完整，少数为遮挡。另外，该数据集由两个摄像头捕获（现阶段不作区分）。  </th> 
        <th> occlusion  </th> 
        <th>  list_query.txt  </th>  
        <th> 946 </th> 
        <th> None </th> 
        <th>    测试样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 48505 </th> 
        <th>  该数据集由Insta360自主采集和标注，分为室内和室外两个场景；行人姿态包括行走、站立、坐下和骑车；每个行人收集充足且多样的图片，大部分图片为完整，少数为遮挡。另外，该数据集由两个摄像头捕获（现阶段不作区分）。  </th> 
        <th> 全部  </th> 
        <th>  list_gallery.txt  </th>  
        <th> 38955 </th> 
        <th> None </th> 
        <th>    测试样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 48505 </th> 
        <th>  该数据集由Insta360自主采集和标注，分为室内和室外两个场景；行人姿态包括行走、站立、坐下和骑车；每个行人收集充足且多样的图片，大部分图片为完整，少数为遮挡。另外，该数据集由两个摄像头捕获（现阶段不作区分）。  </th> 
        <th> complete  </th> 
        <th>  list_gallery.txt  </th>  
        <th> 35211 </th> 
        <th> None </th> 
        <th>    测试样本  </th>   
    </tr>
    <tr> 
        <th> person  </th>  
        <th> 48505 </th> 
        <th>  该数据集由Insta360自主采集和标注，分为室内和室外两个场景；行人姿态包括行走、站立、坐下和骑车；每个行人收集充足且多样的图片，大部分图片为完整，少数为遮挡。另外，该数据集由两个摄像头捕获（现阶段不作区分）。  </th> 
        <th> occlusion  </th> 
        <th>  list_gallery.txt  </th>  
        <th> 3744 </th> 
        <th> None </th> 
        <th>    测试样本  </th>   
    </tr>
</table>
