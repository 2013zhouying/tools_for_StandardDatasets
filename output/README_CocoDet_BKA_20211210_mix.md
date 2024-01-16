
## 婴儿儿童成人数据集
飞书文档链接：[婴儿儿童成人数据集 ](https://arashivision.feishu.cn/wiki/wikcnmfFwYR7LFcIvLiamR1UQze)  


创建目的: 自动剪辑任务希望加入婴儿儿童成人检测器，该算法能够对视频的每一帧进行人体检测，并对人体进行年龄属性分类（婴儿、儿童或者成人），进而挑选出包含婴儿、儿童的帧并剪辑成（有趣的）视频片段。因此需要创建婴儿儿童成人数据集，每一个人体标注检测框对应年龄属性。

数据存储规范: 婴儿儿童成人数据集由多个子集组成，每个子集占用一个文件夹,且统一按COCO格式存储。子集文件夹的命名格式为CocoDet_BKA_<日期>_<备注>。

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
        <th> 婴儿儿童成人  </th>  
        <th> 14241 </th> 
        <th> 在youtube和instagram上爬取视频，并抽帧标注（该数据集的质量稍差） 
 </th> 
        <th> train  </th> 
        <th> babykids_train_clean.json   </th>  
        <th> 14241 </th> 
        <th> 31915 </th> 
        <th> 训练样本
成人检测框数量：3541
婴儿检测框数量：6734
儿童检测框数量：19484
未知类检测框数量：2156 </th>   
    </tr>
    <tr> 
        <th> 婴儿儿童成人   </th>  
        <th> 4637 </th> 
        <th> 在youtube和instagram上爬取视频，并抽帧标注（该数据集的质量稍差）  </th> 
        <th> val   </th> 
        <th> babykids_val_clean.json   </th>  
        <th> 4637 </th> 
        <th> 6677 </th> 
        <th> 测试样本
成人检测框数量：1311
婴儿检测框数量：3106
儿童检测框数量：1814
未知类检测框数量：446 </th>   
    </tr>
</table>
