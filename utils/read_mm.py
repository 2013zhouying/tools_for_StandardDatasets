import xml.etree.ElementTree as ET



# 输入.mm文件路径，输出除一级父节点以外的所有子节点的列表
def find_subnodes_except_first_level(mm_filename):
    # 解析.mm文件
    tree = ET.parse(mm_filename)
    root = tree.getroot()

    first_level_nodes = []
    subnodes_except_first_level = []

    # 基于第一级节点进行迭代
    for first_level_node in root.findall("./node/node"):
        first_level_nodes.append(first_level_node)
        # 基于每一个第一级节点，找它的子节点（二级以及更深层级）
        for subnode in first_level_node.findall(".//node"):
            subnodes_except_first_level.append(subnode)
    
    # 提取节点的TEXT属性
    result = [
        node.get('TEXT') for node in subnodes_except_first_level
        if 'TEXT' in node.attrib
    ]

    subnode_list = []
    for node in result:
        #print(node)
        subnode_list.append(node)

    return subnode_list

# find_subnodes_except_first_level函数使用方法
subnode_list = find_subnodes_except_first_level('data/任务分类.mm')
#print('subnode_list:', subnode_list)




# 对于一个迭代列表的元素，并检查它们是否存在于另一个给定的列表中。如果不存在，它将尝试将当前元素与后续的一个或多个元素连接，直到找到匹配项。
# 输入迭代列表和给定的列表，输出对迭代列表加工后的列表
def find_and_combine_elements(source_list, target_list):
    combined_list = []
    i = 0
    while i < len(source_list):
        # 当前单独元素
        element = source_list[i]

        # 如果元素存在于target_list中，添加到combined_list中
        if element in target_list:
            combined_list.append(element)
            i += 1
        else:
            # 尝试与后续元素结合，直到结合的字符串存在于目标列表中。
            combined_word = element
            j = i + 1
            # 验证combined_word是否和target_list中某个单词匹配
            while j < len(source_list) and combined_word not in target_list:
                combined_word += ' ' + source_list[j]
                j += 1

            # 如果找到匹配项，添加到新列表中，并更新索引
            if combined_word in target_list:
                combined_list.append(combined_word)
                i = j
            else:
                # 如果无法在source_list的剩余部分找到匹配项，则停止循环
                combined_list.append(combined_word)
                break
    return combined_list



# find_and_combine_elements函数使用方法
source_str = "Object, Detection, Image, Denoising, YUV-domain, Multi-Frame, Denoising"
source_list = source_str.split(', ')
target_list = subnode_list
result = find_and_combine_elements(source_list, target_list)
# 打印结果列表
#print(result)



# 实现实现给定一个或多个名称的列表，输出该列表中元素在给定的mm文件中的所有父节点（除根节点和根节点的一级子节点外）名称列表
from lxml import etree

def read_mm_file(mm_file_path):
    try:
        with open(mm_file_path, 'rb') as file:
            return etree.parse(file)
    except Exception as e:
        print(f"Error reading the .mm file: {e}")
        return None

def get_ancestor_names_except_root_and_first(node, root):
    """获取节点的所有祖先节点名称列表，除了根节点和最上层父节点"""
    ancestors = []
    current = node.getparent()
    
    # Move up through the ancestor chain
    while current is not None and current != root:
        parent = current.getparent()
        if parent is None or parent == root:  # Ignore root node and the direct parent of current node
            break
        ancestors.append(current.get('TEXT'))
        current = parent

    return ancestors

def find_nodes_with_ancestors(root, node_name):
    """根据给定的名称找到节点，并返回这些节点的所有祖先节点的名称（除了根节点和最上层父节点）"""
    nodes_with_ancestors = {}
    for node in root.xpath(f"//node[@TEXT='{node_name}']"):
        ancestor_names = get_ancestor_names_except_root_and_first(node, root)
        nodes_with_ancestors[node.get('TEXT')] = ancestor_names
    return nodes_with_ancestors

def check_names_in_mm(mm_file_path, names_to_check):
    tree = read_mm_file(mm_file_path)
    if tree is None:
        return

    automatically_supplement_parent_nodes_list = []
    root = tree.getroot()
    
    for name_to_check in names_to_check:
        results = find_nodes_with_ancestors(root, name_to_check)
        if results:
            for name, ancestors in results.items():
                automatically_supplement_parent_nodes_list.append(name)
                if ancestors:
                    #print(f'名称 "{name}" 存在于.mm文件中。所有父节点（除根节点和最上层父节点）的名称列表:')
                    for ancestor in ancestors[:-1]:
                        #print(f' - {ancestor}')
                        automatically_supplement_parent_nodes_list.append(ancestor)
                        
                else:
                    print(f'名称 "{name}" 存在于.mm文件中, 但它没有其他父节点除了根节点和最上层父节点。')
        else:
            print(f'名称 "{name_to_check}" 不存在于.mm文件中。')
    
    return automatically_supplement_parent_nodes_list


# 使用例子
mm_file_path = 'data/任务分类.mm'  # 修改为你的.mm文件的路径
names_to_check = ['YUV-domain Single-Frame Denoising', 'Semantic Segmentation']  # 修改为你要检查的名称列表
automatically_supplement_parent_nodes_list = check_names_in_mm(mm_file_path, names_to_check)
#print(automatically_supplement_parent_nodes_list)
