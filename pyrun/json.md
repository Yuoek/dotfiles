

将当前目录下所有md文件的三级标题内容转为 json 格式如下,内容示例如下， 写出 python 代码适用所有内容,


---
title: "dp "
date: 2025-11-09T23:03:28+08:00
categories: ""
tags: ""
series: ""
series_order: ""
type: ""
bookCollapseSection: true
---

{{< katex />}}



### vector示例


```cpp 
///////vector 示例 
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> v;

int main(){
  int n,x;
  cout << "HelloWorld" << endl;

  cin>>n;
  for(int i=0;i<n;i++){
    cin>>x;
    v.push_back(x);
  }
  
  for(int i=0;i<v.size();i++)cout<<v[i]<<' ';
  puts("");
  sort(v.begin(),v.end()); 
  for(int e:v)cout<<e<<' ';
  puts("");
  reverse(v.begin(),v.end());
  for(int e:v)cout<<e<<' ';
}

```


### vector2 

```cpp 
///////vector 示例
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

struct edge{
  int u,v,w;
  bool operator<(const edge &t)const
  {return w < t.w;}  
};
vector<edge> es;//边集 

int main(){
  int m,a,b,c;
  cin>>m;
  for(int i=1;i<=m;i++){ 
    cin>>a>>b>>c,
    es.push_back({a,b,c});
  }
  sort(es.begin(),es.end());
  for(int i=0;i<es.size();i++)
    printf("%d %d %d\n",es[i].u,es[i].v,es[i].w);
  // for(auto e : es)
  //   printf("%d %d %d\n",e.u,e.v,e.w);
}

```


{
  "dyvector示例": {
    "prefix": "dyvector示例",
    "body": [
      "///////vector 示例 ",
      "#include <iostream>",
      "#include <cstring>",
      "#include <algorithm>",
      "#include <vector>",
      "using namespace std;",
      "",
      "vector<int> v;",
      "",
      "int main(){",
      "  int n,x;",
      "  cout << \"HelloWorld\" << endl;",
      "",
      "  cin>>n;",
      "  for(int i=0;i<n;i++){",
      "    cin>>x;",
      "    v.push_back(x);",
      "  }",
      "  ",
      "  for(int i=0;i<v.size();i++)cout<<v[i]<<' ';",
      "  puts(\"\");",
      "  sort(v.begin(),v.end()); ",
      "  for(int e:v)cout<<e<<' ';",
      "  puts(\"\");",
      "  reverse(v.begin(),v.end());",
      "  for(int e:v)cout<<e<<' ';",
      "}"
    ]
  },
  "dyvector2"{
    "prefix": "dyvector2",
    "body": [
      "///////vector 示例",
      "#include <iostream>",
      "#include <cstring>",
      "#include <algorithm>",
      "#include <vector>",
      "using namespace std;",
      "",
      "struct edge{",
      "  int u,v,w;",
      "  bool operator<(const edge &t)const",
      "  {return w < t.w;}  ",
      "};",
      "vector<edge> es;//边集 ",
      "",
      "int main(){",
      "  int m,a,b,c;",
      "  cin>>m;",
      "  for(int i=1;i<=m;i++){ ",
      "    cin>>a>>b>>c,",
      "    es.push_back({a,b,c});",
      "  }",
      "  sort(es.begin(),es.end());",
      "  for(int i=0;i<es.size();i++)",
      "    printf(\"%d %d %d\\n\",es[i].u,es[i].v,es[i].w);",
      "  // for(auto e : es)",
      "  //   printf(\"%d %d %d\\n\",e.u,e.v,e.w);",
      "}"
    ]
  }
}
