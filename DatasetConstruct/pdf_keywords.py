import os
import shutil
import PyPDF2

# 定义关键词列表
keywords1 = ['human evaluation', 'manual evaluation']
#keywords2 = ['instruction','guideline','interface','screenshot','questionnaire']

# 定义源文件夹和目标文件夹路径
src_folder = 'C:\\Users\\Wenqing\\Desktop\\EMNLP_2021_2'
# dest_folder = 'C:\\Users\\Wenqing\\Desktop\\pdf_keys\\NAACL_2022'


# 遍历源文件夹中的所有文件
for filename in os.listdir(src_folder):
    # 检查是否为PDF文件
    if filename.endswith('.pdf'):
        # 读取PDF文档内容
        pdf_file = open(os.path.join(src_folder, filename), 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        content = ''
        matching_keywords = []
        for i in range(len(pdf_reader.pages)):
            content += pdf_reader.pages[i].extract_text()
        pdf_file.close()
        # 检查PDF文档内容是否包含关键词
        for keyword in keywords1:
            if keyword.lower() in content.lower():
                # 如果包含关键词，则将PDF复制到目标文件夹中
                matching_keywords.append(keyword)
                # shutil.copy2(os.path.join(src_folder, filename), dest_folder)
        if  matching_keywords:
            print(f'"{matching_keywords}" found in "{filename}" ')
            
            
            
                #break
