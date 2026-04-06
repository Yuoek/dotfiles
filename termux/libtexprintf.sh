
pkg install -y git make clang libtool autoconf automake
git clone https://gh.llkk.cc/https://github.com/bartp5/libtexprintf.git
cd libtexprintf
./autogen.sh
./configure --prefix=$PREFIX
make
make install
rm -r libtexprintf
echo "测试"
utftex '\frac{\alpha}{\beta+x}'

