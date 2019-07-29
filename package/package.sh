#! /bin/bash

# 构建环境
# python -m pipenv install --skip-lock

# 打包
rm -rf build
python -m pipenv run python setup.py build

# 处理启动文件
# cp package/linux/start.sh ./build/exe.linux-x86_64-3.6
# cp package/linux/stop.sh ./build/exe.linux-x86_64-3.6

# 复制配置文件
# cp project/config.py  build/exe.linux-x86_64-3.6

# 处理xlwt缺失模块问题
# cp /home/DMATAPP/.local/share/virtualenvs/dataflow_tool-Gf1Mq4Ii/lib/python3.6/site-packages/xlwt/ExcelFormulaLexer.py ./build/exe.linux-x86_64-3.6/lib/xlwt
# cp /home/DMATAPP/.local/share/virtualenvs/dataflow_tool-Gf1Mq4Ii/lib/python3.6/site-packages/xlwt/ExcelFormulaParser.py ./build/exe.linux-x86_64-3.6/lib/xlwt


# 压缩包体
zip -r build/linux.zip build/exe.linux-x86_64-3.6
