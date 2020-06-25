import re
import threading
from bs4 import BeautifulSoup
import requests
import chardet
from lxml import etree


Mutex = threading.Lock()  # 设置互斥锁
Name_start = []  # 初步存储职位名称信息
Name_end = []  # 存储最终的职位名称
Company = []  # 公司名称
Location = []  # 工作地点
Salary = []  # 薪资
Published = []  # 发布时间

# 获取每页全部的html信息
def get_content(page_num):
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99°reefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=".format(page_num)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
    }

    request = requests.get(url, headers=header)
    # 字符转码
    request.encoding = chardet.detect(request.content)['encoding']
    request.encoding = "iso-8859-1"
    html = request.content.decode('iso-8859-1').encode('iso-8859-1')

    soup = BeautifulSoup(html, 'lxml')
    soup.prettify()  # 格式化soup对象

    return soup


# 爬取1-20页的数据
def info_part1():
    for i in range(21):
        soup = get_content(i)
        # 职位名称
        name = soup.find_all('p', class_="t1")
        for each_name in name:
            Mutex.acquire()
            Name_start.append(each_name.get_text())  # 提取名称加入到 Name_start列表中
            Mutex.release()
        # 公司名称
        company = soup.find_all('span', class_="t2")
        for each_company in company:
            Mutex.acquire()
            Company.append(each_company.get_text())  # 提取公司名称加入到Company列表中
            Mutex.release()
        # 工作地点
        location = soup.find_all('span', class_="t3")
        for each_location in location:
            Mutex.acquire()
            Location.append(each_location.get_text())  # 提取工作地点加入到Location列表中
            Mutex.release()
        # 薪资情况
        salary = soup.find_all('span', class_="t4")
        for each_salary in salary:
            Mutex.acquire()
            Salary.append(each_salary.get_text())  # 提取薪资加入到Salary列表中
            Mutex.release()
        # 发布时间
        published = soup.find_all('span', class_="t5")
        for each_punlished in published:
            Mutex.acquire()
            Published.append(each_punlished.get_text())  # 提取发布时间加入到Published列表中
            Mutex.release()

# 爬取21-37页数
def info_part2():
    for i in range(21,37):
        soup = get_content(i)
        # 职位名称
        name = soup.find_all('p', class_="t1")
        for each_name in name:
            Mutex.acquire()
            Name_start.append(each_name.get_text())  # 提取名称加入到 Name_start列表中
            Mutex.release()
        # 公司名称
        company = soup.find_all('span', class_="t2")
        for each_company in company:
            Mutex.acquire()
            Company.append(each_company.get_text())  # 提取公司名称加入到Company列表中
            Mutex.release()
        # 工作地点
        location = soup.find_all('span', class_="t3")
        for each_location in location:
            Mutex.acquire()
            Location.append(each_location.get_text())  # 提取工作地点加入到Location列表中
            Mutex.release()
        # 薪资情况
        salary = soup.find_all('span', class_="t4")
        for each_salary in salary:
            Mutex.acquire()
            Salary.append(each_salary.get_text())  # 提取薪资加入到Salary列表中
            Mutex.release()
        # 发布时间
        published = soup.find_all('span', class_="t5")
        for each_punlished in published:
            Mutex.acquire()
            Published.append(each_punlished.get_text())  # 提取发布时间加入到Published列表中
            Mutex.release()



if __name__ == '__main__':
    #  通过引用不同定义的函数来实现多线程查询
    thread1 = threading.Thread(target=info_part1)
    thread2 = threading.Thread(target=info_part2)

    print("从51job网站爬到的数据如下：（共37页内容）\n（   职位名称    公司名称    公司位置     薪酬     更新时间  ）")

    thread1.run()
    thread2.run()

    for each_name in Name_start:
        Name_end.append(each_name.strip())  # 提取 Name 中的职位名称
    Name_end.insert(0, '职位')  # Name1 列表中插入“职位” 以保证数据对应

    # 存放北京地区的薪资情况
    salary = []
    for item in list(zip(Name_end, Company, Location, Salary, Published)):
        if '北京' in item[2]:
            print(item)
            salary.append(item[3])

    print("\n")
    print("北京地区的薪资情况", salary)

    # 进一步划分高、低水平薪资情况
    low_salary = []
    high_salary = []

    #  将结果中所有薪酬标准转化成月薪，方便记录
    for each_salary in salary:
        if "年" in each_salary:
            ret = re.findall(r"\d+\.?\d*", each_salary)
            low_salary.append((float(ret[0]) * 10000) / 12)
            high_salary.append((float(ret[0]) * 10000) / 12)
        if "月" in each_salary:
            ret = re.findall(r"\d+\.?\d*", each_salary)
            if "万" in each_salary:
                low_salary.append(float(ret[0]) * 10000)
                high_salary.append(float(ret[0]) * 10000)
            elif "千" in each_salary:
                low_salary.append(float(ret[0]) * 1000)
                high_salary.append(float(ret[0]) * 1000)
        if "天" in each_salary:
            ret = re.findall(r"\d+\.?\d*", each_salary)
            low_salary.append(float(ret[0]) * 30)

    low_average = sum(low_salary) / len(low_salary)
    high_average = sum(high_salary) / len(high_salary)
    print("北京地区的平均薪资水平为%.3f-%.3f" % (low_average, high_average))


