# data-trace-competition
# 一、
**************************************************************************************
根目录下的analuse-tools包含下列脚本：
    信息处理类脚本：
        1.dealShortUrl.py
            该脚本对最常见且数量最大的三类短链接（t.cn新浪短链接、dwz.cn百度短链接、6du.in短链接）进行还原处理，具体还原手段通过请求对应api或者爬虫实现。
        2.shortUrl.py
            该脚本对剩余的短链接进行通用处理，具体实现方式通过请求对应网站api并爬取结果实现。
        3.getDomain.py
            该脚本通过对Url处理得到Url域名。
    信息收集类脚本：
        4.getDNSInfo.py
            该脚本通过Url域名得到其DNS查询结果，进而分析其当前是否可以访问，并得到其IP地址。
        5.getWhoisInfo.py
            该脚本通过Url域名的到其Whois信息，主要包括注册人，注册人邮箱等信息。
    文本对比算法脚本：
        6.simHash,py
            该脚本提供了对任意文本生成其simhash值，对两个simhash值计算汉明距离的功能。
        7.textDistance.py
            该脚本提供了一系列计算文本距离的方法。
        8.shang.py
        9.countKey.py
            该脚本提供了统计所有url中的关键字的频次。
# 二、
**************************************************************************************
根目录下的trace1包含下列文件夹：
    model--用以存储xgboost模型的文件；
    results--用以存储xgboost模型测试数据的结果。
# 三、
**************************************************************************************
根目录下的trace2包含下列文件夹：
    process-data--用以存储：
        1. 筛选后的干扰性强的云服务器域名txt文件；--noUse.txt
        2. 统计出的url中的最后一部分last-section的txt文件，按照频次排列； --last-section.txt
        3. 统计url中的中文关键字； --chinese-all.txt
        4. 统计url中的特殊中文关键字。 --chinese.txt
    results--用以存储测试数据的结果。
    根目录下还包括phase2数据文件，并没有附带在压缩文件中。
# 四、
**************************************************************************************
根目录下脚本：
    一. trace1.py
        - 利用xgboost训练以及测试trace1的文件，其中的特征选用fileSize;stringIdSize;methodIdsSize;classDefsSize;avg_size;
        max_size;min_size;opcode_count;receiver_num;service_num;activity_num;provider_num;meta-data_num;
	    没有使用permission_list和behavior特征。这样使得xgboost模型输入维度固定。
	    - xgboost训练和测试都包含在trace1.py中。
	     - data_preprocess用于处理训练用的csv数据，test_data_preprocess用于处理测试用的csv数据，data_transform用于转换数据成可用形式。
	 二. trace2相关脚本
	     1. ultis.py
	    - 读取筛选出的process-data中的四个txt文件。
	     2. trace2-1-step.py
	    - trace2中的url数据初步预处理，生成基于每个sha1对应的'site', 'ip', 'domain', 'register_username', 'email_address', 'contain_email', 'phone_number',
               'url'的csv文件。
	     3. trace2-2-step.py
	    - 利用analyse-tools工具以及专业背景知识，对url进行前期分析，总结出url如下特征：
	    Features = [0:url, 1:key, 2:last_sentence, 3:digit_domain, 4:alpha_domain, 5:domain_suffix,
                    6:class_domain, 7:len_domain, 8:len_url, 9:class_sub_domain, 10:len_sub_sec, 11:register_username]
        - 将trace-1-step中生成的csv中的url提取特征后转成trace2-2-step中的csv文件。
	     4. trace2-3-step.py
	    - 该脚本实现对不同url对比聚类功能，复杂度n*n。聚类的条件是，或者phone（哈希）相同，或者email（哈希）相同，或者遍历url，两两对比，满足以下任一条件，则认为两个url是同一类别：
	        a. 两个url完全相同，且不属于云服务器；
	        b. 两个url中，域名相同，且不属于云服务器，url结构类似；
	        c. 两个url中，域名相同，且不属于云服务器，last-sectin相同；
	        d. 两个url中，last-section相同，结构类似，且不属于云服务器；
	        e. 两个url中，中文关键字相同，域名相同，且不属于云服务器；
	        f. 两个url中，中文关键字属于process-data中筛选的中文特殊关键字。
	     - 聚类的结果保存在trace2-3-step.csv中。
	     5. trace2-4-step.py
	    - 由于4中的聚类结果经常使得某一类别特别庞大，该脚本的作用是提取出该类别所有数据，保存在trace2-4-step.csv中。
	     6. trace2-5-step.py
	    - 基于5中的筛选某一数目庞大的类别，基于或者phone（哈希）相同，或者email（哈希）相同的条件，再进行该类别下的具体细分聚类，生成最终的trace2-4-step.csv文件。
