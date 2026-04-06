# Doubao

## 1. 安装依赖
pkg install -y git make clang libtool autoconf automake

## 2. 克隆源码（你当时用的仓库）
cd ~
git clone https://github.com/bartp5/libtexprintf.git
cd libtexprintf

## 3. 生成配置 + 编译（你当时的步骤）
./autogen.sh
./configure --prefix=$PREFIX
make

## 4. 安装（把 utftex 命令放进 bin）
make install

## 测试 utftex

1. 分数
utftex '\frac{\alpha}{\beta+x}'

2. 求和
utftex '\sum_{i=1}^n \frac{1}{i^2}'

3. 积分
utftex '\int_0^\infty e^{-x} dx'

4. 矩阵
utftex '\begin{pmatrix} a & b \\ c & d \end{pmatrix}'

## 测试 markdown

1. 分数
$\frac{\alpha}{\beta+x}$

2. 求和
$\sum_{i=1}^n \frac{1}{i^2}$

3. 积分
$\int_0^\infty e^{-x} dx$

4. 矩阵
$\begin{pmatrix} a & b \\ c & d \end{pmatrix}$


