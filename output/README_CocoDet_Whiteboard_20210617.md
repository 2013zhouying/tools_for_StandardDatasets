
## 白板检测数据集
飞书文档链接：[白板检测数据集 ](https://arashivision.feishu.cn/wiki/wikcnVOGAxfZQ7dBHHgYraAGjGg)  


创建目的: 本数据集由部门从公开数据集抽取整理或自行采集标注，用于视频会议、云台相机中的白板检测。

数据存储规范: 本数据集包含多个子数据集模块，各子集分别占一个子文件夹，且统一按COCO格式存储。所有子数据集文件夹命名格式为：CocoDet_Whiteboard_<日期>_<备注>。主要包括存在白板、屏幕、笔记本的室内教学和会议场景。

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
        <th> whiteboard,monitor,laptop  </th>  
        <th> 40186 </th> 
        <th> 从开源数据集openimagev4和object365，以及网上yandex收集的数据，包含无框的背景样本  </th> 
        <th> train   </th> 
        <th> train.json  </th>  
        <th> 19093 </th> 
        <th> 30217 </th> 
        <th> 有框的训练样本，不含无框的背景样本  </th>   
    </tr>
    <tr> 
        <th> whiteboard,monitor,laptop  </th>  
        <th> 40186 </th> 
        <th> 从开源数据集openimagev4和object365，以及网上yandex收集的数据，包含无框的背景样本  </th> 
        <th> openimagesv4_whiteboard  </th> 
        <th> openimagesv4_whiteboard.json  </th>  
        <th> 952 </th> 
        <th> 995 </th> 
        <th> 从openimagesv4抽取的whiteboard样本  </th>   
    </tr>
    <tr> 
        <th> whiteboard,monitor,laptop  </th>  
        <th> 40186 </th> 
        <th> 从开源数据集openimagev4和object365，以及网上yandex收集的数据，包含无框的背景样本  </th> 
        <th> objects365_whiteboard  </th> 
        <th> objects365_whiteboard.json  </th>  
        <th> 9304 </th> 
        <th> 6634 </th> 
        <th> 从objects365抽取的whiteboard样本  </th>   
    </tr>
    <tr> 
        <th> whiteboard,monitor,laptop  </th>  
        <th> 40186 </th> 
        <th> 从开源数据集openimagev4和object365，以及网上yandex收集的数据，包含无框的背景样本  </th> 
        <th> whiteboard_from_yandex  </th> 
        <th> whiteboard_from_yandex.json  </th>  
        <th> 10642 </th> 
        <th> 11367 </th> 
        <th> 从yandex搜索下载的whiteboard样本  </th>   
    </tr>
    <tr> 
        <th> whiteboard,monitor,laptop  </th>  
        <th> 40186 </th> 
        <th> 从开源数据集openimagev4和object365，以及网上yandex收集的数据，包含无框的背景样本  </th> 
        <th> openimagesv4_monitor  </th> 
        <th> openimagesv4_monitor.json  </th>  
        <th> 3539 </th> 
        <th> 5300 </th> 
        <th> 从openimagesv4抽取的monitor样本  </th>   
    </tr>
    <tr> 
        <th> whiteboard,monitor,laptop  </th>  
        <th> 40186 </th> 
        <th> 从开源数据集openimagev4和object365，以及网上yandex收集的数据，包含无框的背景样本  </th> 
        <th> objects365_monitor  </th> 
        <th> objects365_monitor.json  </th>  
        <th> 7000 </th> 
        <th> 4738 </th> 
        <th> 从objects365抽取的monitor样本  </th>   
    </tr>
    <tr> 
        <th> whiteboard,monitor,laptop  </th>  
        <th> 40186 </th> 
        <th> 从开源数据集openimagev4和object365，以及网上yandex收集的数据，包含无框的背景样本  </th> 
        <th> objects365_laptop  </th> 
        <th> objects365_laptop.json  </th>  
        <th> 8748 </th> 
        <th> 8764 </th> 
        <th> 从objects365抽取的laptop样本  </th>   
    </tr>
    <tr> 
        <th> whiteboard,monitor, laptop  </th>  
        <th> 8033 </th> 
        <th> 从开源数据集openimagev4和object365，以及网上yandex收集的数据，包含无框的背景样本  </th> 
        <th> val   </th> 
        <th> val.json  </th>  
        <th> 4726 </th> 
        <th> 7581 </th> 
        <th> 有框的测试样本，不含无框的背景样本  </th>   
    </tr>
</table>
