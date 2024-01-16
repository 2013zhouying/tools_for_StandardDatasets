| 数据集类型 | 数据集名称 | 类别 | 图片数量 | 整体描述 | 划分 (split) | 划分 (split) | 划分 (split) | 划分 (split) | 划分 (split) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unnamed: 0_level_1 | Unnamed: 1_level_1 | Unnamed: 2_level_1 | Unnamed: 3_level_1 | Unnamed: 4_level_1 | 细分场景 | 标注文件 | 图片数量 | 检测框数量 | 细分描述 |
| 人脸检测数据集 | CocoDet_Face_20170331_widerface | face | 159420 | WIDER FACE是基于61个事件类别组织，在尺度，姿势，遮挡，表情，装扮，光照等方面都有很大的变化范围。转为coco格式后不再有Easy, Medium, Hard的划分。 | train | instances_train2017.json | 12880 | 159420 | 训练样本 |
| 人脸检测数据集 | CocoDet_Face_20200616_IJBC | face | 262295 | 但IJB-C数据集的标注框接近人头框，与widerface一起训练时候效果不佳，因此不作为人脸检测，而作为人头检测使用 | train | instances_train2020_frames.json | 138836 | 262295 | 训练样本 |
| 人脸检测数据集 | CocoDet_Face_20170331_widerface | face | 3222 | WIDER FACE是基于61个事件类别组织，在尺度，姿势，遮挡，表情，装扮，光照等方面都有很大的变化范围。转为coco格式后不再有Easy, Medium, Hard的划分。 | val | instances_val2017.json | 3222 | 39704 | 测试样本 |
| 人脸检测数据集 | CocoDet_Face_20200715_FDDB | face | 2845 | FDDB一共包含了2845张图片，包含彩色以及灰度图，其中的人脸总数达到5171个。这些人脸所呈现的状态多样，包括遮挡、罕见姿态、低分辨率以及失焦的情况 | val | FDDBToCoco.json | 2845 | 5171 | 测试样本 |
| 人脸检测数据集 | CocoDet_Face_20200821_benchmark | face | 2150 | 图片来自公司产品oner,onex,go，由标注人员标注。包含全景图片的畸变人脸 | val | FDDBToCoco.json | 2150 | 4675 | 测试样本 |
| 人脸检测数据集 | CocoDet_Face_20200821_insta360go | face | 403 | 图片来自公司产品go，研发人员自行标注，用于与face++进行对比 | val | insta360_face_testset_coco_annotation_640x640.json | 403 | 403 | 测试样本 |
| 人脸检测数据集 | CocoDet_Face_20200616_IJBA | face | 24049 | 这个数据集仅使用其valset进行测试 | val | instances_val2020_frames.json | 24049 | 170574 | 测试样本 |
