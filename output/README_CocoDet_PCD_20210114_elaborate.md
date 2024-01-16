
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
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> 全部  </th> 
        <th> pcd.json  </th>  
        <th> 3847 </th> 
        <th> 8777 </th> 
        <th> 包含以下全部场景  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  lying person  </th> 
        <th>  lying_person.json  </th>  
        <th> 282 </th> 
        <th> 584 </th> 
        <th>  躺、摔倒、横，等非直立状态的  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  inverted person  </th> 
        <th>  inverted_person.json  </th>  
        <th> 0 </th> 
        <th> 0 </th> 
        <th> 倒立、翻滚等人头向下的姿势  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> squat person  </th> 
        <th> squat_person.json  </th>  
        <th> 64 </th> 
        <th> 206 </th> 
        <th> 下蹲的人  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> surfing person  </th> 
        <th> surfing_person.json  </th>  
        <th> 32 </th> 
        <th> 34 </th> 
        <th> 冲浪  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> bizarrely  </th> 
        <th> bizarrely_person.json  </th>  
        <th> 40 </th> 
        <th> 53 </th> 
        <th> 奇装异服  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> skateboard person  </th> 
        <th> skateboard_person.json  </th>  
        <th> 315 </th> 
        <th> 468 </th> 
        <th> 滑板  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> yoga person  </th> 
        <th> yoga_person.json  </th>  
        <th> 154 </th> 
        <th> 240 </th> 
        <th> 做瑜伽，仰卧起坐以及类似动作  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> parkour person  </th> 
        <th> parkour_person.json  </th>  
        <th> 30 </th> 
        <th> 92 </th> 
        <th> 跑酷，特技动作丰富  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> pushups person  </th> 
        <th> pushups_person.json  </th>  
        <th> 28 </th> 
        <th> 28 </th> 
        <th> 俯卧撑以及类似动作  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  side view person  </th> 
        <th>  side_view_person.json  </th>  
        <th> 1557 </th> 
        <th> 7213 </th> 
        <th>  全景相机投影，主角位于图片边缘（上下左右）的情况，如右图中图2  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  person riding  </th> 
        <th>  riding_person.json  </th>  
        <th> 1513 </th> 
        <th> 3236 </th> 
        <th>  人类其在三轮车、摩托车、自行车、马儿等载具上  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  person inside car  </th> 
        <th>  inside_car_person.json  </th>  
        <th> 353 </th> 
        <th> 1447 </th> 
        <th>  车内，坐在车内的司机或者乘客  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> reflective person   </th> 
        <th> reflective_person.json  </th>  
        <th> 34 </th> 
        <th> 77 </th> 
        <th> 反光，透过有反光的车窗、房屋窗户玻璃看到的人  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  backlighting person  </th> 
        <th>  backlighting_person.json  </th>  
        <th> 20 </th> 
        <th> 26 </th> 
        <th>  人类逆光拍照，背景光强烈导致主体暗淡甚至淹没  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  low light person  </th> 
        <th>  low_light_person.json  </th>  
        <th> 938 </th> 
        <th> 6396 </th> 
        <th>  在光线不足的场景拍的照片，人像轮廓不清晰  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  nightclub person  </th> 
        <th>  nightclub_person.json  </th>  
        <th> 257 </th> 
        <th> 2215 </th> 
        <th>  夜店，通常伴随着五颜六色的灯光闪烁着，人像的颜色异于平常  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  swimming person  </th> 
        <th>  swimming_person.json  </th>  
        <th> 74 </th> 
        <th> 162 </th> 
        <th>  游泳，身体浸在水中只露身体的一小部分，不穿衣服  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  skiing person  </th> 
        <th>  skiing_person.json  </th>  
        <th> 908 </th> 
        <th> 1679 </th> 
        <th>  滑雪，通常背景色是白色的，人也比较小  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> fake person  </th> 
        <th> fake_person.json  </th>  
        <th> None </th> 
        <th> None </th> 
        <th> 人类雕像、服装店模特等  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  occlusion person  </th> 
        <th>  occlusion_person.json  </th>  
        <th> 6350 </th> 
        <th> 23887 </th> 
        <th>  遮挡，人体不完整的，局部的（比如只有下半身）  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  intensive person  </th> 
        <th>  intensive_person.json  </th>  
        <th> 1874 </th> 
        <th> 13430 </th> 
        <th> 人群密集处人体框IOU大于0.5的， 通常拥抱、人与人前后遮挡、人体框中包含人体框、抱小孩  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  blur person  </th> 
        <th>  blur_person.json  </th>  
        <th> 165 </th> 
        <th> 836 </th> 
        <th>  运动模糊、镜头虚化、车玻璃中、水面倒影的  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  tiny person  </th> 
        <th>  tiny_person.json  </th>  
        <th> 2816 </th> 
        <th> 13227 </th> 
        <th>  包含极小标注框肉眼难以辨识的图片  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  merge person  </th> 
        <th>  merge person.json  </th>  
        <th> 661 </th> 
        <th> 5190 </th> 
        <th>  人的服饰与周围的环境颜色和纹理相似  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> side person  </th> 
        <th> side person.json  </th>  
        <th> 201 </th> 
        <th> 332 </th> 
        <th> 侧面行人  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> 待添加  </th> 
        <th> None </th>  
        <th> None </th> 
        <th> None </th> 
        <th> 标注员可根据实际情况添加场景  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  car cockpit  </th> 
        <th>  cockpit_car.json  </th>  
        <th> 27 </th> 
        <th> 103 </th> 
        <th>  从车内视角标注自己的车辆，比如驾驶室视角标引擎盖  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> darkness car  </th> 
        <th> darkness_car.json  </th>  
        <th> 1 </th> 
        <th> 3 </th> 
        <th> 夜间光线不足的情况拍到的车辆  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  backlighting car  </th> 
        <th>  backlighting_car.json  </th>  
        <th> 7 </th> 
        <th> 22 </th> 
        <th>  逆光拍照，车辆是黑色的轮廓  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  occlusion car  </th> 
        <th>  occlusion_car.json  </th>  
        <th> 1370 </th> 
        <th> 5567 </th> 
        <th>  车身不完整的，只看到局部的  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  intensive car  </th> 
        <th>  intensive_car.json  </th>  
        <th> 894 </th> 
        <th> 4548 </th> 
        <th>  车辆密集停放相互遮挡，一般在堵车路段或者停车场  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> blur car  </th> 
        <th> blur_car.json  </th>  
        <th> 144 </th> 
        <th> 315 </th> 
        <th> 车速太快产生的运动模糊、或者由于大光圈引起的镜头虚化  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  tiny car  </th> 
        <th>  tiny_car.json  </th>  
        <th> 1407 </th> 
        <th> 5304 </th> 
        <th>  车的面积占图中极小的比例，一般是由于远摄产生  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> 待添加  </th> 
        <th> None </th>  
        <th> None </th> 
        <th> None </th> 
        <th> 标注员可根据实际情况添加场景  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  lying dog  </th> 
        <th>  lying_dog.json  </th>  
        <th> 53 </th> 
        <th> 53 </th> 
        <th>  狗四脚朝天地躺着、侧躺着  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  dog by window  </th> 
        <th>  dog_by_window.json  </th>  
        <th> 86 </th> 
        <th> 184 </th> 
        <th>  狗头伸出窗外，一半身体被遮挡  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  swimming dog  </th> 
        <th>  swimming_dog.json  </th>  
        <th> 681 </th> 
        <th> 1064 </th> 
        <th>  狗游泳，视角有水上、水面、水下  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> fake dog  </th> 
        <th> fake_dog.json  </th>  
        <th> None </th> 
        <th> None </th> 
        <th> 模型狗，动漫狗，雕像狗  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  dressed dog  </th> 
        <th>  dressed_dog.json  </th>  
        <th> 857 </th> 
        <th> 2338 </th> 
        <th>  穿衣服,戴口罩的狗  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> darkness dog  </th> 
        <th> darkness_dog.json  </th>  
        <th> None </th> 
        <th> None </th> 
        <th> 暗光条件拍摄狗  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  backlighting dog  </th> 
        <th>  backlighting_dog.json  </th>  
        <th> 35 </th> 
        <th> 45 </th> 
        <th>  逆光条件拍照狗  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  occlusion dog  </th> 
        <th>  occlusion_dog.json  </th>  
        <th> 841 </th> 
        <th> 1436 </th> 
        <th>  狗的身体被遮挡、仅露出局部  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  blur dog  </th> 
        <th>  blur_dog.json  </th>  
        <th> 16 </th> 
        <th> 22 </th> 
        <th>  狗奔跑过快而产生的运动模糊、或者拍照是使用大光圈产生的镜头虚化等  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  tiny dog  </th> 
        <th>  tiny_dog.json  </th>  
        <th> 115 </th> 
        <th> 235 </th> 
        <th>  远处的狗  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th>  merge dog  </th> 
        <th>  merge_dog.json  </th>  
        <th> 187 </th> 
        <th> 203 </th> 
        <th>  狗与周围的环境颜色和纹理相似  </th>   
    </tr>
    <tr> 
        <th> person, car, dog                         </th>  
        <th>                   </th> 
        <th>                         </th> 
        <th> 待添加  </th> 
        <th> None </th>  
        <th> None </th> 
        <th> None </th> 
        <th> 标注员可根据实际情况添加场景  </th>   
    </tr>
</table>
