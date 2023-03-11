import requests
from tqdm import tqdm
def main():
    print('Github文件下载器(Powered by MeowRain)')
    download_source = 'https://code.meowrain.cn/'
    warn = '''
分支源码：https://github.com/hunshcn/project/archive/master.zip

release源码：https://github.com/hunshcn/project/archive/v0.1.0.tar.gz

release文件：https://github.com/hunshcn/project/releases/download/v0.1.0/example.zip

分支文件：https://github.com/hunshcn/project/blob/master/filename

    '''
    print(warn)
    github_source = input('输入github的文件链接:')
    download_url = download_source + github_source
    response = requests.get(download_url,stream=True)
    total_size = int(response.headers.get('content-length', 0))
    filename = github_source.split('/')[-1]
    print("文件大小: %0.2f MB，开始下载..." % (total_size / (1024 * 1024)))
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            with tqdm(total=total_size, unit='B', unit_scale=True) as pbar:
                for data in response.iter_content(1024):
                    # 更新进度条
                    pbar.update(len(data))
                    f.write(data)
        print('下载完成！')
    else:
        print('Download failed!')
    input("按下任意键退出")


if __name__ == '__main__':
    main()
